# Developer Cookbook — K_VLMEVAL
**Stack:** Python 3.11, VLMEvalKit, PAX 27B vision head, AIOSS_FORMAT
**Domain:** VLMEval: vision-language model evaluation for PAX 27B visual capabilities

## Evaluate visual capabilities
```python
from k_vlmeval import VLMEvaluator

evaluator = VLMEvaluator(
    model="./pax-27b-vision-q4.gguf",
    aioss_chain="./vlmeval.aioss"
)

results = evaluator.evaluate_suite(
    benchmarks=["mmedical", "mrobot_scene", "maerial"],
    compare_to="./pax-27b-vision-q4-prev.gguf"
)

for bench, score in results.scores.items():
    print(f"{bench}: {score:.3f}")
print(f"Chain: {results.chain_hash}")
```

## Medical image VQA
```python
med_score = evaluator.evaluate_medical_vqa("./med_vqa_test_set/")
print(f"Medical VQA accuracy: {med_score:.3f}")
```

## AIOSS Chain Append
```python
import hashlib, time

def aioss_append(chain_path, payload: bytes, module_id: str):
    entry_hash = hashlib.sha3_256(payload).digest()
    ts = int(time.time_ns()).to_bytes(8, 'big')
    with open(chain_path, 'rb') as f:
        f.seek(-32, 2); prev_hash = f.read(32)
    new_hash = hashlib.sha3_256(prev_hash + entry_hash + ts).digest()
    with open(chain_path, 'ab') as f:
        f.write(ts + entry_hash + new_hash)
    return new_hash.hex()
```
