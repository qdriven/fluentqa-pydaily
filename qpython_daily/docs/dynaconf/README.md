---
url: https://github.com/rochacbruno/dynaconf.git
category: PyDaily-Lib
tag: configuration
---

# dynaconf-万能Python配置管理包

在进行自动化测试过程中,经常会修改配置，有时会有不同格式的配置比如:
1. json
2. yaml
3. toml
4. ini
5. ......

对于不同种类的格式需要做不同的处理，这些本身是一些浪费行为，一个配置文件足够用就可以，没有必要进行重复开发，
或者每一个人写法和使用方法还不一样.我总结了一下配置相关的问题可能如下:
1. 配置格式多样，造成了不知道如何配置
2. 配置格式错误，不能及时发现，只能在运行时发现
3. 一些密码写在了文件中，容易上传到github/gitlab，造成安全风险

[dynaconf](https://github.com/rochacbruno/dynaconf.git),就是为了解决这些问题来的，
有了这一个Python 库，基本上你不需要为你的配置相关的内容操心或者自己写很多代码.

dynaconf主要收到了12factor应用的启发而实现了一下功能:

1. 配置参数管理: 默认值，验证，解析，模板
2. 密码/tokens保护
3. 支持不同种类的文件格式: ```toml|yaml|json|ini|py```,同时可以自定义文件加载程序
4. 支持多个环境的不同配置文件
5. 支持用Hashicorp Vault和Redis作为配置文件存储
6. 内建支持Django/Flask
7. 支持命令行操作

## dynaconf 使用

上面把为什么要用dynaconf和dynaconf能做什么介绍完毕，以下为主要dynaconf的功能演示.

## 安装和初始化

```shell
poetry add dynaconf
```

```shell
poetry run dynaconf init -f toml
```

- settings.toml
- .secrets.toml

```shell
poetry run dynaconf -i config.settings list
```

## 配置使用

## 参考

- [12factor-config](https://12factor.net/config)
