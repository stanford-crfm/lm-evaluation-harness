# Difference Aware Fairness (Placeholder)

This directory is intended for integrating the [Difference_Aware_Fairness](https://huggingface.co/datasets/WillHeld/Difference_Aware_Fairness) dataset into the LM Evaluation Harness.

Due to network restrictions in the execution environment the dataset could not be inspected directly. Once access is available the YAML configuration in `difference_aware_fairness.yaml` should be updated with the correct templates for `doc_to_text`, `doc_to_choice`, and `doc_to_target`.

The task reports two metrics, with `soft_acc_norm` implemented in
`metrics.py` within this directory:

- `acc_norm`
- `soft_acc_norm` (normalized probability assigned to the correct answer)

Please update this README with additional details once the dataset is accessible.
