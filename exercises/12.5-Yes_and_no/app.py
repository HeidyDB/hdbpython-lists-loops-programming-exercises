the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# a traves del map recorre la lista e imprime wiki o  woko 

def wiki_woko(elemento):
    
        if elemento ==0:
            return 'wiki'
        elif elemento ==1:
            return 'woko'
        
new_list = list(map(wiki_woko, the_bools))
print(new_list)