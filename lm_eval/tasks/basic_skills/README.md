# Basic Skills

## Paper

Title: OLMo 3

Abstract: https://arxiv.org/abs/2512.13961

Basic Skills is a benchmark suite for evaluating fundamental reasoning capabilities across multiple domains including arithmetic, coding, common knowledge, logical reasoning, pattern recognition, and string operations. It is used as part of the OLMo evaluation suite.

Homepage: https://huggingface.co/datasets/allenai/basic-skills

### Citation

```
@article{olmo3,
  title={OLMo 3},
  author={{Team OLMo} and Ettinger, Allyson and Bertsch, Amanda and Kuehl, Bailey and Graham, David and Heineman, David and Groeneveld, Dirk and Brahman, Faeze and others},
  journal={arXiv preprint arXiv:2512.13961},
  year={2025}
}
```

### Groups, Tags, and Tasks

#### Groups

None

#### Tags

None

#### Tasks

* `basic_skills_arithmetic`: Basic arithmetic problems
* `basic_skills_coding`: Basic programming knowledge
* `basic_skills_common_knowledge`: Common factual knowledge
* `basic_skills_logical_reasoning`: Logical reasoning problems
* `basic_skills_pattern`: Pattern recognition tasks
* `basic_skills_string_operations`: String manipulation knowledge

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
