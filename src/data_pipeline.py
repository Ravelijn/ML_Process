import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import StandardScaler

!pip install yellowbrick

from yellowbrick.target import FeatureCorrelation
from scipy.stats import norm
from scipy import stats

import warnings
warnings.filterwarnings("ignore")
color = sns.color_palette()
color_pal = [x['color'] for x in plt.rcParams['axes.prop_cycle']]

#1. Data Collection
data = pd.read_csv(r'C:\\Users\\PPL2\\Documents\\Private\\Model\\Pacmann Data Science\\Project\\Project X/data.csv')
#data_gen = pd.read_csv('../input/spotify-dataset-19212020-160k-tracks/data_by_genres.csv')
#data_w_gen = pd.read_csv('../input/spotify-dataset-19212020-160k-tracks/data_w_genres.csv')
#data_yr = pd.read_csv('../input/spotify-dataset-19212020-160k-tracks/data_by_year.csv')
data_ar = pd.read_csv(r'C:\\Users\\PPL2\\Documents\\Private\\Model\\Pacmann Data Science\\Project\\Project X/artists.csv')
data_top50 = pd.read_csv(r'C:\\Users\\PPL2\\Documents\\Private\\Model\\Pacmann Data Science\\Project\\Project X/top50.csv',encoding='ISO-8859-1')
data.head()

#2. Data Definition
data.describe()
data.info()

#3. Data Splitting
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

df_mod = pd.read_csv(r'C:\\Users\\PPL2\\Documents\\Private\\Model\\Pacmann Data Science\\Project\\Project X/data.csv', usecols=use_col,nrows=30000)
df_mod.to_csv('file1.csv') 
df_mod.head()

X = df_mod.drop(columns=['popularity'])
y = df_mod['popularity']