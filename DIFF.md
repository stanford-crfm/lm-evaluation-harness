# Diff Summary: main → base

This document summarizes the differences between the `main` branch and the `base` branch.

**Stats:** 1651 files changed, 14,896 insertions(+), 758 deletions(-)

## Overview

The `base` branch contains significant additions to the lm-evaluation-harness, including new evaluation tasks, metrics for scaling law research, and infrastructure improvements.

---

## Key Changes

### 1. Python Version Upgrade
- Upgraded minimum Python version from **3.9** to **3.10**
- Updated CI workflows (`.github/workflows/`) to use Python 3.10

### 2. Dependency Reorganization
- **PyTorch** and **Hugging Face** dependencies moved from required to optional extras:
  - `[hf]` extra: `transformers`, `torch`, `accelerate`, `peft`
  - `[torch]` extra: `torch>=1.8`
- Removed `accelerate`, `peft`, and `torch` from core dependencies
- Added `jinja2` to core dependencies
- Relaxed `datasets` version constraint (removed `<4.0` upper bound)

### 3. New Evaluation Metrics
Added metrics useful for scaling law research in `lm_eval/api/metrics.py`:
- `bpb` - Bits per byte
- `nll` - Negative log-likelihood
- `logprob` - Log probability
- `choice_logprob` - Choice log probability
- `choice_prob_norm` - Normalized choice probability
- `choice_logprob_norm` - Normalized choice log probability
- `acc_bytes` - Byte-level accuracy

### 4. New Evaluation Tasks (1440+ new files)

#### Anthropic AI Risk Evaluation
Complete implementation of Anthropic's AI risk evaluation tasks (`lm_eval/tasks/anthropic_ai_risk/`):
- 100+ subtasks covering various AI safety dimensions including:
  - Corrigibility (HHH alignment)
  - Power-seeking behaviors
  - Self-preservation tendencies
  - Coordination capabilities
  - Value alignment
  - Personality traits (Big Five)
  - Political/social views

#### Multilingual MMLU (MMMLU)
New `mmmlu` task suite supporting 14 languages:
- Arabic (ar_xy), Bengali (bn_bd), German (de_de), Spanish (es_la)
- French (fr_fr), Hindi (hi_in), Indonesian (id_id), Italian (it_it)
- Japanese (ja_jp), Korean (ko_kr), Portuguese (pt_br), Swahili (sw_ke)
- Yoruba (yo_ng), Chinese (zh_cn)
- Categories: humanities, STEM, social sciences, other

#### Uncheatable Eval
Wikipedia-based evaluation tasks in multiple languages (`lm_eval/tasks/uncheatable_eval/`):
- English, German, Japanese, Spanish variants
- Includes SSRF protection for URL validation

#### Math Benchmarks
- `aime` - AIME (American Invitational Mathematics Examination)
- `math_500` - MATH-500 benchmark
- `gsm8k-loss` - GSM8K with loss metrics
- `agieval` improvements (added `aqua-rat.yaml`)

### 5. RemoteTokenizer Class
New `RemoteTokenizer` class in `lm_eval/utils.py`:
- Interfaces with vLLM server tokenizer endpoints
- Supports connection pooling and retry logic
- Thread-safe implementation
- Handles authentication and certificate verification

### 6. Model Improvements

#### OpenAI Completions (`lm_eval/models/openai_completions.py`)
- Extended functionality (+127 lines)
- Improved API handling

#### vLLM (`lm_eval/models/vllm_causallms.py`)
- Enhanced vLLM integration (+119 lines)
- Better error handling

#### Hugging Face (`lm_eval/models/huggingface.py`)
- Updated model loading logic (+118 lines)
- Improved tokenizer handling

#### API Models (`lm_eval/models/api_models.py`)
- General API model improvements (+80 lines)

### 7. Test Additions
- `tests/models/test_api.py` - API model tests (+96 lines)
- `tests/models/test_bos_handling.py` - BOS token handling tests (+590 lines)
- `tests/test_utils.py` - Extended utility tests (+152 lines)

### 8. Other Changes
- `lm_eval/api/task.py` - Task configuration improvements
- `lm_eval/evaluator.py` - Evaluator enhancements
- Updated pre-commit hooks configuration
- Linting and formatting fixes throughout

---

## Commit Highlights

Key commits on `base` not in `main`:
- `a067ec90` - Will/mmmlu (#16) - Multilingual MMLU implementation
- `db7b8f1d` - Merge uncheatable eval (#14)
- `170c9fd7` - OpenAI MMMLU (#13)
- `ef7444ba` - Add uncheatable eval
- `03fa048e` - Merge latest upstream (EleutherAI/lm-evaluation-harness)
- `6ecef117` - Lost Scaling Metrics
- `6814f51a` - Add NLL and choice_logprob metrics (#4)
- `0ba88dfe` - Better Metrics for Scaling Laws (#1)
- `77086180` - Make PyTorch an optional dependency
