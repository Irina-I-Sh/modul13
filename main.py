price1 = 0 # младше 18 лет
price2 = 990 # от 18 до 25 лет
price3 = 1390 # старше 25 лет
s = 0
n = int(input('Сколько билетов хотите купить? '))
if n < 0 or n > 20:
    raise ValueError('Введенное количество билетов не действительно или больше допустимого')
if n > 0:
    for i in range (1,n+1):
        print('\nПосетитель', i)
        age = int(input('Введите возраст посетителя '))
        if age > 100 or age <= 0:
            raise ValueError('Возраст не действительный')
        elif age < 18:
            price = price1
        elif 18 <= age <= 25:
            price = price2
        elif age > 25:
            price = price3
        s += price
if n > 3:
    s -= s/10
print('\nСумма к оплате = ', s)