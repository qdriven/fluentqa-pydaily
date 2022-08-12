# How to handle test failures

## Commands

```shell
pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures
```

## using pdb with pytest

```shell
pytest --pdb
pytest -x --pdb   # drop to PDB on first failure, then end test session
pytest --pdb --maxfail=3  # drop to PDB for first three failures
```