w = int(input("Longueur = "))
h = int(input("Largeur = "))
    
def draw_rectangle(w,h):
    for i in range(h):
        if i == 0 or i == h-1:
            print('|'+('-')*(w-2)+'|')
        else:
            print('|'+(' ')*(w-2)+'|')

draw_rectangle(w,h)