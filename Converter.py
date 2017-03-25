def dec_2_bin(n):
    bin = ''
    while n != 0:
        bin += str(n % 2)
        n //= 2
    return bin[::-1]

def bin_2_dec(l):
    x = 0
    i = 0
    y = len(l)

    while i < y:
        if l[i] == '1':
            x += 2 ** (y - i - 1)
        if l[i] != '1' and l[i] != '0':
            return 'Input Error'
        i += 1
    return x

n = int(input('10 => 2: '))
print(dec_2_bin(n))
n = str(input('2 => 10: '))
print(bin_2_dec(n))
