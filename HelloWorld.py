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