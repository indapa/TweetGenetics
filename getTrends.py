#!/usr/bin/env python
import sys
import os
import string
import re
from optparse import OptionParser
import urllib2
import json

""" get trends based on woeid (default is United States) """
def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("--woeid", type="string", dest="woeid", help="woeid of location", default="2378426")

    (options, args)=parser.parse_args()
    sys.stderr.write("getting trends ...\n")
    url='http://api.twitter.com/1/trends/'+options.woeid+'.json'
    #url='http://api.twitter.com/1/trends/23424977.json'
    trends=urllib2.urlopen(url)
    trends=json.load(trends)
    print trends[0]['created_at']
    for topic in trends:
        for  t in topic['trends']:
            print t['name']
if __name__ == "__main__":
    main()
