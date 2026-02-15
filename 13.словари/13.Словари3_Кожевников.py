caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
check="matcha"
try:
    print(caffeine_level[check])
except KeyError:
    print('That key doesn`t exist')