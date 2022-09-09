#!/bin/python

import requests
import json
import re

def get_cat():

    url =  "https://api.thecatapi.com/v1/images/search"
    response = json.loads(requests.request("GET", url).text)
    x = str(response)
    r = x.split()
    cat_pic = r[3].replace(",", "")
    cat_pic = cat_pic.replace("'","")
    print(cat_pic)
get_cat()
