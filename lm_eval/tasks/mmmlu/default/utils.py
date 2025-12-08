import json
from functools import partial
from pathlib import Path

SUBJECTS_PATH = Path(__file__).resolve().parent.parent / "subjects.json"
with SUBJECTS_PATH.open(encoding="utf-8") as f:
    SUBJECTS = json.load(f)


def _filter_subject(dataset, subject):
    return dataset.filter(lambda row, subject=subject: row["Subject"] == subject)


def _register_subject_filters():
    for subject in SUBJECTS:
        globals()[f"process_{subject}"] = partial(_filter_subject, subject=subject)


_register_subject_filters()
