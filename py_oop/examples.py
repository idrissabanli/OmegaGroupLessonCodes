from datetime import datetime




# class Library:
#     books = []

#     def __add__(self, new_book):
#         self.books.append(new_book)

    # def __repr__(self):
    #     print('repr ise dusdu')
    #     return ",".join(self.books)

    # def __str__(self):
    #     print('str ise dusdu')
    #     return ",".join(self.books)

    # def __sub__(self, value):
    #     self.books.remove(value)

# l = Library()

# print(l.books)

# l + 'Sefiller'
# l + 'Cinayet ve ceza'
# print(l)

# l - "Sefiller"
# print(l)

# class Integer:
    
#     def __init__(self, value):
#         self.value = int(value)

#     def __repr__(self):
#         return f"{self.value}"

#     def __str__(self):
#         return f"{self.value}"

    # def __add__(self, new_value):
    #     return self.value + new_value


# a = Integer(5)
# b = a + 5

# print(b)
# print(a)

# print(isinstance("5", str))

# class MyModel():

#     def __repr__(self,):



# class Employee:
#     working_times = '10:00 - 18:00' # static

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     @classmethod
#     def change_working_times(cls, new_time):
#         cls.working_times = new_time

#     @classmethod
#     def test_classmethod(cls):
#         cls.f_name = 'Idris'

#     @classmethod
#     def get_emp_from_str(cls, emp_data):
#         first_n, last_n, age = emp_data.split('/')
#         return cls(first_n, last_n, age)

#     @staticmethod
#     def print_working_times():
#         print("10")
        

# Employee.print_working_times()

# emp1 = Employee(first_name="Murad", last_name="Rustemzade", age=27)

# Employee.test_classmethod()

# print(emp1.f_name)

# emp2 = Employee(first_name="Idris", last_name="Shabanli", age=25)

# print(emp2.working_times) # '10:00 - 18:00'
# print(emp2.first_name)

# print(emp2.f_name)

# # employee_data = input("Zehmet olmasa ad/soyad/yas daxil edin!") # Murad/Rustemzade/27

# # emp1 = Employee.get_emp_from_str(employee_data)

# # print(emp1.first_name)

# # Employee.working_times = "11:00 - 19:00"
# # Employee.change_working_times("11:00 - 19:00")

# # emp1 = Employee(first_name="Murad", last_name="Rustemzade", age=27)

# # print(emp1.working_times) # "11:00 - 19:00"
# # print(emp1.first_name)

# # emp2 = Employee(first_name="Idris", last_name="Shabanli", age=25)

# # print(emp2.working_times) # '10:00 - 18:00'
# # print(emp2.first_name)


