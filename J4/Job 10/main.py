i = 0
while i == 0:
    nombre = float(input("Entrez un nombre entier positif : "))
    IsInt = nombre.is_integer()
    def parité(nombre):
        if nombre > 0 and IsInt == True:
            if nombre%2 == 0:
                return f"le nombre {int(nombre)} est pair"
            else:
                return f"le nombre {int(nombre)} est impair"
        else:
            return "Ce nombre n'est pas valide."
    
    print(parité(nombre))
    # print(IsInt)