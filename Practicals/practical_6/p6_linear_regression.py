"""
p6_linear_regression.py
Author: Jagrut Gala
Date: 28-08-2021
Practical: 6
Objective: Predict the price of a house  using Linear Regression.
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
Y = np.array(df['price']).reshape(1, -1)
X = np.array(df['tsft']).reshape(1, -1)
# print(f"Shapes: {X.shape} {Y.shape}")
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