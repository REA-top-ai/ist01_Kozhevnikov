statement_one=(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two=(4 * 2 <= 8) and (7 - 1 == 6)

employees = {"Дмитрий": 1,"Ангелина": 2,"Василий": 3,"Екатерина": 4}
user_name = "Дмитрий"
ARM = 2
if user_name in employees and employees[user_name] == ARM:
    print("Добро пожаловать!")
elif user_name == "Дмитрий" and ARM != 1:
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
else:
    print("Логин или пароль не верный, попробуйте еще раз")