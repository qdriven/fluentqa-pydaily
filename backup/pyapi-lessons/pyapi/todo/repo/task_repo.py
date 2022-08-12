#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any, Optional, List

from attr import dataclass
from injector import inject

from core.base_repo import BaseRepository
from pyapi.todo.entity.task import Task


@inject
@dataclass
class TaskRepository(BaseRepository):
    def find_by_id(self, *, entity_class=Task, entity_param=Task.id, variable: Any) -> Optional[Task]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=Task, skip=0, limit=100) -> List[Optional[Task]]:
        return super().find_all(entity_class=entity_class)
