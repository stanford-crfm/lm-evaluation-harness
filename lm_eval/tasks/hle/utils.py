import datasets


def process_docs_no_image(dataset: datasets.Dataset) -> datasets.Dataset:
    def _has_no_image(doc):
        img = doc.get("image")
        return not isinstance(img, str) or img.strip() == ""

    def _map_doc(doc):
        question = doc.get("question", "")
        answer = doc.get("answer", "")
        return {
            "question": question.strip(),
            "answer": answer.strip(),
        }

    keep_cols = {"question", "answer"}
    remove_cols = [c for c in dataset.column_names if c not in keep_cols]
    return dataset.filter(_has_no_image).map(_map_doc, remove_columns=remove_cols)
