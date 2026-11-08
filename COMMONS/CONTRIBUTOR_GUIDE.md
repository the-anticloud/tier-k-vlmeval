# Contributing to K_VLMEVAL

Thank you for contributing to The Anticloud ecosystem.

## Governance
K_VLMEVAL is maintained by Anticloud FZ LLE (sole shareholder: Lois-Kleinner Alpasan).
OSM/OSS governance applies — contributions are reviewed and merged by maintainers.

## How to Contribute

### Bug Reports
File issues at the project repository with:
- Reproducible test case
- Platform info (OS, Python version, GPU if applicable)
- AIOSS ledger entry hash if the bug occurs during an inference run

### Pull Requests
1. Fork the upstream repository
2. Apply the Anticloud integration patch from ANTICLOUD_PATCHES/
3. Run `bandit -r src/` and `radon cc src/` — ensure grade B or better
4. Add or update tests in tests/
5. Submit PR with DCO sign-off: `git commit -s`

### Research Contributions
If you publish results using K_VLMEVAL, cite:

```
Alpasan, L-K. (2026). The Anticloud: Sovereign AI Infrastructure Stack.
Anticloud FZ LLE. USPTO pending. https://0-1.gg/anticloud
```

## Code of Conduct
Anticloud follows the Contributor Covenant v2.1.
Harassment, discrimination, or bad-faith contributions will result in
immediate removal from the community.
