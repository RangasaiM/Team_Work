import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add(a, b):
    return a + b

def subtract(a, b):
    return(a-b)

def multiply(a, b):
    return a*b

def divide(a, b):
    return (a/b)


def modulus(a, b):
    pass


def calculator():
    print("\nWelcome to the Team Calculator!")
    a, b = get_input()  # Taking input for `a` and `b`
    print(f"Values received: a = {a}, b = {b}")
    print(f"addition{add(a, b)}")
    print(f"substraction{subtract(a, b)}")
    print(f"Multiplication{multiply(a,b)}")
    print(f"division{divide(a,b)}")
    
    

if __name__ == "__main__":
    calculator()