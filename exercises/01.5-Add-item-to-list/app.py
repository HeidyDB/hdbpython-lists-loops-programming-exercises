# Remember to import random function here
#add 10 random integer to my list 

my_list = [4, 5, 734, 43, 45]

# The magic goes below

import random
nueva_list  =[]

for i in range(1, 11):
    range_numb = random.randint(1,1000)
    my_list.append(range_numb)
   

print (my_list)