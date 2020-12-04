import json
import requests
from requests.exceptions import RequestException
import re
import time

url='https://shanchengzhiyuanzhe.lingxi360.com/Form/detail/LXEB9tpAfa7KWcc6'
def get_one_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            print( response.text)
        return None
    except RequestException:
        return requests.exceptions


get_one_page(url)