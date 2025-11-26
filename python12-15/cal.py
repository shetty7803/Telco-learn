import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculator(a, b, operation):
    logging.info(f"Calculator called with a={a}, b={b}, operation='{operation}'")

    try:
        if operation == "+":

            if a == 0 or b == 0:
                logging.warning("Addition performed with zero value")
                print("Warning : Addition performed with zero value")

            result = a + b
            logging.info(f"Addition successful: {a} + {b} = {result}")
            return result

        elif operation == "-":

            if a == 0 or b == 0:
                logging.warning("Subtraction performed with zero value")
                print("Warning : Subtraction performed with zero value")

            result = a - b
            logging.info(f"Subtraction successful: {a} - {b} = {result}")
            return result

        elif operation == "*":
            result = a * b
            logging.info(f"Multiplication successful: {a} * {b} = {result}")
            return result

        elif operation == "/":
            if b == 0:
                logging.error("Division by zero attempted!")
                raise ZeroDivisionError("Cannot divide by zero!")

            result = a / b
            logging.info(f"Division successful: {a} / {b} = {result}")
            return result

        else:
            logging.error("Invalid operation selected")
            raise ValueError("Invalid operation")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    except ValueError:
        print("Error: Invalid operation!")
    except Exception:
        print("Unexpected Error occurred!")

print("------ Simple Calculator ------")
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    result = calculator(a, b, operation)

    if result is not None:  
        print("Result =", result)

except ValueError:
    print("Please enter valid numbers!")
except Exception as e:
    print("Unexpected Error:", e)
