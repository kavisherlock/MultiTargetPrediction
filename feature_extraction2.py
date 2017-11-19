__author__ = "kmunjal2"

filename = "digits_train.txt"

target = open(filename, 'w')
data = open("testimages.txt", 'r')
label_file = open("testlabels.txt", 'r')

for i in range(0, 100):
    digit = ""
    label = label_file.readline()
    for j in range(0,28):
        line = data.readline()
        for c in line:
            if c == ' ':
                digit += "0,"
            elif c == '+' or c == '#':
                digit += "1,"
    digit += label
    target.write(digit)