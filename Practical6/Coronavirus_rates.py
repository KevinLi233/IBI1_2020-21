# Import libraries
import matplotlib.pyplot as plt 
# Import the total number of cases for five countries

# set all the country and cases
country = ['USA','India','Brazil','Russia','UK']
cases = [29862124,11285561,11205972,4360823,4234924]
fre = []
total = sum(cases)
# calculate the frequency
for i in range(len(cases)):
    fre.append(cases[i] / total)
# generate frequency dictionary 
dicfre = dict(zip(country,fre))
# generate cases dictionary
dic = dict(zip(country,cases))
# output frequency
print(dicfre)
# Generate a pie chart
plt.pie(dic.values(),labels=dic.keys(),autopct='%1.1f%%',shadow=True,startangle=90)
plt.title('Pie Chart about Frequency of Total Number of Cases for Five Countries')
plt.axis('equal')
plt.show()

