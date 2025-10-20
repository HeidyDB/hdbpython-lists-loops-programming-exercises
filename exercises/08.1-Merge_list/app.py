chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here. unir las dos listas 
    chunk_both= []
    for i in list1:
        chunk_both.append(i)
    for i in list2:
        chunk_both.append(i)

    return (chunk_both)



    
print(merge_list(chunk_one, chunk_two))
