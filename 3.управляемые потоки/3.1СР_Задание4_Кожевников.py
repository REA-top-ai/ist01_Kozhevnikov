brand = "Volkswagen Polo"
age = 25
experience = 5
reputation = 2
traffic = 4
price = 0.0

if brand == "Volkswagen Polo":
    if 20 <= age <= 27 and 2 <= experience <= 9 and 1 <= reputation <= 2:
        if 1 <= traffic <= 3:
            price = 8
        elif 4 <= traffic <= 7:
            price = 8.5
    elif 20 <= age <= 27 and 2 <= experience <= 9 and 3 <= reputation <= 5:
        if 1 <= traffic <= 3:
            price = 7.5
        elif 4 <= traffic <= 7:
            price = 7.4
    elif 27 <= age <= 34 and 2 <= experience <= 9 and 1 <= traffic <= 3:
        if 1 <= reputation <= 2:
            price = 7.2
        elif 3 <= reputation <= 5:
            price = 7
    elif 27 <= age <= 34 and 2 <= experience <= 9 and 4 <= traffic <= 7:
        if 3 <= reputation <= 5:
            price = 7.2
    elif 27 <= age <= 34 and 10 <= experience <= 15 and 1 <= traffic <= 3:
        if 1 <= reputation <= 2:
            price = 6.9
    elif 27 <= age <= 34 and 10 <= experience <= 15 and 4 <= traffic <= 7:
        if 1 <= reputation <= 2:
            price = 6.7
        elif 3 <= reputation <= 5:
            price = 6.6

elif brand == 'BMW X1':
    if 20 <= age <= 27 and 2 <= experience <= 9 and 1 <= reputation <= 2:
        if 1 <= traffic <= 3:
            price = 12
        elif 4 <= traffic <= 7:
            price = 12.5
    elif 20 <= age <= 27 and 2 <= experience <= 9 and 3 <= reputation <= 5:
        if 1 <= traffic <= 3:
            price = 11.6
        elif 4 <= traffic <= 7:
            price = 11.3
    elif 27 <= age <= 34 and 2 <= experience <= 9 and 1 <= traffic <= 3:
        if 1 <= reputation <= 2:
            price = 11.4
        elif 3 <= reputation <= 5:
            price = 11.7
    elif 27 <= age <= 34 and 2 <= experience <= 9 and 4 <= traffic <= 7:
        if 3 <= reputation <= 5:
            price = 11.9
    elif 27 <= age <= 34 and 10 <= experience <= 15 and 1 <= traffic <= 3:
        if 1 <= reputation <= 2:
            price = 10.8
    elif 27 <= age <= 34 and 10 <= experience <= 15 and 4 <= traffic <= 7:
        if 1 <= reputation <= 2:
            price = 11
        elif 3 <= reputation <= 5:
            price = 10.9

else:
    price=0

if price!=0:
    minut=30
    total=price*minut
    print(f'Стоимость вашей поездки состасит {total} рублей')
else:
    print('Ошибка')