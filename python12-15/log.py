import logging
logging.basicConfig(level=logging.INFO)
logging.debug("this is debug")
a=int(input("enter a"))
b=int(input("enter b"))
try:
    div = a / b
    print(f"the result is {div}")
except ZeroDivisionError:
    print("error: it cant be divided by zero")
logging.info("program started")