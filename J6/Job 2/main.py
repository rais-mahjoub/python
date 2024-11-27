h = int(input("hauteur = "))

def draw_triangle(h):
    space = 0
    if h<=1:
        print('Erreur')
    else:
        for i in range(h):
            if i != h-1:
                print((' '*(h-(i+1)))+'/'+(' '*space)+'\\')
                space += 2
            else:
                print('/'+('_'*((h-1)*2))+'\\')
            
draw_triangle(h)