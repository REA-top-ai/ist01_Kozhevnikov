import random
def get_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def start():
    admin_number = random.randint(1, 9)
    print(f"Число администрации: {admin_number}")
    winners_count=0
    current=1
    while winners_count<5:
        if get_sum_of_digits(current)% admin_number==0:
            print(f'Победил билет {current}')
            winners_count+=1
        current+=1
        if current>=10000:
            break
start()