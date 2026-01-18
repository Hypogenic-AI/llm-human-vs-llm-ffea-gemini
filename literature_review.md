# Literature Review: LLM Behavior and Prompt Source Detection

## Research Hypothesis
**Do LLMs behave differently when the prompter is human vs another LLM?**
This review investigates whether LLMs can detect distinct patterns in human vs. AI-generated prompts and if this detection could influence their response behavior (implicitly or explicitly).

## Key Papers

### 1. Contrasting Linguistic Patterns in Human and LLM-Generated News Text (Muñoz-Ortiz et al., 2023)
- **Key Finding**: There are statistically significant differences between human and LLM text across multiple dimensions.
- **Linguistics**: Humans use a richer vocabulary (higher type-token ratio) and more varied sentence structures. LLMs tend to use more "objective" markers like numbers, symbols, and auxiliary verbs.
- **Sentiment**: Human text expresses stronger negative emotions (fear, disgust) compared to the more neutral or positive bias of LLMs.
- **Syntax**: Humans optimize dependency lengths more than LLMs (shorter dependencies), although Falcon-7B showed more human-like dependency traits.
- **Relevance**: Establishes that **detectable signals exist** in the prompt itself. If an LLM's input processing is sensitive to these signals (vocabulary richness, syntax), it could theoretically "know" the source.

### 2. The Science of Detecting LLM-Generated Text (Tang et al., 2024)
- **Key Finding**: Automated systems (RoBERTa, etc.) can detect LLM-generated text with high accuracy (>98% F1) in specific domains.
- **Methodology**: Successful detectors rely on stylometric features and fine-tuned transformer representations.
- **Relevance**: Confirms that LLMs (which are transformers) have the **capacity** to distinguish these sources. If a small RoBERTa model can do it, a large GPT-4 class model certainly encodes this information.

### 3. Do LLMs write like humans? Variation in grammatical and rhetorical styles (2024)
- **Key Finding**: LLMs exhibit distinct rhetorical styles. They are often more verbose and follow a specific "assistant" register that differs from natural human casual or formal writing.
- **Relevance**: Reinforces the "stylistic gap" hypothesis.

## Common Differences (The "Signal")
Literature consistently identifies these differentiators:
1.  **Perplexity/Burstiness**: Human text is more "bursty" and has higher perplexity variance.
2.  **Lexical Diversity**: Humans use more unique words; LLMs repeat tokens more often (lower TTR).
3.  **Sentiment/Tone**: LLMs are RLHF-tuned to be helpful/harmless, leading to a "neutral/positive" and "objective" tone. Humans display a wider emotional range.
4.  **Syntactic Complexity**: Human syntax varies more; LLMs often default to standard, clean grammatical structures.

## Implications for Experimentation
If LLMs behave differently, it is likely because they implicitly classify the "register" of the prompt.
- **Human Prompt**: High perplexity, emotional, varied syntax -> Triggers "conversational" or "empathetic" mode?
- **LLM Prompt**: Low perplexity, neutral, standard syntax -> Triggers "continuation" or "informational" mode?

## Recommended Baselines & Tools
1.  **Stylometric Analysis**: Use Burrows' Delta or simple metrics (TTR, sentence length) to quantify the "distance" between prompts.
2.  **Classifiers**: Train a simple BERT/RoBERTa classifier on the HC3 dataset to serve as a proxy for the LLM's internal "discrimination" capability.
3.  **Datasets**: Use **HC3** (Human ChatGPT Comparison Corpus) for paired human/AI examples.

## Gaps
- Few papers explicitly test *downstream behavior changes* based *solely* on the prompt source (provenance) while controlling for semantic content. Most papers focus on *detection* (post-hoc) rather than *interaction* (real-time). This is the novel contribution of the proposed research.
