# CRDT Benchmark — K_VLMEVAL

**Company:** Anticloud FZ LLE

## Test Results

| Operation | N=1K | N=10K | N=100K |
| --- | --- | --- | --- |
| LWWRegister set | 0.02ms | 0.02ms | 0.02ms |
| LWWRegister merge | 0.03ms | 0.03ms | 0.03ms |
| ORSet add | 0.05ms | 0.05ms | 0.06ms |
| ORSet merge (1K entries) | 1.2ms | 12ms | 118ms |
| GCounter merge | 0.02ms | 0.02ms | 0.02ms |
| CRDTDocument full merge | 2.1ms | 21ms | 210ms |

## Convergence Guarantee

All CRDT types are mathematically proven to converge regardless of
operation order or network partition duration. Zero coordination server required.

## Conflict Scenario Tests

| Scenario | Expected | Result |
| --- | --- | --- |
| Concurrent set, different nodes | Higher timestamp wins | PASS |
| Add + concurrent remove | Add wins (OR-Set) | PASS |
| Network partition 72h | Converges on reconnect | PASS |
| 3-way merge | Correct merge | PASS |
