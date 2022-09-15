# fluentcli

<div align="center">

[![Build status](https://github.com/fluentcli/fluentcli/workflows/build/badge.svg?branch=master&event=push)](https://github.com/fluentcli/fluentcli/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/fluentcli.svg)](https://pypi.org/project/fluentcli/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/fluentcli/fluentcli/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/fluentcli/fluentcli/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/fluentcli/fluentcli/releases)
[![License](https://img.shields.io/github/license/fluentcli/fluentcli)](https://github.com/fluentcli/fluentcli/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Awesome `fluentcli` is a Python cli/package 

</div>

## Very first steps

### Initialize your code

1. Initialize `git` inside your repo:

```bash
cd fluentcli && git init
```

2. If you don't have `Poetry` installed run:

```bash
make poetry-download
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
make pre-commit-install
```

4. Run the codestyle:

```bash
make codestyle
```

5. Upload initial code to GitHub:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M main
git remote add origin https://github.com/fluentcli/fluentcli.git
git push -u origin main
```

