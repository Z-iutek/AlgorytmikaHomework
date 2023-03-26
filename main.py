from random import randint
from time import time
from cleanUpFuncions import converging_pointers, copy_over
from sortingFuncions import insertion_sort, merge_sort
from searchFunctions import binary_search, linear_search

# 1.Wylosować n- elementów z  zakresu od 0 – 100 (Random.randint(0,100))
n = int(input("Podaj wartość n: "))
list_of_n_elements = []

for i in range(n):
    list_of_n_elements.append(randint(0, 100))
# 2.Wylosować wartość z przedziału <0,100> jako tzw. wartość śmieciową
garbage_value = randint(0, 100)

# 3.Wyczyścić dane za pomocą algorytmów data clean-ups:
# A)copy-over
# B)shuffle-left albo converging pointers

# A)copy-over:
print("\nCzyszczenie przy pomocy algorytmu copy-over:\n")
temp1 = list_of_n_elements[:]
print("Wartość śmieciowa: " + str(garbage_value))
print("Lista przed sprzątaniem:" + str(temp1))
cleaned_up_list_2 = copy_over(garbage_value, temp1)
print("Lista po sprzątaniu:    " + str(cleaned_up_list_2))
print("\n")

# B) converging pointers
print("Czyszczenie przy pomocy algorytmu converging pointers:\n")
temp2 = list_of_n_elements[:]
print("Wartość śmieciowa: " + str(garbage_value))
print("Lista przed sprzątaniem:" + str(temp2))
cleaned_up_list = converging_pointers(garbage_value, temp2)
print("Lista po sprzątaniu:    " + str(cleaned_up_list))
print("\n")


# 4.Posortować listę za pomocą:
# A)insertion sort
# B)merge sort

# A)insertion sort:
print("Sortowanie przy pomocy algorytmu insertion sort:\n")
temp3 = list_of_n_elements[:]
print("Lista przed sortowaniem:" + str(temp3))
sorted_list = insertion_sort(temp3)
print("Lista po sortowaniu:    " + str(sorted_list))
print("\n")

# B) merge sort
print("Sortowanie przy pomocy algorytmu merge sort:\n")
temp4 = list_of_n_elements[:]
print("Lista przed sortowaniem:" + str(temp4))
sorted_list2 = merge_sort(temp4)
print("Lista po sortowaniu:    " + str(sorted_list2))
print("\n")

# 5.Wyszukać na liście wylosowaną wartość z zakresu <0,100> bez uwzględnienia wartości śmieciowej
# A)binary search
# B)linear/sequential search - (nie trzeba wcześniej sortować)

# Losujemy wartość <0,100> z wykluczeniem wartości śmieciowej
flag = True
value_to_find = randint(0, 100)
while flag:
    if value_to_find == garbage_value:
        value_to_find = randint(0, 100)
    else:
        flag = False

# A) merge sort plus binary search
temp5 = list_of_n_elements[:]
print("Wartość: " + str(value_to_find) + " znajduje się pod indeksem: " + str(binary_search(merge_sort(temp5), value_to_find)))

# B) linear search
temp6 = list_of_n_elements[:]
print("Wartość: " + str(value_to_find) + " znajduje się pod indeksem: " + str(linear_search(temp6, value_to_find)))
