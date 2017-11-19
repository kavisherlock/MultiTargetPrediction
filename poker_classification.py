from sklearn import tree
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

def convert_to_binary(x):
    binary_x = []
    for i in range (0,4):
        digit = x%2
        x = int(x/2)
        binary_x.append(digit)
    return binary_x


clf = OneVsRestClassifier(LinearSVC(random_state=0))
#clf = tree.DecisionTreeClassifier()

data_file = open("data/Poker/poker-hand-training-true.data", 'r')
test_file = open("data/Poker/poker-hand-testing.data", 'r')
digits = []
labels = []
digits_test = []
labels_test = []
for i in range(0, 25000):
    line = data_file.readline()
    digit = line.split(',')
    digit = map(int, digit)
    label = digit[10]
    digit = digit[:10]
    binary_digit = []
    for i in digit:
        bin_i = convert_to_binary(i)
        for b in bin_i:
            binary_digit.append(b)
    digits.append(binary_digit)
    labels.append(label)
    

for i in range(0, 100000):
    line = test_file.readline()
    digit = line.split(',')
    digit = map(int, digit)
    label = digit[10]
    digit = digit[:10]
    binary_digit = []
    for i in digit:
        bin_i = convert_to_binary(i)
        for b in bin_i:
            binary_digit.append(b)
    digits_test.append(binary_digit)
    labels_test.append(label)

print digits_test[10000], labels[10000]

svm_pred = clf.fit(digits, labels).predict(digits_test)
wrong = 0
wrongNB = 0
for i in range(0, svm_pred.size):
    if (svm_pred[i] != labels_test[i]):
        wrong += 1
    
print wrong, svm_pred.size, 100 - wrong*100./svm_pred.size
