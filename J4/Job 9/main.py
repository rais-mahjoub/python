i = 0
while i == 0:
    note1 = float(input("Note 1 : "))
    note2 = float(input("Note 2 : "))
    note3 = float(input("Note 3 : "))

    def moyenne(note1, note2, note3):
        return (note1+note2+note3)/3

    moyenne_etudiant = moyenne(note1, note2, note3)

    if moyenne_etudiant >= 15:
        print("Très bon élève")
    elif moyenne_etudiant >= 11:
        print("Bon élève")
    elif moyenne_etudiant >= 8:
        print("Elève moyen")
    else:
        print("Elève devant faire des efforts")

    # print('{0:.2f}'.format(moyenne_etudiant))