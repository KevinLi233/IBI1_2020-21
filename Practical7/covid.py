import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("D:\IBI1\IBI1_2020-21\Practical7")

covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:11:2,0:5])
t1 = []
for i in range(covid_data.shape[0]):
    if covid_data.loc[i,"location"] == "Afghanistan":
        t1.append(True)
    else:
        t1.append(False)
print("Mean:",np.mean(covid_data.iloc[t1,2]))    
print("Median:",np.median(covid_data.iloc[t1,2]))

plt.figure(figsize=(6,6), dpi=100)
plt.figure(1)
ax1 = plt.subplot(211)
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

t2 = []
for i in range(covid_data.shape[0]):
    if covid_data.loc[i,"location"] == "World":
        t2.append(True)
    else:
        t2.append(False)

ax1 = plt.subplot(212)
world_dates = covid_data.loc[t2,"date"]
world_new_cases = covid_data.loc[t2,"new_cases"]
world_new_deaths = covid_data.loc[t2,"new_deaths"]
plt.plot(world_dates, world_new_deaths, 'b')
plt.plot(world_dates, world_new_cases, 'r')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()



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