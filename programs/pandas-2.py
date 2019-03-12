# -*- coding: utf-8 -*-

#IRIS DATA SET

import pandas as pd
iris =pd.read_csv('iris.csv')
print('data frame ', iris)
iris.head()
# Map
iris["setosa"] = iris.Species.map({"setosa" : 1,"versicolor":0, "virginica" : 0})
iris.head()

pd.get_dummies(iris.Species,prefix = "Species")
pd.get_dummies(iris.Species,prefix = "Species").iloc[:,0:1]  #1 is not included
species_dummies = pd.get_dummies(iris.Species,prefix = "Species").iloc[:,0:]

