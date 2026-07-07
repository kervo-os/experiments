# kervo experiments

Pre-registered experiments and the raw evidence behind
[kervo](https://github.com/kervo-os/kervo)'s claims.

Extracted from `kervo-os/kervo@f8f7a44` (2026-07-06); the original commit
history remains in the product repository.

| Experiment | Question | Result | Materials |
|---|---|---|---|
| [H4](h4/) | Do trust labels protect agents from poisoned context? | Confirmatory run **A−C = +29.2pp** (n = 24, pre-registered ≥ 20pp bar); across all 54 responses the labeled arm never lost a point to a poisoned claim | pre-registration · rubric · arm artifacts · all 54 raw responses |
| [H5](h5/) | Does the write-back flywheel close the onboarding gap at constant cost? | **Registered, awaiting the volume gate** (10 artifact-present sessions + 10 judged write-backs on the adopted repository — counted by [`h5/gate.py`](h5/gate.py), not a calendar) | pre-registration (SHA-256 anchored via OpenTimestamps at registration — `h5/*.ots` — so "the protocol predates the results" is third-party verifiable) |



Grades in H4 are agent-judged under a pre-registered rubric by
structurally blinded judges; a human-grading replication kit is included
but has not been run — the limitation is stated, not hidden.

Licensed under [Apache-2.0](LICENSE).
