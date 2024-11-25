l = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
count = 0
for element in l:
    count+=1
    l[count-1] = int(l[count-1])
for i in range(count):
    for j in range(count-1):
        if l[j]>l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)