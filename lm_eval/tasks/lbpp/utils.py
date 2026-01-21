import base64
import json
import pickle
import zlib
from typing import Union

import evaluate as hf_evaluate


try:
    pass_at_k_metric = hf_evaluate.load("code_eval")
    test_cases = ["assert add(2, 3)==5"]
    candidates = [["def add(a,b): return a*b"]]
    results = pass_at_k_metric.compute(references=test_cases, predictions=candidates, k=[1])
except Exception as e:
    raise e


def decode_str(str_to_decode: str) -> Union[str, list, dict]:
    """Decode the encoded LBPP strings."""
    return json.loads(
        pickle.loads(zlib.decompress(base64.b64decode(str_to_decode.encode("utf-8"))))
    )


def safe_decode(value: str, field_name: str) -> Union[str, list]:
    """Safely decode LBPP encoded fields."""
    try:
        if (
            isinstance(value, str)
            and len(value) > 100
            and not value.startswith(("def ", "import ", "from "))
        ):
            return decode_str(value)
    except Exception:
        pass
    return value


def pass_at_1(
    references: Union[str, list[str]], predictions: Union[str, list[list[str]]]
) -> float:
    """Compute pass@1 metric."""
    if isinstance(references, str):
        references = [references]
    if isinstance(predictions[0], str):
        predictions = [[p] for p in predictions]
    return pass_at_k_metric.compute(
        references=references,
        predictions=predictions,
        k=[1],
    )[0]["pass@1"]


def build_predictions(resps: list[list[str]], docs: list[dict]) -> list[list[str]]:
    """Build predictions for LBPP code execution."""
    result = []
    for resp, doc in zip(resps, docs):
        preds = []

        # Decode test_list if needed
        test_list = safe_decode(doc.get("test_list", []), "test_list")
        test_setup = safe_decode(doc.get("test_setup", ""), "test_setup")

        for completion in resp:
            # Build the test program
            unittests = "\n".join(test_list) if isinstance(test_list, list) else str(test_list)

            # Add test_setup if it exists
            if test_setup:
                unittests = str(test_setup) + "\n" + unittests

            # Skip the first line (from code import...)
            lines = unittests.split("\n")
            if len(lines) > 1:
                unittests = "\n".join(lines[1:])

            # Combine completion with tests
            full_code = completion + "\n" + unittests
            preds.append(full_code)
        result.append(preds)
    return result
