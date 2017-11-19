from sklearn import svm
from sklearn.naive_bayes import BernoulliNB 

clf = svm.SVC(gamma=0.001, C=100.)
gnb = BernoulliNB()

data_file = open("data/Digits/trainingimages.txt", 'r')
label_file = open("data/Digits/traininglabels.txt", 'r')
data_test_file = open("data/Digits/testimages.txt", 'r')
label_test_file = open("data/Digits/testlabels.txt", 'r')
digits = []
labels = []
digits_test = []
labels_test = []
for i in range(0, 5000):
    digit = []
    label = label_file.readline()
    for j in range(0,28):
        line = data_file.readline()
        for c in line:
            if c == ' ':
                digit.append(0)
            elif c == '+' or c == '#':
                digit.append(1)
    digits.append(digit)
    labels.append(int(label))
    
for i in range(0, 1000):
    digit = []
    label = label_test_file.readline()
    for j in range(0,28):
        line = data_test_file.readline()
        for c in line:
            if c == ' ':
                digit.append(0)
            elif c == '+' or c == '#':
                digit.append(1)
    digits_test.append(digit)
    labels_test.append(int(label))
    
nb_pred = gnb.fit(digits, labels).predict(digits_test)
svm_pred = clf.fit(digits, labels).predict(digits_test)
wrong = 0
wrongNB = 0

for i in range(0, nb_pred.size):
    if (svm_pred[i] != labels_test[i]):
        wrong += 1
    if (nb_pred[i] != labels_test[i]):
        wrongNB += 1
print wrong, svm_pred.size, 100 - wrong*100./svm_pred.size
print wrongNB, nb_pred.size, 100 - wrongNB*100./nb_pred.size