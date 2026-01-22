# BigCodeBench

## Paper

Title: BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions

Abstract: https://arxiv.org/abs/2406.15877

BigCodeBench is a benchmark for evaluating code generation capabilities on complex, practical programming tasks. It tests models on their ability to use diverse library function calls and follow complex instructions.

Homepage: https://github.com/bigcode-project/bigcodebench

### Citation

```
@article{zhuo2024bigcodebench,
  title={BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions},
  author={Zhuo, Terry Yue and Vu, Minh Chien and Chim, Jenny and Hu, Han and Yu, Wenhao and Widyasari, Ratnadira and Yusuf, Imam Nur Bani and Zber, Haolan and He, Junda and Flandrin, Vincent and others},
  journal={arXiv preprint arXiv:2406.15877},
  year={2024}
}
```

### Groups, Tags, and Tasks

#### Groups

None

#### Tags

None

#### Tasks

* `bigcodebench`: Standard BigCodeBench benchmark
* `bigcodebench_hard`: Harder subset of BigCodeBench problems

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
