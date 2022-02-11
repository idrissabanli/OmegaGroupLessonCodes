
class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return self.a / self.b

# print(__name__)
if __name__ == '__main__':
    print(add(1, 5))

    