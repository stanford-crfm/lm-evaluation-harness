import base64
import json
import pickle
import zlib

import evaluate as hf_evaluate


def decode_str(str_to_decode: str) -> str | list | dict:
    """Decode the encoded LBPP strings."""
    return json.loads(
        pickle.loads(zlib.decompress(base64.b64decode(str_to_decode.encode("utf-8"))))
    )


def safe_decode(value: str, field_name: str) -> str | list:
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


def pass_at_1(references: str | list[str], predictions: str | list[list[str]]) -> float:
    """Compute pass@1 metric."""
    if isinstance(references, str):
        references = [references]
    if isinstance(predictions[0], str):
        predictions = [[p] for p in predictions]
    compute = hf_evaluate.load("code_eval")
    return compute.compute(
        references=references,
        predictions=predictions,
        k=[1],
    )[0]["pass@1"]


def build_predictions(resps: list[list[str]], docs: list[dict]) -> list[list[str]]:
    """Build predictions for LBPP code execution."""
    result = []
    for resp, doc in zip(resps, docs, strict=True):
        preds = []

        # Decode test_list if needed
        test_list = safe_decode(doc.get("test_list", []), "test_list")
        test_setup = safe_decode(doc.get("test_setup", ""), "test_setup")

        for completion in resp:
            # Build the test program
            unittests = (
                "\n".join(test_list) if isinstance(test_list, list) else str(test_list)
            )

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
