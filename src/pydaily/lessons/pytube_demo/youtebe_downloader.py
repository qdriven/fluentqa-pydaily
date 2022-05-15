from dataclasses import dataclass

from pytube import YouTube


@dataclass
class YTDownloadAttribute:
    url: str
    title: str
    thumbnail_url: str
    saved_url: str
    captions: dict
    file_url: str


def download(url, **kwargs):
    yt = YouTube(url)
    for k, v in kwargs:
        print(k, v)
    print(yt.title)
    print(yt.thumbnail_url)
    print(yt.captions)
    for caption in yt.captions:
        print(caption)
    print(yt.streams)
