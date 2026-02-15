import random

phrases1 = ["Коллеги,", "Однако,", "Тем не менее,", "Следовательно,", "Соответственно,", "Вместе с тем,", "С другой стороны,"]
phrases2 = ["парадигма цифровой трансформации", "контекст цифровой трансформации", "диджитализация бизнес-процессов", ...]
phrases3 = ["открывает новые возможности для", "выдвигает новые требования", ...]
phrases4 = ["дальнейшего углубления", "бюджетного финансирования", ...]
phrases5 = ["знаний и компетенций.", "непроверенных гипотез.", ...]

idx1 = random.randint(0, 7)
idx2 = random.randint(0, 7)
idx3 = random.randint(0, 7)
idx4 = random.randint(0, 7)
idx5 = random.randint(0, 7)
full1=phrases1[idx1]
full2=phrases2[idx2]
full3=phrases3[idx3]
full4=phrases4[idx4]
full5=phrases5[idx5]
print(f'{full1} {full2} {full3} {full4} {full5}')