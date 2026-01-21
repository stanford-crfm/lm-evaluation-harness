import re

import evaluate as hf_evaluate


try:
    compute_ = hf_evaluate.load("code_eval")
    test_cases = ["assert add(2, 3)==5"]
    candidates = [["def add(a,b): return a*b"]]
    results = compute_.compute(references=test_cases, predictions=candidates, k=[1])
except Exception as e:
    raise e


def doc_to_text(doc):
    """Format the prompt for BigCodeBench."""
    instruction_prefix = "Please provide a self-contained Python script that solves the following problem in a markdown code block:"
    return instruction_prefix + "\n```\n" + doc["complete_prompt"].strip() + "\n"


def sanitize(code: str, entrypoint: str) -> str:
    """Sanitize code by extracting the relevant function."""
    # Extract code from markdown blocks if present
    pattern = r"```(?:python)?\n?(.*?)\n?```"
    matches = re.findall(pattern, code, re.DOTALL)
    if matches:
        code = matches[0]
    return code


def pass_at_k(references: list[str], predictions: list[list[str]], k: list[int] = None):
    """Compute pass@k metric."""
    global compute_
    assert k is not None
    if isinstance(k, int):
        k = [k]
    res = compute_.compute(
        references=references,
        predictions=predictions,
        k=k,
    )
    return res[0]


def build_predictions(resps: list[list[str]], docs: list[dict]) -> list[list[str]]:
    """Build predictions by combining prompt with completion."""
    result = []
    for resp, doc in zip(resps, docs):
        preds = []
        for r in resp:
            completion = doc["complete_prompt"] + sanitize(r, doc["entry_point"])
            preds.append(completion)
        result.append(preds)
    return result
