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
   x.append(row[0])
   y.append(row[1])
'''
xa = {
   'one' : x,
   'two' : y}

myvar = pd.DataFrame(xa)
print(myvar.to_string())''' #Prints all data for pie chart

plt.pie(y, labels = x)
plt.show()              #Shows total amount of money spend in each country in form of pie chart

conn.close()
