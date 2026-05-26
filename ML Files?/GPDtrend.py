#Page 22, using GDP to learn if money makes people happy (GDP per capita)
#Like y = mx + b in algebra Theta 1 and Theta 0 for finding the best fit line are just the intercept and the slope


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

#Visualize the data
lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

#pick a model
model = LinearRegression()
#Train the model (function to find which theta values represent the best line)
model.fit(X, y)

#Cyprus GDP prediction based on training data from 2022
X_new = [[37_655.2]]
print(model.predict(X_new))

X_new_2 = [[105_446.2]]
print(model.predict(X_new_2))






