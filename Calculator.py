import math

def calculator():
    while True:
        print("\n+  -  *  /  power  sqrt  exit")
        op = input("Operation: ")

        if op == "exit":
            break
        elif op == "sqrt":
            x = float(input("Number: "))
            print("Result:", math.sqrt(x))
        else:
            x = float(input("First number: "))
            y = float(input("Second number: "))
            if op == "+":
                print("Result:", x + y)
            elif op == "-":
                print("Result:", x - y)
            elif op == "*":
                print("Result:", x * y)
            elif op == "/":
                print("Result:", x / y)
            elif op == "power":
                print("Result:", x ** y)

calculator()
