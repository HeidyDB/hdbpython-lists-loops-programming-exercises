my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# hallar el numero mayor de l lista 
def max_integer(lista):
    maximo= lista[0]
    for i in lista:
        if maximo < i:
            maximo = i

    return (maximo)

print (max_integer(my_list))

