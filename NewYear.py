from datetime import date

today = date.today()
print('Сегодня', today)

def NewYear():
    delta = date(date.today().year + 1, 1, 1) - date.today()
    return delta.days

print('До нового года осталось', NewYear(), 'дней')
