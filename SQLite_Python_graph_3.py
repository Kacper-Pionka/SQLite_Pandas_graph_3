# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sqlite3

x = []
y = []
z = 0

conn = sqlite3.connect('chinook.sqlite')
print("Opened database successfully");

cursor = conn.execute("SELECT billingcountry, SUM(total) FROM invoice GROUP BY billingcountry ORDER BY SUM(total)")
for row in cursor:
   if row[1] > 50:      #values that are smaller than 50 are summed and
      x.append(row[0])  #displayed on chart as Others
      y.append(row[1])
   else:
      z = row[1] + z
   
y.append(z)
x.append('Others')

#prints data used to draw chart
print(pd.DataFrame(data = {'countries' : x,
                           'total' : y}))

#colors used in pie chart
colors = ['#00ff66','#a6ff00','#ffb300','#ff5e00','#ff1100',
          '#00ffd5','#00a6ff','#002aff','#c800ff','#ff0088']

#value of explode
explode = [0.03 for i in range(len(x))]

fig1, ax1 = plt.subplots()
ax1.pie(y, colors = colors, labels = x, autopct='%1.1f%%', startangle=90, pctdistance=0.85,
        explode = explode)

#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax1.axis('equal')
plt.tight_layout()
plt.show()

conn.close()
