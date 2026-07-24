# Runs

Persistent state for FoundryOS state-machine-backed runs, per [`../runtime/state-machine/ENGINE_SPEC.md`](../runtime/state-machine/ENGINE_SPEC.md). Each subdirectory is one run: `run-state.md` (current state, overwritten in place), `state-history.md` (append-only transition log), `approvals.md` (append-only human approval records).

This directory did not exist before Phase 2 of the FoundryOS Evolution initiative — it is the repository's first persistent run-state mechanism, per `docs/architecture/adr/ADR-005-run-state-persistent-and-resumable.md`.

- `demo-0001/` — the Phase 2 test-harness demo run, proving the generic state-machine engine (valid/invalid transitions, pause, resume, human approval, completion) before any concrete product workflow is built on top of it. Kept as a permanent reference example — do not delete.

Real runs (Idea Discovery and beyond, starting Phase 3) will be created here following the same layout, governed by their own state registries rather than the generic one `demo-0001` uses.
