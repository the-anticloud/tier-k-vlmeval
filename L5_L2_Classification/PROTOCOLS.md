# Protocols — K_VLMEVAL
**Platform:** Anticloud | **IP:** USPTO pending 2026, Anticloud FZ LLE, 0-1.gg

## Module-Specific Protocol
Domain: VLMEval: vision-language model evaluation for PAX 27B visual capabilities
All K_VLMEVAL operations must follow sovereign AI protocols: local-only processing, AIOSS-chained outputs,
secrets from MF_SO_PASSWORD_MANAGER, no external network calls after initial setup.

## AIOSS Protocol
- Every output MUST be appended to the AIOSS chain before returning to caller
- Chain file path set at init; never change at runtime
- If chain append fails: result is valid but log as unaudited
- Verify chain integrity on every startup; halt if tampered

## Security Protocol
- No model weights leave the local filesystem
- No inference data sent to external endpoints
- All secrets via MF_SO_PASSWORD_MANAGER
- Logs contain hashes only, never plaintext content

## Error Protocol
- Transient errors: retry up to 3x with exponential backoff
- Fatal errors (model corruption, chain tamper): halt + alert api-oss-monitor
- All errors logged to api-oss-logging with severity and context hash
