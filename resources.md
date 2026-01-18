# Resources Catalog

## Summary
This catalog lists all resources gathered for the project "Do LLMs behave differently when the prompter is human vs another LLM?".

## Papers
Located in `papers/`.

1.  **Contrasting Linguistic Patterns in Human and LLM-Generated News Text** (2023) - `papers/2023_Contrasting_Linguistic_Patterns.pdf`
2.  **The Science of Detecting LLM-Generated Text** (2023) - `papers/2023_Science_of_Detecting_LLM_Text.pdf`
3.  **Do LLMs write like humans?** (2024) - `papers/2024_Do_LLMs_Write_Like_Humans.pdf`
4.  **Large Language Models Are Human-Level Prompt Engineers** (2022) - `papers/2022_LLMs_Human_Level_Prompt_Engineers.pdf`
5.  **EvoPrompt** (2023) - `papers/2023_EvoPrompt.pdf`
6.  **Comparing LLM-generated and human-authored news text** (2025) - `papers/2025_Comparing_LLM_Human_News.pdf`

## Datasets
Located in `datasets/`.

| Name | Source | Format | Size | Notes |
|------|--------|--------|------|-------|
| **HC3** | HuggingFace | JSONL | ~5MB (samples) | Human vs ChatGPT answers. Contains `open_qa` and `wiki_csai`. |

**Note**: Dataset files are excluded from git. See `datasets/README.md` for download instructions.

## Code Repositories
Located in `code/`.

| Name | Purpose | Location |
|------|---------|----------|
| **chatgpt-comparison-detection** | HC3 Baseline & Detection | `code/chatgpt-comparison-detection/` |
| **M4** | Multi-generator detection | `code/M4/` |

## Recommendations for Experiment Design

1.  **Hypothesis Testing**:
    - Use the **HC3** dataset to get paired questions/prompts (Human vs AI).
    - Feed these prompts to a target LLM (e.g., GPT-3.5/4 or Llama 2).
    - Measure differences in the *response*:
        - Length
        - Sentiment
        - Refusal rate (does it refuse AI prompts more?)
        - Stylometric features (TTR, perplexity)

2.  **Control**:
    - Ideally, paraphrase the Human prompt to be "AI-like" and the AI prompt to be "Human-like" using a style transfer model (or another LLM) to verify if the *style* is the causal factor, not the content.

3.  **Metrics**:
    - Use the code in `code/chatgpt-comparison-detection` to calculate stylistic metrics.
