class Human:
    first_name = 'Murad'
    last_name = 'Rustemzade'
    __age = 27
    _heigth = 180

    def run(self):
        print("I am running")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.__age:
            raise ValueError('Age can not be nagative')
        self.__age = value


class Employee(Human):
    
    def __init__(self, department):
        self.department = department
    
    def work(self):
        print("I am working")


class Programmer(Employee):
    pass
    
    def __init__(self): # override, 
        super().__init__("IT")


murad = Programmer()

print(murad.department)

# print(murad.age)

# murad.age = murad.age + 26

# print(murad.age)

# print(f"my name is {murad.first_name} {murad.last_name}")
# murad.work()