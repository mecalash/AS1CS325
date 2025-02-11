def Evilnelly_decorator(func):
    def wrapper(*args):
        print("Nelly why are you scratching me?")
        func(*args)
        print(" Noooo my sweet kitty!!")## result)
        ##return result
    return wrapper

@Evilnelly_decorator
def greet(name):
    print("Meow!" " I am evil and I am "+name+"!")

greet("Nelly")