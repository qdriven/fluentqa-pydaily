# Python Magic Method

| 魔术方法                        | 调用方式                          | 解释  |
|:--------------------------------|:----------------------------------|:------|
|**__new__(cls [,...])**          |instance = MyClass(arg1, arg2)     |创建实例
|**__init__(self [,...])**        |instance = MyClass(arg1, arg2)     |创建实例
|**__cmp__(self, other)**         |self == other, self > other, ....  |比较
|__pos__(self)                    |+self                              |一元加运算符
|__neg__(self)                    |-self                              |一元减运算符
|__invert__(self)                 |~self                              |取反运算符
|__index__(self)                  |x[self]                            |对象被作为索引使用
|**__nonzero__(self)**            |bool(self)                         |对象的布尔值
|__getattr__(self, name)          |self.name # name不存在             |访问一个不存在的属性
|__setattr__(self, name, val)     |self.name = val                    |对一个属性赋值
|__delattr__(self, name)          |del self.name                      |删除一个属性
|__getattribute(self, name)       |self.name                          |访问任何属性
|__len__(self)                    |len(self)                          |返回当前对象长度
|**__getitem__(self, key)**       |self[key]                          |使用索引访问元素
|**__setitem__(self, key, val)**  |self[key] = val                    |对某个索引值赋值
|__delitem__(self, key)           |del self[key]                      |删除某个索引值
|**__iter__(self)**               |for x in self                      |迭代
|**__contains__(self, value)**    |value in self, value not in self   |使用in操作测试关系时
|**__concat__(self, value)**      |self + other                       |连接两个对象时
|__call__(self [,...])            |self(args)                         |调用对象
|**__enter__(self)**              |with self as x:                    |with声明上下文管理
|__exit__(self, exc, val, trace)  |with self as x:                    |with声明上下文管理
|__getstate__(self)               |pickle.dump(pkl_file, self)        |序列化
|__setstate__(self)               |data = pickle.load(pkl_file)       |序列化


__cmp__被取消，因为和其他魔法方法有功能上的重复。

__nonzero__被重命名成__bool__。