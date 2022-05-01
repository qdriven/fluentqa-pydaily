from lessons.pytube_demo.youtebe_downloader import download


class TestPytubeDemo:
    def test_download(self):
        url = "https://www.youtube.com/watch?v=WlQdLLOmW3o"
        download(url)
