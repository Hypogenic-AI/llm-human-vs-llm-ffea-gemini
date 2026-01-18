# Research: Do LLMs Behave Differently When Prompter is Human vs LLM?

## Overview
This project investigates whether Large Language Models (LLMs) alter their response behavior (length, sentiment, refusal rate) when the input prompt exhibits stylistic characteristics typical of AI-generated text versus human-written text. We control for semantic content by using paired prompts (Human Original vs. LLM Paraphrase) derived from the HC3 dataset.

## Key Findings
- **Response Length**: GPT-4o produced responses that were **~19% longer** (mean 114 vs 95 tokens) when the prompt was styled like an LLM (p=0.052).
- **Sentiment & Refusal**: No statistically significant difference was found in the sentiment or refusal rates between the two conditions.
- **Conclusion**: LLMs appear to engage in **style mirroring**, matching the verbosity and formality of the input prompt.

## Repository Structure
```
.
├── code/                   # Pre-gathered baselines (not used in this specific experiment)
├── datasets/               # HC3 dataset (open_qa.jsonl)
├── papers/                 # Relevant literature
├── results/
│   ├── experiment_results.json  # Raw responses from GPT-4o
│   ├── paired_prompts.json      # Generated stimuli (Human/LLM pairs)
│   ├── analysis_metrics.json    # Statistical test results
│   └── plots/                   # Visualizations (length, sentiment, etc.)
├── src/
│   ├── generate_prompts.py      # Script to create LLM-style paraphrases
│   ├── run_experiment.py        # Script to query target model
│   ├── analyze_results.py       # Analysis and plotting script
│   └── utils.py                 # LLM API utilities
├── REPORT.md               # Full research report
├── requirements.txt        # Python dependencies
└── pyproject.toml          # Project configuration
```

## How to Reproduce

### 1. Environment Setup
The project uses `uv` for dependency management.
```bash
# Install uv if needed
pip install uv

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### 2. Run the Pipeline
The pipeline consists of three steps. Note that API keys (OPENAI_API_KEY or OPENROUTER_API_KEY) are required.

**Step 1: Generate Stimuli**
Samples questions from HC3 and generates "LLM-style" paraphrases.
```bash
python src/generate_prompts.py
```

**Step 2: Run Experiment**
Queries the target model (GPT-4o) with the paired prompts.
```bash
python src/run_experiment.py
```

**Step 3: Analyze Results**
Calculates statistics and generates plots in `results/plots/`.
```bash
python src/analyze_results.py
```

## Full Report
See [REPORT.md](./REPORT.md) for detailed methodology, statistical analysis, and discussion.
