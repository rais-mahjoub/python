print(10+3)

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(alphabet)

alphabet.reverse()
print(alphabet)

ma_string = "Je suis une String"
print(ma_string)

num1 = 40
num2 = 2
print(num1+num2)

num1 = 3
num2 = 14
print(num1*num2)

nom = 'nom'
prix = 10.00
stock = 5
print("Le produit", nom, "coûte", prix, "€ et il en reste", stock)
qté = int(input("Combien souhaitez-vous en acheter ?"))
stock = stock-qté
print("Il en reste désormais", stock)

prix = prix*1.1
print("Le produit", nom, "coûte", prix, "€ et il en reste", stock)

#job 10
first_invest = float
rendement_annuel = float