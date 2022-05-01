#!/usr/bin/env python
# -*- coding:utf-8 -*-


CONTENT = "content"


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    assert 0

def test_histogram(image_file):
    print(image_file)
        # compute and test histogram