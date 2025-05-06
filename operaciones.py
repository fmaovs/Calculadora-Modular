def Resta(a,b):
    try:
        resta = a - b
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        print("Result:", resta)


def Division(a,b):
    try:
        division = a / b
    except ValueError:
        print("Invalid input.")
    except ZeroDivisionError:
        print("Can't divide by zero.")
    else:
        print("Result: ", division)

def DivisionEntera(a,b):
    try:
        division = a // b
    except ValueError:
        print("Invalid input.")
    except ZeroDivisionError:
        print("Can't divide by zero.")
    else:
        print("Result: ", division)

def Potencia(a,b):
    try:
        result= a**b
    except ValueError:
        print("Invalid input.")
    else:
        print("Result: ", result)

"_____________________________________________"

def Suma(a,b):
    try:
        suma = a + b
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        print("Result:", suma)


def Multiplicacion(a,b):
    try:
        multiplicacion = a * b
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        print("Result:", multiplicacion)
