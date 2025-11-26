def my_dec(func):
    def decor():
        print("before decorator runs")
        func()
        print("after decorator runs")
    return decor

@my_dec
def greet():
    print("hello")

greet()