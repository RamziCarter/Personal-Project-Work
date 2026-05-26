import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#Download and prepare the data
data_root = "https://github.com/argeron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita(USD)"]].values
y = lifesat[["Life Satisfaction"]].values

#Visualize the data
lifesat.plot(kind='scatter', grid=True, x="GDP per capita(USD)", y="Life Satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

#pick a model
model = LinearRegression()
#Train the model
model.fit(X, y)





