from sklearn import tree
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from random import randint
    
data_file = open("data/yeast.txt", 'r')
clf = tree.DecisionTreeClassifier()
n_labels = 14

labels = [[0 for x in range(2417)] for x in range(n_labels)] 
pred = [[0 for x in range(2417)] for x in range(n_labels)] 

yeasts = []
for i in range(0, 2417):
    line = data_file.readline()
    yeast = line.split(',')
    yeast = map(float, yeast)
    
    for j in range(n_labels):
        labels[j][i] = (yeast[103+j])
    
    yeast = yeast[:103]
    yeasts.append(yeast)

data_file.close()

n_train = 2000

for i in range(n_labels):
    pred[i] = clf.fit(yeasts[:n_train], labels[i][:n_train]).predict(yeasts[n_train:])

wrong = np.zeros(n_labels)
for j in range(n_labels):
    for i in range(0, pred[1].size):
        if (labels[j][n_train+i] != pred[j][i]):
            wrong[j] += 1
    print 100 - wrong[j]*100./pred[j].size