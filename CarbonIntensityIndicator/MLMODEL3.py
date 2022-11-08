import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')
df = pd.read_csv(r'C:\Users\harvi\Oiltanker.csv')



x = df.drop(['Fuel Con'], axis=1)
y = df['Fuel Con']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators= 200, random_state=(0))
regressor.fit(x_train, y_train)
predictions = regressor.predict(x_test)
acc = regressor.score(x_test, y_test)
print(acc)

diff = y_test - predictions



import pickle

pickle.dump(regressor, open('./modeltankernew.sav', 'wb'))