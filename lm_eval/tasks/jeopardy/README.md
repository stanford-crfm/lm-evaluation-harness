# Jeopardy

## Paper

Title: Mosaic Eval Gauntlet

Jeopardy is a benchmark for evaluating world knowledge and question answering capabilities using Jeopardy-style clues. The dataset contains questions from the TV game show Jeopardy.

Homepage: https://huggingface.co/datasets/soldni/jeopardy

### Citation

```
@misc{mosaicml2023gauntlet,
  title={Mosaic Eval Gauntlet},
  author={MosaicML},
  year={2023},
  howpublished={\url{https://github.com/mosaicml/llm-foundry/blob/main/scripts/eval/local_data/EVAL_GAUNTLET.md}}
}
```

### Groups, Tags, and Tasks

#### Groups

None

#### Tags

None

#### Tasks

* `jeopardy`: Open-ended generation task for Jeopardy-style questions
* `jeopardy_gen2mc`: Multiple choice version (converted from generation)

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
