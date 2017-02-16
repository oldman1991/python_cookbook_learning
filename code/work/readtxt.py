# coding=utf-8
# create by oldman at 17/2/16

def readtxt():
    file = open('/Users/lipeng/Desktop/doctors/result.txt', 'r')

    for line in file:
        print(int(line))


if __name__ =="__main__":
    readtxt()