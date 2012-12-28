#!/usr/bin/env python
import sys
import os
import string
import re
import time
from optparse import OptionParser
import twitter
from datetime import datetime
from dateutil import tz
""" dump tweets and time stamps to  to text file """
def main():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("--user", type="string", dest="user", help="twitter userid", default="aindap")
    (options, args)=parser.parse_args()

    api = twitter.Api(consumer_key='XXXXX', consumer_secret='XXXXXX', access_token_key='XXXXXX', access_token_secret='XXXXX')

    


    if os.path.isfile('ids.txt') == True and os.path.isfile('tweets.txt'):
        #if previous file of tweets and last tweet ids, read the last tweet id
        idsfh=open('ids.txt', 'r')
        lastid=idsfh.readline().strip()
        #and get all status updates since the most recent tweet id
        statuses = api.GetUserTimeline(options.user, since_id=lastid)
        #if there are new tweets psoted
        if len( statuses ) !=0:
            newidsfh=open('ids.txt', 'w')
            os.rename('tweets.txt', 'old.tweets')
            os.rename('times.txt', 'old.times.txt')
            tweetsfh=open('tweets.txt', 'w')
            timesfh=open('times.txt', 'w')
        else:
            sys.stderr.write("no new tweets posted since last time run!\n")
            return 0
    else:

        newidsfh=open('ids.txt', 'w')
        tweetsfh=open('tweets.txt','w')
        timesfh=open('times.txt', 'w')
        statuses = api.GetUserTimeline(options.user)

    #http://farmdev.com/talks/unicode/ 
    for s in statuses:
        created=s.GetCreatedAt()
        date_struct = time.strptime(created, '%a %b %d %H:%M:%S +0000 %Y')
        datestring= time.strftime('%Y-%d-%m %H:%M:%S %A', date_struct)
        timesfh.write(datestring+"\n")
        out=s.text.encode('utf-8')
        tweetsfh.write(out+"\n")
        newidsfh.write( str(s.id) + "\n")

    if os.path.isfile('old.tweets'):
        oldfh=open('old.tweets', 'r')
        oldtimefh=open('old.times.txt', 'r')
        for line in oldfh:
            tweetsfh.write(line)
        os.remove('old.tweets')

        for line in oldtimefh:
            timesfh.write(line)
        os.remove('old.times.txt')


if __name__ == "__main__":
    main()
