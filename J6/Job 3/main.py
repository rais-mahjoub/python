n = int(input("Taille = "))

def draw_tapis(n):
    space = 0
    for i in range(n+3):
        if i == 0 or i == n+2:
            print('+'+('-'*(n+1))+'+')
        else:
            print('|'+('#'*(n-space))+' '+('#'*space)+'|')
            space+=1

draw_tapis(n)