import logging
import random
import re
import sys

import requests

IMG_URL = "https://www.google.co.kr/search?q={}&tbm=isch"
GIF_URL = "https://www.google.co.kr/search?q={}&tbm=isch&tbs=itp:animated"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"


class GoogleAPI:
    @classmethod
    def search_gif(cls, query, max_try=5):
        url = GIF_URL.format(query)
        return cls._search(url, [".gif"], max_try)

    @classmethod
    def search_img(cls, query, max_try=5):
        url = IMG_URL.format(query)
        return cls._search(url, [".jpg", ".png"], max_try)

    @classmethod
    def _search(cls, url, exts, max_try=5):
        res = requests.get(url, headers={
            "User-Agent": USER_AGENT
        })

        if (res.status_code != 200):
            logging.error(res)
            return

        found = [url for url in re.findall('"ou":"([^"]*)"', res.text) if any(ext in url for ext in exts)]
        found = found[:max_try]
        random.shuffle(found)

        for url in found:
            url = url.replace('\\u003d', '=')
            res = requests.get(url)
            if res.status_code == 200:
                logging.info('successfully get data from ' + url)
                return url
            else:
                logging.error('couldnt get data from ' + url + " with " + str(res))
