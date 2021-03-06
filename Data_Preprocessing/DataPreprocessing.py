# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas  as pd

# Importing the dataset
datasets = pd.read_csv('Data.csv')
x = datasets.iloc[:,:-1].values
y = datasets.iloc[:,-1].values

print(x)
print(y)

# Taking Care of Missing Data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

print(x)

# Encoding the Independent Variable

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

print(x)

# Encoding the Dependent Variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 1)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

# Feature Scaling
from sklearn.preprocessing import StandardScaler as sr
ss = sr()
x_train[:, 3:] = ss.fit_transform(x_train[:, 3:])
x_test[:, 3:] = ss.transform(x_test[:, 3:])

print(x_train)
print(x_test)
