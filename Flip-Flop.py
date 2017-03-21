l = [1, 2, 3, 8, 14, 89, 45]
print(l)
for n in range(len(l)//2):
    l[n], l[len(l)-1-n] = l[len(l)-1-n], l[n]
print(l)

