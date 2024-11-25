nombre = int(input("x = "))
def Nombre(nombre):
    if nombre>0:
        return f"{nombre} est positif."
    elif nombre<0:
        return f"{nombre} est négatif."
    else:
        return f"{nombre} est nul."

print(Nombre(nombre))