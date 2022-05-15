# How to capture stdout/stderr output

```shell
pytest -s                  # disable all capturing
pytest --capture=sys       # replace sys.stdout/stderr with in-mem files
pytest --capture=fd        # also point filedescriptors 1 and 2 to temp file
pytest --capture=tee-sys   # combines 'sys' and '-s', capturing sys.stdout/stderr
                           # and passing it along to the actual sys.stdout/stderr
```