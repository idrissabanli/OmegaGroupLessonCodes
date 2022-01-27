class Animal:

    def sound(self):
        print("uuuuuuuuu")


class A:

    def sound(self):
        print('aaaaaaaaaa')


class Dog(Animal, A):
    
    def sound(self):
        super(Animal, self).sound()

dog = Dog()

dog.sound()
