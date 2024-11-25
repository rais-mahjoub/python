first_invest = int(input("Combien souhaitez-vous inverstir ? "))
rendement_annuel = 1.02
valeur = int(first_invest*rendement_annuel)
gain_perte = int(valeur-first_invest)
if gain_perte < 0:
    print("La perte est de", gain_perte, "€.")
else:
    print("Le profit est de", gain_perte, "€.")

new_invest = int(input("Souhaitez-vous continuer à investir ? Si oui, combien souhaitez ajouter ? "))
invest = first_invest+new_invest
rendement_annuel = rendement_annuel+0.02
valeur = int((valeur+new_invest)*rendement_annuel)
gain_perte = int(valeur-invest)
if gain_perte < 0:
    print("La perte est de", gain_perte, "€.")
else:
    print("Le profit est de", gain_perte, "€.")

print(valeur*.1)

new_invest = int(input("Nouvel investissement : "))
invest = invest+new_invest
rendement_annuel = rendement_annuel-0.01
valeur = int((valeur+new_invest)*rendement_annuel)
gain_perte = int(valeur-invest)
if gain_perte < 0:
    print("La perte est de", gain_perte, "€.")
else:
    print("Le profit est de", gain_perte, "€.")
print("Vous avez investi au total", invest, "€.")
print("La valeur totale de votre investissement est de", valeur, "€.")
