import random
def dice_flips():
    try:
        n=int(input('Количество бросков: '))
        for i in range(n):
            resultat = random.randint(1,6)
            print(resultat)
    except ValueError:
        print('Ведите целое число')
dice_flips()