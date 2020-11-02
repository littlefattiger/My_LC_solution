#https://leetcode.com/problems/encode-and-decode-tinyurl/
#very simple, just use its lacation to do encoding
class Codec:
    def __init__(self):
        self.url = []
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.url.append(longUrl)
        return "http://tinyurl.com/" + str(len(self.url  ) - 1)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.url[int(shortUrl.split('/')[-1])]
