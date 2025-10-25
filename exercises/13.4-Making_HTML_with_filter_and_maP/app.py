all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def filter_colors(color_sexy):
    #color_s = [color_sexy['label'] for color_sexy in all_colors if color_sexy['sexy']]
   # print (f'los colores sexy son: {color_s}')
    return (color_sexy['sexy']) #devuelve ['Red', 'Orange', 'Pink', 'Violet']
	
def generate_li(color):
    return (f'<li>{color["label"]}</li>')

lista_sexy= list(filter(filter_colors, all_colors))  
lista_sexy_con_html = list(map(generate_li, lista_sexy)) 
print (lista_sexy_con_html)
