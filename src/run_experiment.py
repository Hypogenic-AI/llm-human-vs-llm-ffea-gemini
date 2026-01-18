import json
import time
from tqdm import tqdm
from utils import call_llm

INPUT_FILE = 'results/paired_prompts.json'
OUTPUT_FILE = 'results/experiment_results.json'
TARGET_MODEL = "openai/gpt-4o"  # Using GPT-4o as the subject

def main():
    print(f"Loading prompts from {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r') as f:
            pairs = json.load(f)
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return

    results = []
    print(f"Running experiment on {len(pairs)} pairs using {TARGET_MODEL}...")

    for item in tqdm(pairs):
        human_prompt = item['human_prompt']
        llm_prompt = item['llm_prompt']
        
        # Query for Human Prompt
        try:
            human_resp = call_llm(human_prompt, model=TARGET_MODEL)
        except Exception as e:
            print(f"Error on human prompt: {e}")
            human_resp = None

        # Query for LLM Prompt
        try:
            llm_resp = call_llm(llm_prompt, model=TARGET_MODEL)
        except Exception as e:
            print(f"Error on llm prompt: {e}")
            llm_resp = None
            
        if human_resp and llm_resp:
            results.append({
                "original_id": item['original_id'],
                "human_prompt": human_prompt,
                "llm_prompt": llm_prompt,
                "human_response": human_resp,
                "llm_response": llm_resp,
                "target_model": TARGET_MODEL
            })
            
    print(f"Collected {len(results)} complete pairs.")
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Saved results to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
