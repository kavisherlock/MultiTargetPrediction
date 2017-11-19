from sklearn import tree
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from random import randint

data = 'l'

clf = SVC()
if data == 'l':
    data_file = open("data/letter-recognition.data", 'r')
    n_labels = 1
    n_examples = 20000
    n_train = 15000
    n_features = 13
if data == 'y':
    data_file = open("data/yeast.txt", 'r')
    n_labels = 1
    n_examples = 2147
    n_train = 2000
    n_features = 16
if data == 'e':
    data_file = open("data/emotions.txt", 'r')
    n_labels = 6
    n_examples = 593
    n_train = 500
    n_features = 72

print "Independent Classifiers"
labels = [[0 for x in range(n_examples)] for x in range(n_labels)] 
pred = [[0 for x in range(n_examples)] for x in range(n_labels)] 

letters = []
    
for i in range(0, n_examples):
    line = data_file.readline()
    letter = line.split(',')
    if data == 'l':    
        letter[0] = ord(letter[0])-65
        letter = map(int, letter)
    else:
        letter = map(float, letter)
    
    for j in range(n_labels):
        labels[j][i] = (letter[j])
    
    letter = letter[1:]
    letters.append(letter)

data_file.close()

for i in range(n_labels):
    pred[i] = clf.fit(letters[:n_train], labels[i][:n_train]).predict(letters[n_train:])
net = 0
wrong = np.zeros(n_labels)
for j in range(n_labels):
    for i in range(0, pred[j].size):
        if (labels[j][n_train+i] != pred[j][i]):
            wrong[j] += 1
    print 100 - wrong[j]*100./pred[j].size
    net += 100 - wrong[j]*100./pred[j].size
print net*1./n_labels