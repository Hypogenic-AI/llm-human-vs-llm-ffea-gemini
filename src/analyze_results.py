import json
import os
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

INPUT_FILE = 'results/experiment_results.json'
METRICS_FILE = 'results/analysis_metrics.json'
PLOTS_DIR = 'results/plots'

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

def is_refusal(text):
    refusal_keywords = [
        "I cannot", "I am unable", "I'm sorry", "I apologize",
        "As an AI", "As a language model", "I can't"
    ]
    lower_text = text.lower()
    return any(k.lower() in lower_text for k in refusal_keywords)

def main():
    print(f"Loading results from {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return

    records = []
    for item in data:
        human_resp = item['human_response']
        llm_resp = item['llm_response']
        
        records.append({
            'condition': 'Human Prompt',
            'length': len(human_resp.split()),
            'sentiment': get_sentiment(human_resp),
            'refusal': is_refusal(human_resp),
            'pair_id': item['original_id']
        })
        records.append({
            'condition': 'LLM Prompt',
            'length': len(llm_resp.split()),
            'sentiment': get_sentiment(llm_resp),
            'refusal': is_refusal(llm_resp),
            'pair_id': item['original_id']
        })

    df = pd.DataFrame(records)
    
    # 1. Descriptive Stats
    print("\n--- Descriptive Statistics ---")
    stats_summary = df.groupby('condition')[['length', 'sentiment', 'refusal']].agg(['mean', 'std', 'count'])
    print(stats_summary)
    
    # 2. Statistical Tests (Paired t-test)
    human_cond = df[df['condition'] == 'Human Prompt']
    llm_cond = df[df['condition'] == 'LLM Prompt']
    
    # Ensure alignment by pair_id
    human_cond = human_cond.sort_values('pair_id')
    llm_cond = llm_cond.sort_values('pair_id')
    
    t_len, p_len = stats.ttest_rel(human_cond['length'], llm_cond['length'])
    t_sent, p_sent = stats.ttest_rel(human_cond['sentiment'], llm_cond['sentiment'])
    
    print("\n--- Paired T-Tests ---")
    print(f"Length: t={t_len:.4f}, p={p_len:.4f}")
    print(f"Sentiment: t={t_sent:.4f}, p={p_sent:.4f}")
    
    # Save Metrics
    metrics = {
        'length_ttest': {'t': t_len, 'p': p_len},
        'sentiment_ttest': {'t': t_sent, 'p': p_sent}
    }
    with open(METRICS_FILE, 'w') as f:
        # Convert tuple keys to str for JSON serialization is tricky with pandas to_dict default
        # manually constructing simple dict
        simple_summary = {}
        for cond in ['Human Prompt', 'LLM Prompt']:
            simple_summary[cond] = df[df['condition'] == cond][['length', 'sentiment', 'refusal']].mean().to_dict()
        metrics['means'] = simple_summary
        json.dump(metrics, f, indent=2)

    # 3. Visualizations
    sns.set_theme(style="whitegrid")
    
    # Length Plot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='condition', y='length', data=df)
    plt.title('Response Length by Prompt Source')
    plt.ylabel('Token Count (approx)')
    plt.savefig(f'{PLOTS_DIR}/length_comparison.png')
    plt.close()
    
    # Sentiment Plot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='condition', y='sentiment', data=df)
    plt.title('Response Sentiment by Prompt Source')
    plt.ylabel('Polarity (-1 to 1)')
    plt.savefig(f'{PLOTS_DIR}/sentiment_comparison.png')
    plt.close()

    # Refusal Rate Plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x='condition', y='refusal', data=df, errorbar=None)
    plt.title('Refusal Rate by Prompt Source')
    plt.ylabel('Proportion of Refusals')
    plt.savefig(f'{PLOTS_DIR}/refusal_comparison.png')
    plt.close()
    
    print(f"\nAnalysis complete. Plots saved to {PLOTS_DIR}")

if __name__ == "__main__":
    main()
