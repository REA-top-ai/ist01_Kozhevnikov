user_name_test1 = "Дмитрий"
user_name_test2 = "Ангелина"

Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
Welcome_message = "Добро пожаловать"

def check_user(user):
    if user == "Дмитрий":
        print(Dmitriy_check)
    else:
        print(Welcome_message)

check_user(user_name_test1)
check_user(user_name_test2)

enter_number=0
if enter_number < 3:
    attempts_left = 3 - enter_number
    print(f"Попробуйте еще раз. У вас осталось {attempts_left} попыток.")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")
