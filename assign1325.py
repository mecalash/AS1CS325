def nelly_decorator(func):
    def wrapper(*args):
        print("Nelly are you cute?")
        func(*args)
        print("Awwww that is my girl!")## result)
        ##return result
    return wrapper

@nelly_decorator
def greet(name):
    print("Meow!" " Hello I am "+name+"!")

greet("Nelly")