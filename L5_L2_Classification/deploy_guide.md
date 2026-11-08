# Deploy Guide — K_VLMEVAL
**Tier:** TIER_6_SECURITY_EVAL | **Stack:** Python 3.11, VLMEvalKit, PAX 27B vision head, AIOSS_FORMAT
**Air-gap capable after initial setup.**

## Prerequisites
Python 3.11+, VLMEvalKit 0.x, PAX 27B with vision head, T4 GPU.

## Environment
T4 GPU. VLMEvalKit benchmark datasets (download separately). 16GB RAM.

## AIOSS Integration
```bash
aioss init --module K_VLMEVAL --output ./k_vlmeval.aioss
aioss append --chain ./k_vlmeval.aioss --payload ./output.bin --module K_VLMEVAL
aioss verify --chain ./k_vlmeval.aioss
```

## Air-Gap Setup
```bash
pip download -r requirements.txt -d ./wheels/
pip install --no-index --find-links ./wheels/ -r requirements.txt
```

## PAX 27B Harness Wiring
```python
from anticloud_pax import PAXHarness
harness = PAXHarness(
    model_path="./pax-27b-q4.gguf",
    module="K_VLMEVAL",
    aioss_chain="./K_VLMEVAL.aioss",
    classification="L5_NARROW_L2_GENERAL"
)
result = harness.process(input_data)
```

## Verification
```bash
aioss verify --chain ./K_VLMEVAL.aioss --verbose
python -m K_VLMEVAL.tests.smoke
```
