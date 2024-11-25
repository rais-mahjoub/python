liste=[8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
def maximum(liste):
    maxi = liste[0]
    for i in liste:
        if i >= maxi:
            maxi = i
    return maxi
def minimum(liste):
    mini = liste[0]
    for i in liste:
        if i <= mini:
            mini = i
    return mini
print("Vmax :", maximum(liste))
print("Vmin :", minimum(liste))