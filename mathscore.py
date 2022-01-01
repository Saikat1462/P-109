import pandas as p
import plotly.figure_factory as ff
import csv
import statistics
df=p.read_csv("data.csv")
fig=ff.create_distplot([df["math score"].to_list()],["math Score"])
fig.show()

math=df["math score"].to_list()
mathmean=statistics.mean(math)
mathmode=statistics.mode(math)
mathmedian=statistics.median(math)
mathstd=statistics.stdev(math)
print("Mean, Median and Mode of math is {}, {} and {}".format(mathmean,mathmedian,mathmode))
print("standard deviation of math is {}".format(mathstd))

math1stdstart,math1stdend=mathmean-mathstd,mathmean+mathstd
math2stdstart,math2stdend=mathmean-(mathstd*2),mathmean+(mathstd*2)
math3stdstart,math3stdend=mathmean-(mathstd*3),mathmean+(mathstd*3)

mstdp1st=[r for r in math if r >math1stdstart and r <math1stdend]
mstdp2nd=[r for r in math if r >math2stdstart and r <math2stdend]
mstdp3rd=[r for r in math if r >math3stdstart and r <math3stdend]
print("{}% of data lies within 1st standard deviation".format(len(mstdp1st)*100.0/len(math)))
print("{}% of data lies within 2nd standard deviation".format(len(mstdp2nd)*100.0/len(math)))
print("{}% of data lies within 3rd standard deviation".format(len(mstdp3rd)*100.0/len(math)))