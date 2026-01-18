import json
import os

file_path = 'datasets/HC3/open_qa.jsonl'
print(f"Checking {file_path}...")

data = []
with open(file_path, 'r') as f:
    for i, line in enumerate(f):
        if i < 3:
            print(f"Item {i}: {line.strip()[:200]}...") # Print first 200 chars
        data.append(json.loads(line))

print(f"Total items: {len(data)}")
