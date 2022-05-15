# How to Invoke Pytest

## 运行在模块中的测试 run test in module

```shell
pytest test_mod.py
```

## 运行在目录中的测试 run test in directory

```shell
pytest test_folder/
```

## 运行指定的测试方法 run tests by keyword expression

```shell
pytest -K "MyClass and not method"
```

## 通过节点id运行测试集合 run tests by node ids

```shell
 pytest pytest_basic/test_in_class.py::TestDemoForTestInClass::test_two
```

## 根据标记运行测试 run tests by mark

```shell
pytest -m slow
```

如何设置mark呢？使用pytest.ini文件设置或者使用pyproject.toml设置

### 运行package里面的测试 run tsts from packages

```shell
pytest --pyargs pkg.testing
```

### 获取版本/配置参数/环境变量名称

- pytest --version
- pytest --fixtures
- pytest -h | --help

## Profiling test execution duration

```shell
pytest --durations=10 --durations-min=1.0
```

To get a list of the slowest 10 test durations over 1.0s long:


## loading plugin

```shell
pytest -p myplugin_module
pytest -p pytest_cov

```

disable plugin:

```shell
pytest -p no:doctest
```

### 调用pytest的其他方式

```shell
python -m pytest [options]
```