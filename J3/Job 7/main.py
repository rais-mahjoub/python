alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]*10
str_alphabet = ''.join(alphabet)
j = 1
while j<=len(alphabet) :
        print(str_alphabet[slice(0,j)])
        j += 2
