invest = int(input("Combien souhaitez-vous inverstir ? "))
rendement_annuel = 1.02
valeur = int(invest*rendement_annuel)
gain_perte = int(valeur-invest)
if gain_perte < 0:
    print("La perte est de", gain_perte, "€.")
else:
    print("Le profit est de", gain_perte, "€.")