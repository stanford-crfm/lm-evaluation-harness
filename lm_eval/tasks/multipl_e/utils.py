import evaluate as hf_evaluate


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
    """Build predictions by combining prompt with completion."""
    result = []
    for resp, doc in zip(resps, docs, strict=False):
        preds = []
        for r in resp:
            completion = doc["prompt"] + r
            preds.append(completion)
        result.append(preds)
    return result
