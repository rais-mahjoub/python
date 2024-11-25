i=0
while i == 0:
    num1 = int(input(""))
    operator = input("")
    num2 = int(input(""))
    
    def calcule(num1, operator, num2):
        if operator == "+":
            return num1+num2
        elif operator == "-":
            return num1-num2
        elif operator == "*":
            return num1*num2
        elif operator == "/":
            return num1/num2
        elif operator == "%":
            return num1%num2
        else:
            return "Erreur : opérateur inconnu"

    print("=", calcule(num1, operator, num2))
    print("------------")