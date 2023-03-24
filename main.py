from random import randint
from time import time
from cleanUpFuncions import coverging_pointers, copy_over

n = int(input("Podaj wartość n <0,100>: "))
listOfNElements = []

for i in range(n):
    listOfNElements.append(randint(0, 100))

garbageValue = randint(0, 100)

temp1 = listOfNElements[:]
print("GV: " + str(garbageValue))
print("Lista przed sprzątaniem:" + str(temp1))
cleanedUpList = coverging_pointers(garbageValue, temp1)
print("Lista po sprzątaniu:    " + str(cleanedUpList))

temp2 = listOfNElements[:]
print("GV: " + str(garbageValue))
print("Lista przed sprzątaniem:" + str(temp2))
cleanedUpList2 = copy_over(garbageValue, temp2)
print("Lista po sprzątaniu:    " + str(cleanedUpList2))
