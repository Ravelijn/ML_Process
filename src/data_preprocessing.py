import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import StandardScaler


use_col =['acousticness','danceability','loudness','popularity','duration_ms','energy','speechiness','valence']

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

X = df_mod.drop(columns=['popularity'])
y = df_mod['popularity']

x_train,x_test,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=27)