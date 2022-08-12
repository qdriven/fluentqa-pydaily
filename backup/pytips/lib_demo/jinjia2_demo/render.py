#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json

from jinja2 import Template


def render_template(temp_str, context={}):
    template = Template(temp_str)
    return template.render(context)


def render_to_dict(dict_or_json, context={}):
    template = Template(json.dumps(dict_or_json))
    filled_str = template.render(context)
    return json.loads(filled_str, encoding='utf-8')


if __name__ == '__main__':
    json_str = """
    {
    "location": {
        "id": "123454",
        "name": "{{ range(1, 1000) | random }}-location-error",
        "address": "",
        "cityCode": "110100000000",
        "cityName": "",
        "employeeNum": "-100"
    }
}
    """
    result = render_template(json_str)
    print(result)
