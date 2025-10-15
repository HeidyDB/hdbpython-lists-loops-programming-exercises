mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# imprimir el tipo de cada elemento de la lista  
def typeoflist(mixlist):
    for element in mixlist:
        print(type(element))