mdp = input("Entrez un mot de passe : ")
def valid_mdp(mdp):
    maj = False
    mnsc = False
    sifr = False
    carac = False
    carac_auth = "!@#$%^&*"
    if len(mdp)<8:
        return 'invalide'
    else:
        for i in mdp:
            if 'A'<=i<='Z':
                maj = True
            elif 'a'<=i<='z':
                mnsc = True
            elif '0'<=i<='9':
                sifr = True
            elif i in carac_auth:
                carac = True
            else:
                return 'invalide'
        if maj==True and mnsc==True and sifr==True and carac==True:
            return "Le mot de passe a bien été enregitré."
        else:
            return 'invalide'
def add_json(nw_mdp, filename='mdp.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        mdp_saved = jp.parse("$.mdp")
        dr_dre = mdp_saved.find(file_data)
        if dr_dre!=mdp_secu:
            file_data['mdps'].append(nw_mdp)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
            

valid_mdp(mdp)
if valid_mdp(mdp) == 'invalide':
    print("Merci d'entrer un mot de passe valide.")
    mdp = input("Entrez un mot de passe : ")
    valid_mdp(mdp)
else:   
    print(valid_mdp(mdp))
    import hashlib
    import json
    import  
    mdp_secu = hashlib.sha256(mdp.encode()).hexdigest()
    nw_mdp = {"mdp": mdp_secu}
    add_json(nw_mdp)
