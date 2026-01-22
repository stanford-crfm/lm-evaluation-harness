import re
import string
from collections import Counter


def normalize_answer(s):
    """Normalize answer for comparison (SQuAD-style)."""

    def remove_articles(text):
        return re.sub(r"\b(a|an|the)\b", " ", text)

    def white_space_fix(text):
        return " ".join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return "".join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def f1_score(predictions: list[str], references: list[str]) -> float:
    """Compute F1 score between prediction and reference."""
    scores = []
    for pred, ref in zip(predictions, references, strict=False):
        # Handle list of references (multiple correct answers)
        if isinstance(ref, list):
            # Compute F1 against all references and take max
            ref_scores = []
            for single_ref in ref:
                ref_scores.append(_compute_f1(pred, single_ref))
            scores.append(max(ref_scores) if ref_scores else 0.0)
        else:
            scores.append(_compute_f1(pred, ref))

    return sum(scores) / len(scores) if scores else 0.0


def _compute_f1(pred: str, ref: str) -> float:
    """Compute F1 between a single prediction and reference."""
    pred_tokens = normalize_answer(pred).split()
    ref_tokens = normalize_answer(ref).split()

    if len(pred_tokens) == 0 or len(ref_tokens) == 0:
        return float(pred_tokens == ref_tokens)

    common = Counter(pred_tokens) & Counter(ref_tokens)
    num_same = sum(common.values())

    if num_same == 0:
        return 0.0

    precision = num_same / len(pred_tokens)
    recall = num_same / len(ref_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1
