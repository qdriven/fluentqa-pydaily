#!/usr/bin/env python
# -*- coding:utf-8 -*-
from backup.pytips.lib_demo.pydantic_demo import UserModel


class TestUserModel_pydantic_usage:
    def setup(self):
        self.user = UserModel(id=12)

    def test_init_model(self):
        assert self.user.id == 12
        assert self.user.name == 'Simon'
        assert self.user.__fields_set__ == {"id"}

    def test_model_properties(self):
        result_dict = self.user.dict()
        result_json = self.user.json()
        print(result_dict, result_json)
        user1 = self.user.copy()
        assert user1 == self.user

    def test_parse_function(self):
        # UserModel.parse_obj()
        # UserModel.parse_raw()
        # UserModel.parse_file()
        # UserModel.from_orm()
        # UserModel.construct()
        # self.user.schema()
        # self.user.schema_json()
        pass
