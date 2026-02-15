import datetime

employees=[{'Name':'Иванов Иван Иванович','Post': 'Менеджер','Date': '22.10.2013', 'Salary': '250 000'},
{'Name':'Сорокина Екатерина Матвеевна','Post': 'Аналитик','Date': '12.03.2020', 'Salary': '75 000'},
{'Name':'Струков Иван Сергеевич','Post': 'Старший программист','Date': '23.04.2012', 'Salary': '150000'},
{'Name':'Корнеева Анна Игоревна','Post': 'Ведуший программист','Date': '22.02.2015', 'Salary': '120 000'},
{'Name':'Старчиков Сергей Анатольевич','Post': 'Младший программист','Date': '12.11.2021', 'Salary': '50 000'},
{'Name':'Бутенко Артем Андреевич','Post': 'Архитектор','Date': '12.02.2010', 'Salary': '200 000'},
{'Name':'Савченко Алина Сергеевна','Post': 'Старший аналитик','Date': '13.04.2016', 'Salary': '100 000'},
        ]
def programmers_bonus(emp_list):
    for emp in emp_list:
        if 'программист' in emp['Post'].lower():
            bonus=['Salary']*0.03
            print({emp['Name']:bonus})

def gender_bonus(emp_list):
    for emp in emp_list:
        name=emp['Name']
        if 'Анна' in name or 'Екатерина' in name or 'Алина' in name:
            print(f'Премия к 8 марта для {emp['Name']}: 2000')
        else:
            print(f'Премия к 23 февраля для {emp['Name']}: 2000')

def index_bonus(emp_list):
    today=datetime.date.today()
    for emp in emp_list:
        day=datetime.datetime.strptime(emp['Date'], '%d.%m.%Y').date()
        year=(today-day).days//365
        if year>10:
            rate=0.07
        else:
            rate=0.05
        new_salary=emp['Salary']*(rate+1)
        print(f'Новая зарплата {emp['Name']:new_salary}')

def vacation_bonus(emp_list):
    voc=[]
    today = datetime.date.today()
    for emp in emp_list:
        data=datetime.datetime.strptime(emp['Date'], '%d.%m.%Y').date()
        months=(today-data).days//30
        if months>6:
            voc.append(emp['Name'])
    return voc
print('Премии')
programmers_bonus(employees)
print('Индексация')
index_bonus(employees)
print('Отпуск')
vacation_bonus(employees)


