i = 0

while i == 0:
    langage = input("Quel est votre langage de prédilection ? ")
    def chanson():
        print("Un jour, je serai le meilleur développeur")
        print("Je coderai sans répis")
        print("Je ferai tout mettre en valeur")
        print("Tout ce que j'aurai appris")
        print()
        print("La Plateforme_!")
    def lang(langage):
        if langage == "JavaScript" or langage == "javascript" or langage == "JS" or langage == "js" or langage == "Javascript":
            print("Tu es un dév Web !")
        elif langage == "Python" or langage == "python":
            print("Tu es un dév IA !")
        elif langage == "Java" or langage == "java":
            print("Tu es un dév logiciel !")
        elif langage == "ReactJS" or langage == "reactjs":
            print("Tu es un dév mobile !")
        else:
            chanson()

    lang(langage)