l = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(l)
count = 0
for element in l:
	count += 1
for i in range(count**2):
	for j in range(count-1):
		if l[j]>l[j+1]:
			l[j], l[j+1] = l[j+1], l[j]
a=0
while a<count-1:
	if l[a]==l[a+1]:
		del l[a]
		count -= 1
	a+=1
print(l)