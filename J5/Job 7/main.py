l=[8,24,48,2,16]
compte=0
for i in range(len(l)):
    if l[i]%3==0:
        compte+=1
if compte<2:
    print(f"Il y a {compte} multiple de 3 dans cette liste")
else:
    print(f"Il y a {compte} multiples de 3 dans cette liste")