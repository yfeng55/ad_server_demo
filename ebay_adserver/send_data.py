#! /usr/bin/python

import sys
import json
import requests

# create 5 ads
url = 'http://localhost:5000/create_ad' 
args = "width=100&height=100&creative='s3://bucket/blah.png"
args = {
    'width': '100
    'height': 100
    'creative': 's3://bucket/blah.png'
}
requests.post(url, data=args)


# register impressions for all 5 ads
impression_counts = [1001, 2000, 3000, 2500, 1200]

# register clicks for all 5 ads
click_counts = [10, 4, 8, 9, 10]

if __name__ == '__main__':
    send()
