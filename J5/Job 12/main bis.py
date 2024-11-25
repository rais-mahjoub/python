l = [7, 11, 42, 39, 2]
print(l)
count = 0
for element in l:
	count += 1
for i in range(count):
	for j in range(count-1):
		if l[j]>l[j+1]:
			l[j], l[j+1] = l[j+1], l[j]
print(l)