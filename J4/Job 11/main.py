i = 0
while i == 0:
    temps = int(input("Entrez un temps en minute : "))
    def time_to_text(temps):
        horas = temps//60
        minutos = temps%60
        return f"{horas} heures et {minutos} minutes"
    print(time_to_text(temps))
