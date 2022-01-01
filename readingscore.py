import pandas as p
import plotly.figure_factory as ff
import csv
import statistics
df=p.read_csv("data.csv")
fig=ff.create_distplot([df["reading score"].to_list()],["reading Score"])
fig.show()

reading=df["reading score"].to_list()
readingmean=statistics.mean(reading)
readingmode=statistics.mode(reading)
readingmedian=statistics.median(reading)
readingstd=statistics.stdev(reading)
print("Mean, Median and Mode of reading is {}, {} and {}".format(readingmean,readingmedian,readingmode))
print("standard deviation of reading is {}".format(readingstd))

reading1stdstart,reading1stdend=readingmean-readingstd,readingmean+readingstd
reading2stdstart,reading2stdend=readingmean-(readingstd*2),readingmean+(readingstd*2)
reading3stdstart,reading3stdend=readingmean-(readingstd*3),readingmean+(readingstd*3)

rstdp1st=[r for r in reading if r >reading1stdstart and r <reading1stdend]
rstdp2nd=[r for r in reading if r >reading2stdstart and r <reading2stdend]
rstdp3rd=[r for r in reading if r >reading3stdstart and r <reading3stdend]
print("{}% of data lies within 1st standard deviation".format(len(rstdp1st)*100.0/len(reading)))
print("{}% of data lies within 2nd standard deviation".format(len(rstdp2nd)*100.0/len(reading)))
print("{}% of data lies within 3rd standard deviation".format(len(rstdp3rd)*100.0/len(reading)))