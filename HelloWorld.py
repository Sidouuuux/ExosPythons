#exo 1
time =6.892
distance = 19.7

print(round(distance/time))

#exo 2
name = input("Nom : ")
age = input("Age : ")

print("je suis "+str(name)+" et j'ai "+str(age))

#exo 3
import math

number = int(input("Number : "))

if number >= 0:
    print(math.sqrt(number))
else:
    print("Erreur Nb")

#exo 4

list = []

word = str(input("Word 1 : "))
list.append(word)
word = str(input("Word 2 : "))
list.append(word)
list.sort()
print(list[0])

#////////////

word1 = str(input("Word 1 : "))
word2 = str(input("Word 2 : "))
word1.upper()
word2.upper()
ascii1 = 0
ascii2 = 0
for c in word1:
    ascii1 += ord(c)

for c in word2:
    ascii1 += ord(c)

if ascii1 < ascii2:
    print(word2)
else:
    print(word1)

#exo 5

pression = float(input("Pression : "))
volume = float(input("Volume : "))

if pression >= 2.3 & volume >= 7.41:
    print("STOP NOW")
elif pression >= 2.3 & volume < 7.41:
    print("Increase volume")
elif pression < 2.3 & volume >= 7.41:
    print("Decrease  volume")
else:
    print("It's Ok")

#exo 6

mail = input("Mail : ")

if mail.find('@') != -1 and mail.find('.com') != -1:
    print("It's a mail")
else:
    print("It's not a mail")

#exo 7

for i in range(10):
    print("Afficher 10fois un message")

#exo 8

word = input("Mot : ")

for c in word:
    print(c)

#exo 9

a = 0
b = 10

while a < b:
    a += 1

#exo 10

b = 10

while b > 0:
    print(b) if b%2 != 0 else ""
    b -= 1

#exo 11

number = int(input("number : "))

while number < 1 or number > 10:
    number = int(input("Invalid, retry : "))

#exo 12

word = input("Mot : ")

for c in word:
    print(c, end = "")

print("\n")
list = [ "Oui", "Hier", "Peut-etre", "Café"]

for l in list:
    print(l)

#exo 13

for i in range(0, 15, 3):
    print(i, end = " ")

#exo 14

n = int(input("N : "))
a = 1

while a <= n:
    tmp=0
    for i in range(2):
        tmp+=a

    print(tmp)
    a+=1