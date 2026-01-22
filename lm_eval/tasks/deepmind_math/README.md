# DeepMind Mathematics Dataset

## Paper

Title: Analysing Mathematical Reasoning Abilities of Neural Models

Abstract: https://arxiv.org/abs/1904.01557

Evaluation tasks based on the DeepMind Mathematics Dataset for evaluating mathematical reasoning across various problem types including algebra, arithmetic, calculus, and number theory. The dataset contains 5,600 examples (100 per category) across 56 math categories.

Homepage: https://github.com/google-deepmind/mathematics_dataset

### Citation

```
@article{saxton2019analysing,
  title={Analysing Mathematical Reasoning Abilities of Neural Models},
  author={Saxton, David and Grefenstette, Edward and Hill, Felix and Kohli, Pushmeet},
  journal={arXiv preprint arXiv:1904.01557},
  year={2019}
}
```

### Groups, Tags, and Tasks

#### Groups

None

#### Tags

None

#### Tasks

* `deepmind_math_algebra_linear_1d`: Solving linear equations in one variable
* `deepmind_math_algebra_linear_2d`: Solving linear equations in two variables
* `deepmind_math_algebra_polynomial_roots`: Finding polynomial roots
* `deepmind_math_arithmetic_add_or_sub`: Addition and subtraction problems
* `deepmind_math_arithmetic_div`: Division problems
* `deepmind_math_arithmetic_mul`: Multiplication problems
* `deepmind_math_calculus_differentiate`: Differentiation problems
* `deepmind_math_numbers_gcd`: Greatest common divisor problems
* `deepmind_math_numbers_is_prime`: Primality testing problems
* `deepmind_math_numbers_lcm`: Least common multiple problems

### Checklist

For adding novel benchmarks/datasets to the library:

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?

### Changelog
