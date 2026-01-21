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
    """Format the prompt for DS-1000."""
    prompt = doc["prompt"]
    prompt = prompt.replace("\nBEGIN SOLUTION\n<code>\n", "\n")
    prompt = prompt.replace("    ### BEGIN SOLUTION", "")
    prompt = prompt.replace("<code>", "```python")  # replace <code> tags
    prompt = prompt.replace("</code>", "```")
    prompt = prompt + "\n"  # add newline

    # Replace:
    # "result = ... # put solution in this variable"
    # "# result = ... # put solution in this variable"
    lines = prompt.split("\n")
    for i, line in enumerate(lines):
        if "put solution" in line:
            lines[i] = "\n# " + line

            # Remove trailing ``` if present
            if i > 0 and lines[i - 1].strip() == "```":
                lines.pop(i - 1)
    prompt = "\n".join(lines)
    prompt = prompt.rstrip("\n") + "\n"  # only one trailing newline
    return prompt


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
    """Build predictions for DS-1000 code execution."""
    result = []
    for resp, doc in zip(resps, docs):
        preds = []
        for continuation in resp:
            code_context = doc["code_context"]
            # Build test program following DS-1000 format
            test_program = (
                code_context
                + "\n"
                + f"code = {repr(continuation)}\n"
                + "test_execution(code)\n"
                + ("test_string(code)\n" if "test_string(" in code_context else "\n")
            )
            preds.append(test_program)
        result.append(preds)
    return result
