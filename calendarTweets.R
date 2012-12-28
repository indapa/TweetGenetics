library(zoo)
library(openair)
times=read.table("/Users/amit/software/TweetGenetics/times.2012.txt", colClasses='character')
names(times)=c("datestring", "timestamp", "weekday")
zoo=read.zoo(times, format="%Y-%d-%m", aggregate=length)
plos.year <- "2012"

# uncomment if you want the whole calendar year displayed
#dates <- seq(as.Date(paste(plos.year, "01","01", sep="-")), as.Date(paste(plos.year, "12","01", sep="-")), by="months")
#empty <- zoo(,dates)
#zoo <- merge(zoo, empty, all=TRUE)

alm <- as.data.frame(zoo)
alm$date=as.Date(row.names(alm))
row.names(alm)=NULL
alm=alm[,c("weekday","date")]
names(alm)=c("tweets","date")
calendarPlot(alm, pollutant='tweets', year='2012',main="@aindap Tweet frequency 2012", limits=c(0,10), cex.lim=c(1,1))