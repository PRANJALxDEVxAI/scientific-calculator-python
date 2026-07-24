import math

# ---------------- BASIC OPERATIONS ---------------- #

def add(current):
    num = float(input("Enter number to add: "))
    result = current + num
    print("Result:", result)
    return result

def subtract(current):
    num = float(input("Enter number to subtract: "))
    result = current - num
    print("Result:", result)
    return result

def multiply(current):
    num = float(input("Enter number to multiply: "))
    result = current * num
    print("Result:", result)
    return result

def divide(current):
    num = float(input("Enter number to divide: "))
    if num != 0:
        result = current / num
        print("Result:", result)
        return result
    else:
        print("Error: Division by zero")
        return current


# ---------------- SCIENTIFIC OPERATIONS ---------------- #

def sine(current):
    result = math.sin(math.radians(current))
    print("sin(", current, ") =", result)
    return result

def cos(current):
    result = math.cos(math.radians(current))
    print("cos(", current, ") =", result)
    return result

def tan(current):
    result = math.tan(math.radians(current))
    print("tan(", current, ") =", result)
    return result

def cosec(current):
    sin_val = math.sin(math.radians(current))
    if sin_val != 0:
        result = 1 / sin_val
        print("cosec(", current, ") =", result)
        return result
    else:
        print("Error: Undefined")
        return current

def sec(current):
    cos_val = math.cos(math.radians(current))
    if cos_val != 0:
        result = 1 / cos_val
        print("sec(", current, ") =", result)
        return result
    else:
        print("Error: Undefined")
        return current

def cot(current):
    tan_val = math.tan(math.radians(current))
    if tan_val != 0:
        result = 1 / tan_val
        print("cot(", current, ") =", result)
        return result
    else:
        print("Error: Undefined")
        return current


# ---------------- MATH FUNCTIONS ---------------- #

def square_root(current):
    if current >= 0:
        result = math.sqrt(current)
        print("sqrt(", current, ") =", result)
        return result
    else:
        print("Error: Negative number")
        return current

def power(current):
    exp = float(input("Enter exponent: "))
    result = current ** exp
    print(current, "^", exp, "=", result)
    return result

def log(current):
    if current > 0:
        result = math.log(current)
        print("log(", current, ") =", result)
        return result
    else:
        print("Error: Invalid input")
        return current

def factorial(current):
    if current >= 0 and current == int(current):
        result = math.factorial(int(current))
        print("factorial(", int(current), ") =", result)
        return result
    else:
        print("Error: Invalid input")
        return current


# ---------------- CONSTANTS ---------------- #

def pi():
    return math.pi

def euler():
    return math.e


# ---------------- MAIN PROGRAM ---------------- #

def main():
    current = 0

    while True:
        try:
            current = float(input("Enter starting number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")

    while True:
        print("\nCurrent Value:", current)

        op = input(
            "Enter operation (+ - * / sin cos tan cosec sec cot sqrt power log fact pi e euler quit clear): ").lower()

        if op == "quit":
            print("Goodbye!")
            break

        elif op == "clear":
            current = 0
            print("Cleared")

        elif op == "+":
            current = add(current)

        elif op == "-":
            current = subtract(current)

        elif op == "*":
            current = multiply(current)

        elif op == "/":
            current = divide(current)

        elif op == "sin":
            current = sine(current)

        elif op == "cos":
            current = cos(current)

        elif op == "tan":
            current = tan(current)

        elif op == "cosec":
            current = cosec(current)

        elif op == "sec":
            current = sec(current)

        elif op == "cot":
            current = cot(current)

        elif op == "sqrt":
            current = square_root(current)

        elif op == "power":
            current = power(current)

        elif op == "log":
            current = log(current)

        elif op == "fact":
            current = factorial(current)

        elif op == "pi":
            current = math.pi
            print("Result:", current)

        elif op == "euler":
            current = math.e
            print("Result:", current)

        else:
            print("Invalid operation")


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    main()