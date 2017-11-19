__author__ = "kmunjal2"

filename = "digits_test.arff"

att = "@attribute "
name = ["firstName", "lastName"]
target = open(filename, 'w')
data = open("testimages.txt", 'r')
label_file = open("testlabels.txt", 'r')

target.write("@relation digits")
target.write("\n\n")

for i in range(0,28):
    for j in range (0,28):
        line = att + "position[" + str(i) + "][" + str(j) + "] {1,0}\n"
        target.write (line)

target.write("@attribute Class {0,1,2,3,4,5,6,7,8,9}\n")
target.write("\n@data\n")

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