from operaciones import Resta, Potencia, Division, DivisionEntera, Suma, Multiplicacion



try:
    a = int(input('Ingrese el primer valor: '))
    b = int(input('Ingrese el segundo valor: '))
    operacion = input("Ingrese: \n"
                      "- para restar\n"
                      "/ para dividir\n"
                      "// para division entera\n"
                      "** para potencia\n"
                      "+ para sumar\n"
                      "* multiplicacion\n"
                      )
    if operacion == "-":
        Resta(a,b)
    elif operacion == "/":
        Division(a,b)
    elif operacion == "//":
        DivisionEntera(a,b)
    elif operacion == "**":
        Potencia(a,b)
    elif operacion =="+" :
        Suma (a,b)
    elif operacion =="*":
        Multiplicacion (a,b)
    else:print("Error vuelve a intertar")
except ValueError as e:
    print(f"{e}")
