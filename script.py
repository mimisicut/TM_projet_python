my_list = [2, 3, 10, -50, 0, 33, -4, 64, 88, 100, 6, -5, -9, 99]
list_positif = []
list_negatif = []


for i in my_list:
    if i >= 0:
        list_positif.append(i)
print(list_positif)
list_positif.sort()
print(list_positif[-1])
