import random
import string
def password_generator(length):
    letters = string.ascii_letters
    password="".join(random.choice(letters) for i in range(length))
    return password
try:
    user_input=int(input('Длина пароля: '))
    if user_input <= 0:
        print('Длина - положительное число')
    else:
        result=password_generator(user_input)
        print(f'Ваш пароль: {result}')
except ValueError:
    print('Ошибка')