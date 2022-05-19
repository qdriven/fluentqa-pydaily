#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import annotations

from typing import List

from pydantic import BaseModel

# $ datamodel-codegen  --input pets.json --input-file-type json --output model.py

json_model = {
    "phaseId": "ebbaad8c-c1b6-4c2e-853f-4e7c9dfa22b0",
    "productId": "128c37f2-cb42-49f4-baa7-d8169a3c7e26",
    "descriptor": {
        "id": "",
        "elementId": "aad19c26-b5ff-4ad6-b2f9-596b04052541",
        "elementName": "12343",
        "elementValue": {
            "unitId": "3a662e5a-c09f-463f-bf37-07e53ed3dcac",
            "unitName": "个",
            "unitGroupName": "个",
            "elements": [
                {
                    "unitId": "3a662e5a-c09f-463f-bf37-07e53ed3dcac",
                    "unitName": "个",
                    "unitGroupName": "个",
                    "elements": "",
                    "factor": "1"
                }
            ],
            "factor": "1"
        },
        "instanceId": "",
        "instanceName": "",
        "instanceType": "",
        "intermediateId": "",
        "intermediateName": "",
        "factorOrigin": "",
        "phaseId": "ebbaad8c-c1b6-4c2e-853f-4e7c9dfa22b0",
        "phaseName": ""
    }
}


class Element(BaseModel):
    unitId: str
    unitName: str
    unitGroupName: str
    elements: str
    factor: str


class ElementValue(BaseModel):
    unitId: str
    unitName: str
    unitGroupName: str
    elements: List[Element]
    factor: str


class Descriptor(BaseModel):
    id: str
    elementId: str
    elementName: str
    elementValue: ElementValue
    instanceId: str
    instanceName: str
    instanceType: str
    intermediateId: str
    intermediateName: str
    factorOrigin: str
    phaseId: str
    phaseName: str


class ProductModel(BaseModel):
    phaseId: str
    productId: str
    descriptor: Descriptor


m = ProductModel.parse_obj(json_model)
print(m)
#
# with TemporaryDirectory() as temporary_directory_name:
#     temporary_directory = Path(temporary_directory_name)
#     output = Path(temporary_directory / 'model.py')
#     datamodel_code_generator.generate(
#         json_str,
#         input_file_type=datamodel_code_generator.InputFileType.JsonSchema,
#         input_filename="./field.json",
#         output=output,
#     )
#     model: str = output.read_text()
# print(model)
