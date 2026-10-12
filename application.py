def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    if not isinstance((a or b),int):
        return "Provide an integer number"
    return a * b
