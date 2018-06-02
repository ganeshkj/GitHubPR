#!/usr/bin/python
from urllib.parse import urlencode

import validators
import requests


def httpget(url, timeout=30,params={},headers={}):
    if validators.url:
        try:
            if len(params) == 0:
                httpresp = requests.get(url,timeout=timeout,headers=headers)
            else:
                httpresp = requests.get(url,timeout=timeout,headers=headers,params=urlencode(params))

            return httpresp

        except requests.exceptions.HTTPError as err:
            print(format(err)+"\n HTTP Error from server with URL:"+format(url))
    else:
        print("Malformed URL")
        return "URL_ERROR"
