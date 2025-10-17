#decoraters

def greet(fx):
    def mfx(*args, **kwargs):
        print("Let's run this function")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

def hello():
    print("hello world")

@greet
def add(a, b):
    print(a+b)

greet(hello)()
add(1,2)