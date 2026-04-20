import functools

#декоратор is alive
def is_alive(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.health <= 0:
            print(f"{self.name} мертв и не может действовать!")
            return None
        return func(self, *args, **kwargs)
    return wrapper

#декоратор log action
def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Начало действия: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Действие завершено")
        return result
    return wrapper

class Hero:
    def __init__(self,name, hero_class):
        self.name = name
        self.hero_class = hero_class.lower()

        if self.hero_class == 'воин':
            self.health = 100
            self.mana = 10
        else:
            self.health = 60
            self.mana = 50

        self.spells_names = {}
        self.items = {}

    
    @is_alive
    def attack(self, damage):
        print(f"Герой нанес урон: {damage}")

    @log_action
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} восстановил {amount} здоровья. Текущее HP: {self.health}")

    
    @is_alive
    def cast_spell(self, spell_name):
        if spell_name in self.spells_names:
            cost = self.spells_names[spell_name]['mana_cost']
            if self.mana >= cost:
                self.mana -= cost
                print(f"Герой применяет заклинание: {spell_name}")
            else:
                print("Недостаточно маны!")
        else:
            print(f"Заклинание {spell_name} не изучено.")

    def add_spell(self, spell_name, mana_cost, attack_damage, health_increase):
        self.spells_names[spell_name] = {
            'mana_cost': mana_cost,
            'attack_damage': attack_damage,
            'health_increase': health_increase
        }

    def add_item(self, item_name, parameter, value):
        if len(self.items) < 6:
            self.items[item_name] = {parameter: value}
            if parameter == 'здоровье':
                self.health += value
            elif parameter == 'мана':
                self.mana += value
            print(f"Предмет {item_name} добавлен.")
        else:
            print("Инвентарь полон!")




#Самостоятельная работа
#двойное здоровья
def double_health(func):
    def wrapper(hero, *args, **kwargs):
        original_health = hero.health
        hero.health *= 2
        print(f"Здоровье {hero.name} увеличено вдвое: {original_health} -> {hero.health}")
        result = func(hero, *args, **kwargs)
        hero.health = original_health
        print(f"Здоровье {hero.name} восстановлено: {hero.health}")
        return result
    return wrapper

#увеличение маны
def mana_increase(func):
    def wrapper(hero, *args, **kwargs):
        original_mana = hero.mana
        hero.mana = int(hero.mana * 1.5)
        print(f"Мана {hero.name} увеличена в 1.5 раза: {original_mana} -> {hero.mana}")
        result = func(hero, *args, **kwargs)
        hero.mana = original_mana
        print(f"Мана {hero.name} восстановлена: {hero.mana}")
        return result
    return wrapper

#священный посох

def sacred_staff_for_mage(func):
    def wrapper(hero, *args, **kwargs):
        original_mana = hero.mana
        if hero.hero_class.lower() == "волшебник":
            hero.mana += 5
            print(f"[EVENT] Священный посох! Мана {hero.name} увеличена на 5: {original_mana} -> {hero.mana}")
        result = func(hero, *args, **kwargs)
        if hero.hero_class.lower() == "волшебник":
            hero.mana = original_mana
            print(f"[EVENT] Священный посох перестал действовать. Мана {hero.name} восстановлена: {hero.mana}")
        return result
    return wrapper


#свой декоратор(будет ограничивать количество использованных способностей за игру)

def limit_use(max_use):
    def dec(func):
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, 'use_counter'):
                self.use_counter={}
            if func.__name__ not in self.use_counter:
                self.use_counter[func.__name__]=0

            if self.use_counter[func.__name__]>=max_use:
                print(f"[LIMIT] {self.name} не может исользовать {func.__name__} (лимит использований: {max_use})")
                return None
            self.use_counter[func.__name__] +=1
            print(f"[LIMIT] {self.name} использует {func.__name__}")
            return func(self, *args, **kwargs)
        return wrapper
    return dec

