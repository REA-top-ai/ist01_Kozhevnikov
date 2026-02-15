correct_answers = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1)
answers=[]
for i in range(1,21):
    a=int(input(i))
    answers.append(a)
if tuple(answers)==correct_answers:
    print('Результат: экзамен сдан')
else:
    print("Результат: экзамен провален")