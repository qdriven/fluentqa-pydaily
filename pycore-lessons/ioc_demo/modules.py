#!/usr/bin/env python
# -*- coding:utf-8 -*-
from dataclasses import dataclass
from pydantic import BaseModel
from injector import inject


class RepoClass:
    def __init__(self):
        self.repo = "repo"


@inject
@dataclass
class ServiceDataClassDemo:
    repo: RepoClass

    def serve_you(self):
        print("can I help you! {}-2", self.repo.repo)


@inject
# @dataclass
class ServiceClass(BaseModel):
    repo: RepoClass

    # @inject
    # def __init__(self, repo: RepoClass):
    #     self.repo = repo

    def serve_you(self):
        print("can I help you! {}", self.repo.repo)
