# Import libraries
import matplotlib.pyplot as plt 
# Import the total number of cases for five countries
dic = {
    'USA':29862124,
    'India':11285561,
    'Brazil':11205972,
    'Russia':4360823,
    'UK':4234924
}

# Generate a pie chart
plt.pie(dic.values(),labels=dic.keys(),autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()