#! /usr/bin/python

import sys
import json
import requests

if __name__ == '__main__':

    # create 5 ads
    url = 'http://localhost:5000/create_ad' 
    for i in xrange(0,5):
        args = {
            'width': str((i+1)*100),
            'height': str((i+1)*50),
            'creative': 's3://bucket/blah{num}.png'.format(num=str(i))
        }
        requests.post(url, data=args)
    
    # check that 5 ads were created
    ads = json.loads(requests.get('http://localhost:5000/show_store').content)

    # register impressions for all 5 ads
    impression_counts = [1001, 2000, 3000, 2500, 1200]
    url = 'http://localhost:5000/inc_impressions' 
    for i,ad_id in enumerate(ads.keys()):
        args = {
            'ad_id': ad_id
        }
        for j in xrange(impression_counts[i]):
            requests.post(url, data=args)

    # register clicks for all 5 ads
    click_counts = [10, 4, 8, 9, 10]
    url = 'http://localhost:5000/inc_clicks' 
    for i,ad_id in enumerate(ads.keys()):
        args = {
            'ad_id': ad_id
        }
        for j in xrange(click_counts[i]):
            requests.post(url, data=args)


