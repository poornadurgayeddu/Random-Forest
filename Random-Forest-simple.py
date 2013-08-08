#! /usr/bin/python                                                                   
# -*- coding: utf-8 -*- 

import random
from sklearn.ensemble import RandomForestClassifier
#from sklearn.cross_validation import cross_val_score
#from numpy import *

#training_data = [[1,1], [2,2], [-1,-1], [-2,-2]]
training_data = [ ]

#training_label = [1, 1, -1, -1]
training_label = [ ]

#test_data = [[3, 3], [-3, -3]] 
test_data = [ ] 
test_key = [ ]

shimdata = { }

#-----------データの下処理----------#
with open('tatsushim.1131','r') as fp:
    for line_ in fp:
        keyword, label = line_.rstrip( ).split( )
        shimdata[keyword] = int(label)

with open('features.tab','r') as fp:
    for line_ in fp:
        line = line_.rstrip( ).split( )

        keyword = line[0]

        if keyword == 'keyword':
            feature_names = line[1:]
            continue

        #function を list の全ての要素に適用し、返された値からなるリストを返す。
        # map(function, list, ...)
        # - なら0、数字ならint(x)で値を返す
        node = map(lambda x:0 if x == '-' else int(x), line[1:])

        if shimdata.has_key(keyword): 
            training_data.append(node)
            training_label.append(shimdata[keyword])            
        #shimdataに無いもの(ラベル付けされていないもの)はテスト用に使う
        else:
            test_data.append(node)
            test_key.append(keyword)
#---------------------------------#

model = RandomForestClassifier()
model.fit(training_data, training_label)
prediction = model.predict(test_data)

i = 0
for label in prediction : 
    print test_key[i], label  
    i = i + 1
