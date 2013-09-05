#! /usr/bin/python                                                                   
# -*- coding: utf-8 -*- 
import time
starttime = time.clock()

import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from numpy import *

#training_data = [[1,1], [2,2], [-1,-1], [-2,-2]]
training_data = [ ]

#training_label = [1, 1, -1, -1]
training_label = [ ]

#test_data = [[3, 3], [-3, -3]] 
#test_data = [ ] 
#test_key = [ ]

predict_data = [ ]
predict_label = [ ]

features_ = []
labels_ = []

shimdata = { }
count = 1 # shimdataカウント

time1 = time.clock()

#-----------データの下処理----------#
with open('tatsushim.1131','r') as fp:
    for line_ in fp:
        keyword, label = line_.rstrip( ).split( )
        shimdata[keyword] = int(label)
        count = count + 1
        #print keyword, label, count

with open('features.tab','r') as fp:

    for line_ in fp:

        # shimdataをすべて取り終えたらループを抜ける
        if count == 0:
            break
  
        line = line_.rstrip( ).split( )

        keyword = line[0]

        if keyword == 'keyword':
            feature_names = line[1:]
            continue

        # lambda式は「lambda 」の後に引数を指定し、「: 」の後に処理を記述
        #function を list の全ての要素に適用し、返された値からなるリストを返す。
        # map(function, list, ...)
        # - なら0、数字ならint(x)で値を返す
        node = map(lambda x:0 if x == '-' else int(x), line[1:])

        if shimdata.has_key(keyword): 

            if random.random() > 0.5:
                training_data.append(node)
                training_label.append(shimdata[keyword])
            else:
                predict_data.append(node)
                predict_label.append(shimdata[keyword])
            
            features_.append(node)
            labels_.append(shimdata[keyword])
                
            count = count - 1
            
        #shimdataに無いもの(ラベル付けされていないもの)はテスト用に使う
#         else:
#             test_data.append(node)
#             test_key.append(keyword)
#---------------------------------#
features = array(features_)
labels = array(labels_)

predict_data_array = array(predict_data)
predict_label_array = array(predict_label)

time2 = time.clock()

model = RandomForestClassifier(n_estimators=int(sqrt(len(feature_names))),max_features=None,min_samples_split=1)

# ------------------------------model.fit前のスコア--------------------------------
scores = cross_val_score(model,features,labels)
#scores = model.score(predict_data_array,predict_label_array)
print("Step1 Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


model.fit(training_data, training_label)


# ------------------------------model.fit後のスコア--------------------------------
#scores = model.score(predict_data_array,predict_label_array)
scores = cross_val_score(model,features,labels)
print("Step2 Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


#prediction = model.predict(test_data)

#i = 0
# for label in prediction : 
#     #print test_key[i], label  
#     i = i + 1

time3 = time.clock()
print time1-starttime,time2-time1,time3-time2
