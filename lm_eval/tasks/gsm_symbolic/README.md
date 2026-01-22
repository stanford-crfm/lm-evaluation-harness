# GSM-Symbolic

## Paper

Title: GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

Abstract: https://arxiv.org/abs/2410.05229

GSM-Symbolic is a benchmark for evaluating mathematical reasoning capabilities by testing models on symbolic variations of GSM8K problems. It introduces perturbations to test the robustness of mathematical reasoning.

Homepage: https://huggingface.co/datasets/apple/GSM-Symbolic

### Citation

```
@article{mirzadeh2024gsm,
  title={GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models},
  author={Mirzadeh, Iman and Alizadeh, Keivan and Shahrokhi, Hooman and Tuzel, Oncel and Bengio, Samy and Farajtabar, Mehrdad},
  journal={arXiv preprint arXiv:2410.05229},
  year={2024}
}
```

### Groups, Tags, and Tasks

#### Groups

None

#### Tags

None

#### Tasks

* `gsm_symbolic`: Main symbolic math benchmark
* `gsm_symbolic_p1`: Perturbation level 1 (moderate difficulty increase)
* `gsm_symbolic_p2`: Perturbation level 2 (higher difficulty increase)

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
