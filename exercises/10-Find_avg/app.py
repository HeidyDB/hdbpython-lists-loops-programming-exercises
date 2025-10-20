my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

# promedio de los valores de la lista

suma=0
for i in range(0, len(my_list)):
    suma += my_list[i]
promedio= suma / (len(my_list))
print (promedio)