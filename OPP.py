class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")

e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()

----------------

class Admin(Employee):
    pass

e3 = Admin()
e3.say_id()

-----------------

class Admin(Employee):
    def say_id(self):
        print("I am an Admin")

e3 = Admin()
e3.say_id()

-------------------

class Admin(Employee):
    def say_id(self):
        super().say_id()
        print("I am an Admin")

e3 = Admin()
e3.say_id()

------------------

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am in charge")

e4 = Manager()
e4.say_id()

----------------

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"My username is {self.username} and my role is {self.role}")

class Admin(Employee, User):
    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        super().say_id()
        print("I am an Admin")

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am in charge")

e3 = Admin()
e3.say_user_info()

---------------

meeting = [Employee(), Admin(), Manager()]

for attendee in meeting:
    attendee.say_id()

--------------

class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        self.attendees.append(employee)
        print(f"Added attendee with id {employee.id}")
        return self

    def __len__(self):
        return len(self.attendees)

m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))

-----------

from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class Employee(AbstractEmployee):
    def say_id(self):
        print(f"My id is {self.id}")

abstract_e1 = Employee()
abstract_e1.say_id()

----------------

class Employee:
    def __init__(self):
        self.id = 1
        self._id = "single underscore"
        self.__id = "double underscore"

e = Employee()
print(dir(e))