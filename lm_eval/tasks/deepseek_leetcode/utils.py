import re

import evaluate as hf_evaluate


def fallback_code_extraction(continuation: str) -> str:
    """Extract code by splitting on common patterns."""
    codelist = re.split(r"\ndef|\nclass|\nif|\n#|\nprint", continuation)
    if len(codelist) > 0:
        return codelist[0]
    else:
        return ""


def markdown_code_extraction(continuation: str) -> str:
    """Extract code from markdown blocks."""
    p_code = re.compile(r"```python\n?(.*?)\n?```", flags=re.DOTALL)
    code_blocks = p_code.findall(continuation)
    if len(code_blocks) > 0:
        return code_blocks[0]
    else:
        return fallback_code_extraction(continuation)


def pass_at_k(references: list[str], predictions: list[list[str]], k: list[int] = None):
    """Compute pass@k metric."""
    assert k is not None
    if isinstance(k, int):
        k = [k]
    compute = hf_evaluate.load("code_eval")
    res = compute.compute(
        references=references,
        predictions=predictions,
        k=k,
    )
    return res[0]


def build_predictions(resps: list[list[str]], docs: list[dict]) -> list[list[str]]:
    """Build predictions by combining prompt with extracted code."""
    result = []
    for resp, doc in zip(resps, docs, strict=True):
        preds = []
        for continuation in resp:
            # Extract code from the continuation
            if "```python" in continuation:
                content = markdown_code_extraction(continuation)
            else:
                content = fallback_code_extraction(continuation)
            completion = doc["prompt"] + content
            preds.append(completion)
        result.append(preds)
    return result
