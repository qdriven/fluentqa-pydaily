# Pytest 入门

Pytest 功能：
> Features¶
Detailed info on failing assert statements (no need to remember self.assert* names)
Auto-discovery of test modules and functions
Modular fixtures for managing small or parametrized long-lived test resources
Can run unittest (including trial) and nose test suites out of the box
Python 3.7+ or PyPy 3
Rich plugin architecture, with over 800+ external plugins and thriving community

## Get Started
### 1. 安装

- 全局安装
```shell
pip install -U pytest # 全局安装
```
- 虚拟环境安装

### 第一个pytest

- [最简单例子](../../../lessons/pytest_demos/pytest_basic/test_sample_01.py)
- run pytest:
```shell
pytest
```
- 成功的测试用例/失败的测试用例
- 多个测试文件
> pytest will run all files of the form test_*.py or *_test.py 
- pytest -q
- Conventions for Python test discovery
    * test_*.py
    * *_test.py
    * test prefixed test functions or methods outside of class
    * test prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)
    * Tests outside application code
  - Test Class for Group Tests
    * Test organization
    * Sharing fixtures for tests only in that particular class
    * Applying marks at the class level and having them implicitly apply to all tests

### pytest fixture

- show all fixture
```shell
pytest --fixture
```


