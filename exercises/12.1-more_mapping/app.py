my_numbers = [23,234,345,4356234,243,43,56,2]

# Your code here
'''
Use the list map() function to run the multiply_by_three function through each value in the list.
'''
def multiply_by_three(number):
    return (number*3)

new_list = list(map(multiply_by_three, my_numbers))
#toma la lista my_number y le aplica la funcion 
#multiply_by_three a cada elemento de la lista 

print(new_list)
