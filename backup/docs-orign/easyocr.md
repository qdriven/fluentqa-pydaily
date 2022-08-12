# README

## EasyOCR

[EasyOCR](https://github.com/JaidedAI/EasyOCR)


## 实例代码

```shell
import easyocr

reader = easyocr.Reader(['ch_sim', 'en'])


def extract_from_img(img_path: str,**kwargs) -> str:
    return reader.readtext(img_path,kwargs)

```