import random


def shuffle_and_insert(lst, value, rnd):
    """Shuffle list and insert value at random position."""
    shuffled_list = lst.copy()
    rnd.shuffle(shuffled_list)
    insert_index = rnd.randint(0, len(shuffled_list))
    shuffled_list.insert(insert_index, value)
    return shuffled_list, insert_index


def get_shuffled_choices(doc):
    """Get shuffled choices with answer inserted."""
    answer = doc["answer"]
    wrong_answers = doc["wrong_answers"]
    rnd = random.Random(doc["id"])
    choices, _ = shuffle_and_insert(wrong_answers, answer, rnd)
    return choices


def get_answer_index(doc):
    """Get the index of the correct answer in shuffled choices."""
    answer = doc["answer"]
    wrong_answers = doc["wrong_answers"]
    rnd = random.Random(doc["id"])
    _, answer_index = shuffle_and_insert(wrong_answers, answer, rnd)
    return answer_index
