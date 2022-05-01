# How to install and use plugins


```shell
pip install pytest-NAME
pip uninstall pytest-NAME
```


## plugin list

Here is a little annotated list for some popular plugins:

- pytest-django: write tests for django apps, using pytest integration.
- pytest-twisted: write tests for twisted apps, starting a reactor and processing deferreds from test functions.
- pytest-cov: coverage reporting, compatible with distributed testing
- pytest-xdist: to distribute tests to CPUs and remote hosts, to run in boxed mode which allows to survive segmentation faults, to run in looponfailing mode, automatically re-running failing tests on file changes.
- pytest-instafail: to report failures while the test run is happening.
- pytest-bdd: to write tests using behaviour-driven testing.
- pytest-timeout: to timeout tests based on function marks or global definitions.
- pytest-pep8: a --pep8 option to enable PEP8 compliance checking.
- pytest-flakes: check source code with pyflakes.

## Requiring/Loading plugins in a test module or conftest file

```shell
pytest_plugins = ("myapp.testsupport.myplugin",)
```

## find out which plugins are active

```shell
pytest --trace-config
```

## Deactivating / unregistering a plugin by name
