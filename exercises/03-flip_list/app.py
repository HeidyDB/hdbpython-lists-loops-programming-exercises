sample_list = [45, 67, 87, 23, 5, 32, 60]

# recorriendo la lista de atras para alante y poniendola en una nueva lista
new_list =[]
for i in range(len(sample_list)-1, -1, -1):
    new_list.append(sample_list[i])

print (new_list)