from sklearn import tree
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB

def convert_to_binary(x):
    binary_x = []
    for i in range (0,4):
        digit = x%2
        x = int(x/2)
        binary_x.append(digit)
    return binary_x


#clf = OneVsRestClassifier(LinearSVC(random_state=0))
#clf = MultinomialNB()
#clf = LinearSVC()
#clf = tree.DecisionTreeClassifier()

data_file = open("data/Covtype/covtype.data", 'r')
test_file = open("data/Covtype/covtype_test.data", 'r')
digits = []
labels = []
digits_test = []
labels_test = []
for i in range(0, 50000):
    line = data_file.readline()
    digit = line.split(',')
    digit = map(int, digit)
    label = digit[54]
    digit = digit[:54]
    digits.append(digit)
    labels.append(label)

data_file.close()

for i in range(0, 80000):
    line = test_file.readline()
    digit = line.split(',')
    digit = map(int, digit)
    label = digit[54]
    digit = digit[:54]
    digits_test.append(digit)
    labels_test.append(label)

test_file.close()
svm_pred = clf.fit(digits, labels).predict(digits_test)
wrong = 0

for i in range(0, svm_pred.size):
    if (svm_pred[i] != labels_test[i]):
        wrong += 1
    
print wrong, svm_pred.size, 100 - wrong*100./svm_pred.size
