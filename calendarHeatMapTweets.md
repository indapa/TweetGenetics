Calendar Heatmap of Tweet frequency
========================================================

Starting in late 2012 Twitter [allowed you to download all your tweets](https://blog.twitter.com/2012/your-twitter-archive) Earlier last week a friend of mine posted an interesting link in her [blog](http://virulentb.com/post/78604875905/science-writing-tips-from-former-nature-editors-and-obr) how to make the how to [make the most of Twitter](http://yoursocialmediaworks.com/twitter-by-the-numbers)
This reminded me that back in 2012 I was nerding out with the Twitter API and using a [calendar heatmap ](http://nextgenetics.blogspot.com/2012/09/calendar-heat-maps-and-tweet-frequency.html?spref=tw) to visualize tweeting frequency. I hadn't done much with it since, but I decided to re-visit this recreational coding project today.

First step, I requested Twitter to send me my entire Twitter archive. They give you a nice csv file from where I parsed out the date stamps of my tweets with some python code:
```python
from collections import namedtuple
import csv

tweetsfile='tweets.csv'
outfh=open('tweet.timestamps.txt', 'w')
TweetRecord = namedtuple('TweetRecord', 'tweet_id,vin_reply_to_status_id, in_reply_to_user_id, timestamp, source, text, retweeted_status_id,retweeted_status_user_id, retweeted_status_timestamp, expanded_urls')

for tweet in map(TweetRecord._make, csv.reader(open(tweetsfile, "rb"))):
    outfh.write( tweet.timestamp + "\n")
```

Next, I used the below R code to read in the dates and calculate the tweet counts:

When you click the **Knit HTML** button a web page will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:


```
## Loading required package: zoo
## 
## Attaching package: 'zoo'
## 
## The following objects are masked from 'package:base':
## 
##     as.Date, as.Date.numeric
## 
## Loading required package: openair
```


This is all inspired from this post from Martin Fenner on [visualzing tweets linking to a paper](http://blogs.plos.org/mfenner/2012/07/14/visualizing-tweets-linking-to-a-paper/). It uses the [zoo](http://cran.r-project.org/web/packages/zoo/index.html) and [openair](http://cran.r-project.org/web/packages/openair/index.html) packages. Here are my calendar heatmaps from 2008-2014. I created a Twitter account in late November 2008. From Dec-08 through Feb-09 I kind of forgot about it. Then starting in March-09 I fully committed to the medium and haven't looked back. There are definite time windows where my tweet frequency heats up. I'll have to look back into my archive and see what I was tweeting about. Overall patterns though, I would say my tweet frequency is generally 4 times a day or less. I'll dive more into this dataset in later post ...



```r
calendarPlot(alm, pollutant = "tweets", year = "2008", main = "@aindap Tweet frequency 2008", 
    limits = c(0, 10), cex.lim = c(1, 1))
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-21.png) 

```r

calendarPlot(alm, pollutant = "tweets", year = "2009", main = "@aindap Tweet frequency 2009", 
    limits = c(0, 10), cex.lim = c(1, 1))
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-22.png) 

```r

calendarPlot(alm, pollutant = "tweets", year = "2010", main = "@aindap Tweet frequency 2010", 
    limits = c(0, 10), cex.lim = c(1, 1))
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-23.png) 

```r

calendarPlot(alm, pollutant = "tweets", year = "2011", main = "@aindap Tweet frequency 2011", 
    limits = c(0, 10), cex.lim = c(1, 1))
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-24.png) 

```r

calendarPlot(alm, pollutant = "tweets", year = "2012", main = "@aindap Tweet frequency 2012", 
    limits = c(0, 10), cex.lim = c(1, 1))
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-25.png) 

```r

calendarPlot(alm, pollutant = "tweets", year = "2013", main = "@aindap Tweet frequency 2013", 
    limits = c(0, 10), cex.lim = c(1, 1))
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-26.png) 

```r

calendarPlot(alm, pollutant = "tweets", year = "2014", main = "@aindap Tweet frequency 2014", 
    limits = c(0, 10), cex.lim = c(1, 1))
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-27.png) 

```r

```


