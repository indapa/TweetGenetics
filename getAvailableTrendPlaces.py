#!/usr/bin/env python
import urllib2
import json
import string
""" get the woeid's available for Twitter trends
    https://dev.twitter.com/discussions/6942  """
def main():
    url='https://api.twitter.com/1/trends/available.json'
    avail=urllib2.urlopen(url)
    locations=json.load(avail)
    for h in locations:
        name=h['name']
        name=name.encode('utf-8')
        id=h['woeid']
        print name, id
if __name__ == "__main__":
    main()
