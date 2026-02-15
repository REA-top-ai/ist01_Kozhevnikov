maximum = 100
average = 50
minimum = 10
standart = 5

if maximum > average + 3 * standart or minimum < average - 3 * standart:
    print("В ваших данных имеются выбросы и требуют предобработки")
elif maximum > average + 5 * standart or minimum < average - 5 * standart:
    print("В ваших данных имеются экстремальные значения и требуют предобработки") #
else:
    print("Ваши данные пригодны для анализа")