from datetime import datetime
n = datetime.now().minute
print(n)
color = n % 5
if color < 3:
    print('GREEN! GO!')
else:
    print('RED! STOP!')