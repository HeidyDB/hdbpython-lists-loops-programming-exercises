all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def resulting_names(lista):
    return lista[0].lower() == 'r'

lista_R= list(filter(resulting_names, all_names))
print(lista_R)




