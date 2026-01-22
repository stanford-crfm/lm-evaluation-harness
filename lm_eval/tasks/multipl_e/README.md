# MultiPL-E

## Paper

Title: MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation

Abstract: https://arxiv.org/abs/2208.08227

MultiPL-E is a benchmark for evaluating code generation across multiple programming languages, translating HumanEval and MBPP problems into various languages including C++, Java, JavaScript, PHP, Rust, and Shell.

Homepage: https://nuprl.github.io/MultiPL-E/

### Citation

```
@article{cassano2022multipl,
  title={MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation},
  author={Cassano, Federico and Gouwar, John and Nguyen, Daniel and Nguyen, Sydney and Phipps-Costin, Luna and Pinckney, Donald and Yee, Ming-Ho and Zi, Yangtian and Anderson, Carolyn Jane and Feldman, Molly Q and others},
  journal={IEEE Transactions on Software Engineering},
  year={2022}
}
```

### Groups, Tags, and Tasks

#### Groups

None

#### Tags

None

#### Tasks

##### HumanEval Variants
* `multipl_e_humaneval_cpp`: HumanEval translated to C++
* `multipl_e_humaneval_java`: HumanEval translated to Java
* `multipl_e_humaneval_js`: HumanEval translated to JavaScript
* `multipl_e_humaneval_php`: HumanEval translated to PHP
* `multipl_e_humaneval_rs`: HumanEval translated to Rust
* `multipl_e_humaneval_sh`: HumanEval translated to Shell/Bash

##### MBPP Variants
* `multipl_e_mbpp_cpp`: MBPP translated to C++
* `multipl_e_mbpp_java`: MBPP translated to Java
* `multipl_e_mbpp_js`: MBPP translated to JavaScript
* `multipl_e_mbpp_php`: MBPP translated to PHP
* `multipl_e_mbpp_rs`: MBPP translated to Rust
* `multipl_e_mbpp_sh`: MBPP translated to Shell/Bash

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
