nom = 'nom'
prix = 10.00
stock = 5
print("Le produit", nom, "coûte", prix, "€ et il en reste", stock)
qté = int(input("Combien souhaitez-vous en acheter ?"))
stock = stock-qté
print("Il en reste désormais", stock)

prix = prix*1.1
print("Le produit", nom, "coûte", prix, "€ et il en reste", stock)