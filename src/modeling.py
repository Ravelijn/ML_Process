import seaborn as sns 
from sklearn.preprocessing import StandardScaler

from yellowbrick.target import FeatureCorrelation
from scipy.stats import norm
from scipy import stats

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split


use_col = ['acousticness','danceability','loudness','popularity','duration_ms','energy','speechiness','valence']



df_mod = pd.read_csv(r'C:\\Users\\PPL2\\Documents\\Private\\Model\\Pacmann Data Science\\Project\\Project X/data.csv', usecols=use_col,nrows=30000)
df_mod.to_csv('file1.csv') 
df_mod.head()

X = df_mod.drop(columns=['popularity'])
y = df_mod['popularity']


cor = df_mod.corr()
sns.heatmap(cor)

x_train,x_test,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=27)