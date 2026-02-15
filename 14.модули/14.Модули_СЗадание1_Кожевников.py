import random
def coin_flips():
    try:
        n=int(input('Количество бросков: '))
    except ValueError:
        print('Ведите целое число')
        return
    variants=['Орел','Решка']
    for i in range(n):
        resultat=random.choice(variants)
        print(resultat)
coin_flips()