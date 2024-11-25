def my_long_word(longueur, phrase):
    taille_phrase = 0
    mots = []
    mot = ""
    nbe_de_mots = 0
    for a in phrase:
        taille_phrase+=1
        if a == " ":
            mots += [mot]
            mot == ""

            nbe_de_mots += 1
            
        else:
            mot += a
    print(mots)
    taille_mot = 0
    for i in mots:
        for j in i:
            for b in mots[j]:
                taille_mot += 1
        if taille_mot<longueur:
                del b
            
            

print(my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance "))