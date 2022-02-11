

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero")
    return a / b

# print(__name__)
if __name__ == '__main__':
    print(add(1, 5))

    