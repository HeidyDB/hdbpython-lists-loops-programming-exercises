my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# sumar solo los impares 
def sum_odds(lista):

    sum_odd=0
    for i in lista:
        if i%2!=0:
            sum_odd+=i

    return sum_odd
print (sum_odds(my_list))
