mess = input("Entrez le message à chiffrer : ")

def chiffrement(mess):
    rep = ''
    for i in range(len(mess)):
        if mess[i] == ' ':
            rep += ' '
        else:
            asc=ord(mess[i])+3
            print(asc)
            rep+=chr(asc+26*((asc<97)-(asc>122)))
    return rep


print(chiffrement(mess))