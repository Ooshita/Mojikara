# -*- coding: UTF=8 -*-
from urllib import request
from urllib.parse import urljoin, urlencode

class Search:
    def __init__(self):
        self.word = ""
    
    def execute(self, word):
        with open("/Users/noriakioshita/.config/googleCustomSearch/.customsearchApikey.dat", "r", encoding="utf-8") as f:
            api_key = f.read()
        with open("/Users/noriakioshita/.config/googleCustomSearch/.searchEngineId.dat", "r", encoding="utf-8") as f:
            engine_id = f.read()

        self.word = word
        url = 'https://www.googleapis.com/customsearch/v1?'
        params = {
            'key' : api_key,
            'cx' : engine_id,
            'searchType' : 'image',
            'q' : word
        }
        url = url + urlencode(params)
        with request.urlopen(url) as res:
            html = res.read().decode("utf-8")
        return html

   

