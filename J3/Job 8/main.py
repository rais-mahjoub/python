a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a+b > c and b+c > a and c+a > b:
    print("On peut construire un triangle avec ces longueurs.")
    if (a**2)+(b**2)==(c**2) or (b**2)+(c**2)==(a**2) or (a**2)+(c**2)==(b**2):
        if a==b or b==c or c==a:
            print("Ce triangle serait rectangle et isocèle")
        else:
            print("Ce triangle serait rectangle")
        
    elif a==b==c:
        print("Ce triangle serait équilatéral")

    elif a==b or b==c or c==a:
        print("Ce triangle serait isocèle")

    else:
        print("Ce triangle serait quelconque")

else:
    print("On ne peut pas construire un triangle avec ces longueurs.")

