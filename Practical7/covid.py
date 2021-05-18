import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Change working directory
os.chdir("D:\IBI1\IBI1_2020-21\Practical7")
#importing the .csv file
covid_data = pd.read_csv("full_data.csv")
#showing all columns, and every second row between (and including) 0 and 10
print(covid_data.iloc[0:11:2,0:5])
#used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
t1 = []
for i in range(covid_data.shape[0]):
    if covid_data.loc[i,"location"] == "Afghanistan":
        t1.append(True)
    else:
        t1.append(False)
print(covid_data.loc[t1,"total_cases"])
# the mean and median of new cases for the entire world
print("Mean:",np.mean(covid_data.iloc[t1,2]))    
print("Median:",np.median(covid_data.iloc[t1,2]))
#Set up the canvas
plt.figure(figsize=(6,6), dpi=120)
plt.figure(1)
#boxplot of new cases worldwide.
ax1 = plt.subplot(311)
plt.boxplot(
    covid_data.loc[:,"new_cases"],
    vert = True,
    whis = 1.5,
    patch_artist = True,
    meanline = True,
    showmeans=True,
    meanprops={'color':'red'},
    medianprops={'color':'blue'},
    showbox = True,
    showcaps = True,
    showfliers = True,
    notch = False
    )
plt.title("Boxplot of New Cases Worldwide")

t2 = []
for i in range(covid_data.shape[0]):
    if covid_data.loc[i,"location"] == "World":
        t2.append(True)
    else:
        t2.append(False)
#plotted both new cases and new deaths worldwide.
ax1 = plt.subplot(312)
world_dates = covid_data.loc[t2,"date"]
world_new_cases = covid_data.loc[t2,"new_cases"]
world_new_deaths = covid_data.loc[t2,"new_deaths"]
plt.plot(world_dates, world_new_deaths, label = "world new cases" )
plt.plot(world_dates, world_new_cases, label = "world new deaths" )
plt.title("Plot of New Cases and New Deaths Worldwide")
plt.xlabel("date")
plt.ylabel("number")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.legend(loc="upper left",
            ncol=1,
            mode="None",
            borderaxespad=0,
            title="legends",
            shadow=False,
            fancybox=True)
plt.show()

#Close the output image to run
#answer the question stated in file question.txt
i = 0
while covid_data.loc[i,"location"] != "United Kingdom":
    i = i + 1
p = i
while covid_data.loc[p,"location"] == "United Kingdom":
    p = p + 1
pu = covid_data.loc[p-1,"total_deaths"] / covid_data.loc[p-1,"total_cases"]
print("proportion of cases have died in the UK:",pu)
i = 0
while covid_data.loc[i,"location"] != "Germany":
    i = i + 1
p = i
while covid_data.loc[p,"location"] == "Germany":
    p = p + 1
gu = covid_data.loc[p-1,"total_deaths"] / covid_data.loc[p-1,"total_cases"]
print("proportion of cases have died in the Germany:",gu)