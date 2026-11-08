# How to Operate — K_VLMEVAL
**Platform:** Anticloud | **IP:** USPTO pending 2026, Anticloud FZ LLE, 0-1.gg

## Module Overview
K_VLMEVAL — VLMEval: vision-language model evaluation for PAX 27B visual capabilities
Stack: Python 3.11, VLMEvalKit, PAX 27B vision head, AIOSS_FORMAT

## Daily Operations
1. `aioss verify --chain ./k_vlmeval.aioss`
2. Check service health via api-oss-monitor
3. Review api-oss-logging for error-level events
4. Confirm PAX 27B is loaded and responding

## Incident Response
- Chain tamper: halt, notify compliance, restore from backup
- GPU OOM: reduce batch size, check memory leak
- High latency >2s P99: check queue depth, scale workers
- Compliance gap: run api-oss-compliance report

## Backup (nightly)
```bash
python -m api_oss_backup backup --sources ./k_vlmeval.aioss --output ./backups/
```
