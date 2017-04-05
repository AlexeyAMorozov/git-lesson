def palindrome(a):
    z=int(len(a)/2)
    if a[:z] == a[::-1][:z]:
        print('Это палиндром!')
    else:
        print('Это не палиндром!')

palindrome(input('Введите строку:',))