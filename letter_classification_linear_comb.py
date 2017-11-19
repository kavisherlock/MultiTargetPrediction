from sklearn import tree
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from random import randint


iterations = 1
N = 1000
print "Linear Combinations:", N, "new targets,", iterations, "iterations"
   
data = 'e'

clf = tree.DecisionTreeClassifier()
if data == 'l':
    data_file = open("data/letter-recognition.data", 'r')
    n_labels = 4
    n_examples = 20000
    n_train = 15000
    n_features = 13
if data == 'y':
    data_file = open("data/yeast.txt", 'r')
    n_labels = 14
    n_examples = 2147
    n_train = 2000
    n_features = 103
if data == 'e':
    data_file = open("data/emotions.txt", 'r')
    n_labels = 6
    n_examples = 593
    n_train = 500
    n_features = 72
    
labels = [[0 for x in range(n_examples)] for x in range(N)] 
org_labels = [[0 for x in range(n_examples)] for x in range(n_labels)] 
svm_pred = [[0 for x in range(n_examples)] for x in range(N)] 

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
        org_labels[j][i] = (letter[n_features+j])
    
    letter = letter[:n_features]
    letters.append(letter)

data_file.close()
    
acc = np.zeros(n_labels)
for x in range(iterations):
    a = []
    for i in range (N):
        a.append(np.zeros(n_labels))
        for j in range(n_labels):
            a[i][j] = randint(0,9)
    a = np.matrix(a)
    inva = np.linalg.inv(a.getT()*a)*a.getT()
    
    for i in range(0, n_examples):
        old_labels = np.zeros(n_labels)
        for j in range(n_labels):    
            old_labels[j] = org_labels[j][i]
        old_labels = np.matrix(old_labels)
        new_labels = np.array((a*(old_labels.getT())))
        for j in range(N):
            labels[j][i] = (new_labels[j][0])
    
    for i in range(N):
        svm_pred[i] = clf.fit(letters[:n_train], labels[i][:n_train]).predict(letters[n_train:])
    
    wrong = np.zeros(n_labels)
    for i in range(0, svm_pred[1].size):
        new_labels = np.zeros(N)
        for j in range(N):
            new_labels[j] = svm_pred[j][i]
        
        new_labels = np.matrix(new_labels)
        new_labels = np.rint(np.array(inva*(new_labels.getT())))
    
        for j in range(n_labels):
            if (new_labels[j] != org_labels[j][n_train+i]):
                wrong[j] += 1
    
    for i in range(n_labels):
        acc[i] += 100 - wrong[i]*100./svm_pred[1].size
net = 0
for x in range (n_labels):
    acc[x] = acc[x]*1./iterations
    print acc[x]
    net += acc[x]
print net*1./n_labels
