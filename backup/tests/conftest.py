#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

import pytest

sys.dont_write_bytecode = True


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, set) \
            and isinstance(right, set) and op == "==":
        return [
            "Comparing object instances:",
            "   vals: {} != {}".format(left, right),
        ]


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    # img = compute_expensive_image()
    fn = tmp_path_factory.mktemp("data") / "mimtweb-startup.png"
    # img.save(fn)
    return fn


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))

    # pytest - q - -stringinput = "hello" - -stringinput = "world"
    # test_strings.py
#
# import pytest
# from fastapi import FastAPI
# from fastapi.testclient import TestClient
#
#
#
# @pytest.fixture
# def app() -> FastAPI:
#     application.dependency_overrides = {}
#
#     return application
#
#
# @pytest.fixture
# def client(app) -> TestClient:
#     return TestClient(app)
