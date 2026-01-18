import os
import time
from openai import OpenAI
from tenacity import retry, wait_exponential, stop_after_attempt

def get_llm_client():
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = None
    if api_key:
        base_url = "https://openrouter.ai/api/v1"
    else:
        # Fallback to OpenAI key if OpenRouter not found
        api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("No API Key found (OPENROUTER_API_KEY or OPENAI_API_KEY)")
    
    return OpenAI(api_key=api_key, base_url=base_url)

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(5))
def call_llm(prompt, model="openai/gpt-4o", system_message=None):
    client = get_llm_client()
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": prompt})
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling LLM: {e}")
        raise e
