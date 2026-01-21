"""Utilities for DeepMind Math tasks."""


def _filter_category(dataset, category):
    """Filter dataset to only include documents from a specific category."""
    return dataset.filter(lambda x: x["category"] == category)


# Filter functions for each category
def filter_algebra_linear_1d(dataset):
    return _filter_category(dataset, "algebra__linear_1d")


def filter_algebra_linear_2d(dataset):
    return _filter_category(dataset, "algebra__linear_2d")


def filter_algebra_polynomial_roots(dataset):
    return _filter_category(dataset, "algebra__polynomial_roots")


def filter_arithmetic_add_or_sub(dataset):
    return _filter_category(dataset, "arithmetic__add_or_sub")


def filter_arithmetic_div(dataset):
    return _filter_category(dataset, "arithmetic__div")


def filter_arithmetic_mul(dataset):
    return _filter_category(dataset, "arithmetic__mul")


def filter_calculus_differentiate(dataset):
    return _filter_category(dataset, "calculus__differentiate")


def filter_numbers_gcd(dataset):
    return _filter_category(dataset, "numbers__gcd")


def filter_numbers_lcm(dataset):
    return _filter_category(dataset, "numbers__lcm")


def filter_numbers_is_prime(dataset):
    return _filter_category(dataset, "numbers__is_prime")
