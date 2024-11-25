i=0
while i==0:
    Type = input("Fruit ou Légume ? ")
    saison = input("Quelle saison ? ")
    def liste(Type, saison):
        if Type == "Fruit" or Type == "fruit": 
            if saison == "Hiver" or saison == "hiver":
                return "orange, mandarine et kiwi"
            elif saison == "été" or saison == "Eté":
                return "poire, fraise et cassis"
            else:
                return "Aucun Fruit n'a été trouvé pour la saison renseignée."
        elif Type == "Légume" or Type == "légume":
            if saison == "Hiver" or saison == "hiver":
                return "carotte, topinambour, endive"
            elif saison == "été" or saison == "Eté":
                return "artichaut, aubergine, navet"
            else:
                return "Aucun légume n'a été trouvé pour la saison renseignée." 
        else:
            return "Veuillez choisir entre fruit et légume s'il vous plaît."
    
    print(liste(Type, saison))