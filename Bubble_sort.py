lst = [1, 2, 3, 8, 14, 89, 45]
n=len(lst)
m=n-1
while m>0:
    for i in range(m):
        if (lst[i]>lst[i+1]):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    m=m-1
print(lst)
