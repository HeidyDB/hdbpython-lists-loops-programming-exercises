my_list = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]

def my_function(numbers):
    new_list = []
    for i in numbers:
        # The magic happens here. si es 1 poner 1 si es cero poner yahoo
        if i==1:
            new_list.append(i)
        elif i==0:
            new_list.append("Yahoo")
    
        
        
    return new_list
    
print(my_function(my_list))
