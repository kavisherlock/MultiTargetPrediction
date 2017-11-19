from sklearn import tree
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from random import randint

data = 'l'

if data == 'l':
    file_name = "data/letter-recognition.data"
    n_labels = 4
    n_examples = 20000
    n_train = 15000
    n_features = 13
if data == 'y':
    file_name = "data/yeast.txt"
    n_labels = 14
    n_examples = 2147
    n_train = 2000
    n_features = 103
if data == 'e':
    file_name = "data/emotions.txt"
    n_labels = 6
    n_examples = 593
    n_train = 500
    n_features = 72

net_wrong = np.zeros(n_labels)
iterations = 100
print "Ensemble of Chains:", iterations, "iterations"

for x in range(iterations):
    data_file = open(file_name, 'r')
    clf = tree.DecisionTreeClassifier()
    
    letters2 = [[[0 for x in range(n_features)] for x in range(n_examples)] for x in range(n_labels)] 
    labels = [[0 for x in range(n_examples)] for x in range(n_labels)] 
    pred = [[0 for x in range(n_examples)] for x in range(n_labels)] 
    
    letters = []
    indices = range(n_labels)
    np.random.shuffle(indices)

    for i in range(0, n_examples):
        line = data_file.readline()
        letter = line.split(',')
        if data == 'l':    
            letter[0] = ord(letter[0])-65
            letter = map(int, letter)
        else:
            letter = map(float, letter)
        j = 0
        for q in indices:
            labels[j][i] = (letter[n_features+q])
            j += 1
        
        letter = letter[:n_features]
        letters.append(letter)
        for j in range(n_features):
            for k in range(n_labels):
                letters2[k][i][j] = letter[j]
    data_file.close()
        
    for i in range(n_labels):
        if i >= 1:    
            pred[i] = clf.fit(letters2[i-1][:n_train], labels[i][:n_train]).predict(letters2[i-1]).astype(int)
        else:
            pred[i] = clf.fit(letters2[i][:n_train], labels[i][:n_train]).predict(letters).astype(int)
        for k in range(i):
            for j in range(pred[i].size):
                letters2[i][j].append(pred[k][j])
    
    wrong = np.zeros(n_labels)
    for j in range(n_labels):
        for i in range(0, pred[j].size-n_train):
            if (labels[j][n_train+i] != pred[j][n_train+i]):
                wrong[j] += 1
        net_wrong[j] += 100 - wrong[j]*100./(pred[j].size-n_train)
net = 0
for a in net_wrong:
    print a/iterations
    net += a/iterations
print net*1./n_labels