import re
import string
from collections import Counter


def doc_to_text(doc):
    """Format the prompt for Jeopardy generation."""
    category, question = re.findall(r"(.*?):\s*(.*)", doc["context"])[0]
    return f"Category: {category}\nQuestion: {question}\nAnswer:"


def doc_to_text_mc(doc):
    """Format the prompt for Jeopardy multiple choice."""
    category, question = re.findall(r"(.*?):\s*(.*)", doc["context_original"])[0]
    return f"Category: {category}\nQuestion: {question}\nAnswer:"


def normalize_answer(s):
    """Normalize answer for comparison."""

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
    for pred, ref in zip(predictions, references, strict=True):
        pred_tokens = normalize_answer(pred).split()
        ref_tokens = normalize_answer(ref).split()

        if len(pred_tokens) == 0 or len(ref_tokens) == 0:
            scores.append(int(pred_tokens == ref_tokens))
            continue

        common = Counter(pred_tokens) & Counter(ref_tokens)
        num_same = sum(common.values())

        if num_same == 0:
            scores.append(0.0)
            continue

        precision = num_same / len(pred_tokens)
        recall = num_same / len(ref_tokens)
        f1 = (2 * precision * recall) / (precision + recall)
        scores.append(f1)

    return sum(scores) / len(scores) if scores else 0.0
