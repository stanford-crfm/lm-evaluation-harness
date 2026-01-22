# LBPP (Less Basic Python Problems)

## Paper

Title: On Leakage of Code Generation Evaluation Datasets

Abstract: https://arxiv.org/abs/2407.07565

LBPP (Less Basic Python Problems) is a benchmark for evaluating Python code generation capabilities, designed to be uncontaminated and share no inspiration with existing training and evaluation datasets. It presents 161 prompts with associated solutions, offering a novel generalization challenge for LLMs.

Homepage: https://huggingface.co/datasets/CohereLabs/lbpp

### Citation

```
@inproceedings{matton2024leakage,
  title={On Leakage of Code Generation Evaluation Datasets},
  author={Matton, Alexandre and Sherborne, Tom and Aumiller, Dennis and Tommasone, Elena and Alizadeh, Milad and He, Jingyi and Ma, Raymond and Voisin, Maxime and Gilsenan-McMahon, Ellen and Gall{\'e}, Matthias},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2024},
  year={2024}
}
```

### Groups, Tags, and Tasks

#### Groups

None

#### Tags

None

#### Tasks

* `lbpp`: Less Basic Python Problems with execution-based evaluation

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
