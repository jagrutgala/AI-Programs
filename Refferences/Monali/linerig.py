"""
linerig.py
Author: Jagrut Gala
Date: 
Objective: Predict the price of house  using Linear Regression
"""

import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets, linear_model 
import pandas as pd
import io
from pathlib import Path
p= Path(__file__).parent/ "Housing.xlsx"
fio= io.open(p, "rb")
df = pd.read_excel(fio)
print(df)
Y = df['price']
X = np.array(df['tsft']).reshape(1, -1)
# # Plot outputs 
plt.scatter(X, Y) 
plt.title('Test Data') 
plt.xlabel('Size') 
plt.ylabel('Price') 
plt.xticks(()) 
plt.yticks(())
# # Create linear regression object 
regr = linear_model.LinearRegression()
# # Train the model using the training sets 
regr.fit(X, Y)
# # Plot outputs 
plt.plot(X, regr.predict(X), color='red',linewidth=3) 
plt.show()