def doc_to_choice(doc):
    choices = []
    for i, raw_choice in enumerate(doc["choices"]):
        let = chr(65 + i)
        choice = "{let}. {raw_choice}"
        choices.append(choice)
    return choices
