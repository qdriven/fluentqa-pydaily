from abc import ABC, abstractmethod


class SimplePlugin(ABC):
    """
    该基类每个插件都需要继承，插件需要实现基类定义的方法"""

    def __init__(self):
        self.description = '未知'

    @abstractmethod
    def perform(self, argument):
        """
        实际执行插件所执行的方法，该方法所有插件类都需要实现
        """
        raise NotImplementedError
