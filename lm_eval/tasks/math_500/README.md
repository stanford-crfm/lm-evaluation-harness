# MATH-500

## Dataset

`MATH-500` is a curated evaluation set of 500 competition-level mathematics
problems released by the Hugging Face open LLM leaderboard team. Each example
contains a `problem` statement paired with a step-by-step `solution`. The task in
this repository mirrors the prompt formatting used for GSM8K but scores models
with negative log-likelihood over the reference solution text.

Homepage: https://huggingface.co/datasets/HuggingFaceH4/MATH-500

## Citation

Please cite the original MATH dataset when using this benchmark:

```
@article{hendrycks2021math,
  title={Measuring Mathematical Problem Solving With the MATH Dataset},
  author={Dan Hendrycks and Collin Burns and Saurav Kadavath and Akul Arora and Steven Basart and Eric Tang and Dawn Song and Jacob Steinhardt},
  journal={NeurIPS},
  year={2021}
}
```

### Groups and Tasks

#### Groups

- `math_word_problems`

#### Tasks

- `math_500`: Computes the negative log-likelihood of the gold solution given the
  problem statement.

