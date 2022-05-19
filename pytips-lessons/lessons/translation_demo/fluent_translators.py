#!/usr/bin/env python
# -*- coding:utf-8 -*-
from abc import ABC

proxies_example = {
    "https": "34.195.196.27:8080",
    "http": "34.195.196.27:8080"
}

from deep_translator import GoogleTranslator
from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

# langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
# # output: {arabic: ar, french: fr, english:en etc...}
# print(langs_dict) ## zh-CN/en
# using context

class ZhTranslator(ABC):
    def __init__(self):
        self.to="zh-CN"
        self.translator = GoogleTranslator(target=self.to)

    def translate_batch(self,batch_lines:[],target:str,**kwargs):
        self.translator.target=target
        return self.translator.translate_batch(batch_lines)
    def translate_file(self,file:str,target:str,**kwargs):
        self.translator.target=target
        return self.translator.translate_file(file,**kwargs)

# translated = GoogleTranslator(source='en', target='zh')\
#     .translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig
# print(translated)

# translated = GoogleTranslator(source='auto', target='de', proxies=proxies_example).translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig
# deep-translator --source "en" --target "de" --text "hello world"
