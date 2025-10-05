#!/usr/bin/env python

"""
First step in communications w/ the ICFP 2024 server
"""

import requests
from util import strDecode

url = "http://localhost:8000/communicate"

hdrs = {
    'Authorization': 'Bearer 00000000-0000-0000-0000-000000000000',
}

get_index = "S'%4}).$%8"
resp = requests.post(url, headers=hdrs, data=get_index)
print("raw response:")
print(resp.text)
print()
print("decoded response:")
print(strDecode(resp.txt))

# EOF

