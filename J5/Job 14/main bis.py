def my_long_word(longueur, phrase):
    result = ""
    mot = ""
    taille_mot = 0
    for a in phrase:
        if a != " " and a != ",":
            mot += a
            taille_mot += 1
        else:
            # print(mot)
            if longueur<taille_mot:
                result += mot
                result += " "
            taille_mot = 0
            mot = ""
    return result

print(my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance "))