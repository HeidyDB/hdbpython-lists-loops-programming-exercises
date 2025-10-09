names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here
names[1]= 'Steven'
names[len(names)-1]='Pepe' #la ultima posision
names[0]= names[2]+names[4] # concatenar 
for i in range(len(names)-1, -1, -1): #imprimir la lista en reverso 
    print(names[i])
