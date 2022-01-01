import pandas as p
import plotly.figure_factory as ff
import csv
import statistics
df=p.read_csv("data.csv")
fig=ff.create_distplot([df["writing score"].to_list()],["writing Score"])
fig.show()

writing=df["writing score"].to_list()
writingmean=statistics.mean(writing)
writingmode=statistics.mode(writing)
writingmedian=statistics.median(writing)
writingstd=statistics.stdev(writing)
print("Mean, Median and Mode of writing is {}, {} and {}".format(writingmean,writingmedian,writingmode))
print("standard deviation of writing is {}".format(writingstd))

writing1stdstart,writing1stdend=writingmean-writingstd,writingmean+writingstd
writing2stdstart,writing2stdend=writingmean-(writingstd*2),writingmean+(writingstd*2)
writing3stdstart,writing3stdend=writingmean-(writingstd*3),writingmean+(writingstd*3)

mstdp1st=[r for r in writing if r >writing1stdstart and r <writing1stdend]
mstdp2nd=[r for r in writing if r >writing2stdstart and r <writing2stdend]
mstdp3rd=[r for r in writing if r >writing3stdstart and r <writing3stdend]
print("{}% of data lies within 1st standard deviation".format(len(mstdp1st)*100.0/len(writing)))
print("{}% of data lies within 2nd standard deviation".format(len(mstdp2nd)*100.0/len(writing)))
print("{}% of data lies within 3rd standard deviation".format(len(mstdp3rd)*100.0/len(writing)))