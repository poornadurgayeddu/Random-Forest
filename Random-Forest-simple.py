#! /usr/bin/python                                                                   
# -*- coding: utf-8 -*- 

# PythonでRandom Forestを使う　参照(http://qiita.com/tma15/items/769c924dda383a378a63)

from sklearn.ensemble import RandomForestClassifier

training_data = [[1,1], [2,2], [-1,-1], [-2,-2]]
training_label = [1, 1, -1, -1]
test_data = [[3, 3], [-3, -3]] 

model = RandomForestClassifier()
model.fit(training_data, training_label)
prediction = model.predict(test_data)

for label in prediction : print label 
