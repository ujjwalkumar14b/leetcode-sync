class Codec:
    def __init__(self):
        self.urls = []

    def encode(self, longUrl: str) -> str:
        self.urls.append(longUrl)
        return "http://tinyurl.com/" + str(len(self.urls) - 1)

    def decode(self, shortUrl: str) -> str:
        idx = int(shortUrl.split('/')[-1])
        return self.urls[idx]
