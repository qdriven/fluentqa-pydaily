#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pyapi.todo.repo.task_repo import TaskRepository
from pyapi.todo.service.task_service import TaskService
from core.contexts import injector

task_repository = injector.get(TaskRepository)
task_service = injector.get(TaskService)
