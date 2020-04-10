import hashlib
import csv

def crack_animals(pwd):
    file = open("dico_animaux.txt", "r")
    content = file.read()
    list = content.split("\n")
    for i in list:
        result = hashlib.md5(i.encode()).hexdigest()
        if result == pwd:
            return i
    return False


def crack_name(name, pwd):
    name = str(name)
    result = hashlib.md5(name.encode()).hexdigest()
    if result == pwd:
            return name

    test = name.capitalize()
    result = hashlib.md5(test.encode()).hexdigest()
    if result == pwd:
        return name

    test = name.lower()

    for i in range(9999):
        test = name.lower()
        test += str(i)
        result = hashlib.md5(test.encode()).hexdigest()
        if result == pwd:
            return test
    return False

    test = name.lower()


    for i in range(65, 91):
        test = name.lower()
        test = chr(i)+test
        result = hashlib.md5(test.encode()).hexdigest()
        if result == pwd:
            return test
    return False

all = []
with open('Liste_Atrouver.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        all.append(row)

all.pop(0)

for i in all:
    result = crack_animals(i[2])
    if result == False:
        result = crack_name(i[0], i[2])
    elif result == False:
        result = crack_name(i[1], i[2])
    print(result)