#No es la manera mas eficiente de Solucionarlo, 
#funciona como solucion pero no es tampoco la mejor, dejo al final la solucion sugerida por Github Copilot

def convert(number):
    #Si se puede dividir por 3, agregar Pling al resultado
    #Si % 5 = 0, agregar Plang
    # Si La division por 7 da 0 de residuo, agregar Plong al resultado
    # Si no es divisible por 3, 5 o 7. el resultado deberia ser el nombre como String'''
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0 :
        return "PlingPlangPlong"
    elif number % 3 == 0 and number % 5 == 0:
        return "PlingPlang"
    elif number % 3 == 0 and number % 7 == 0:
        return "PlingPlong"
    elif number % 5 == 0 and number % 7 == 0:
        return "PlangPlong"
    elif number % 3 == 0:
        return "Pling"
    elif number % 5 == 0:        
        return "Plang"
    elif number % 7 == 0:
        return "Plong"

    else: return str(number)


"""Copilot:
#Your code is correct, but it can be simplified and made more efficient by reducing the number of conditional checks. 
#Instead of checking all combinations of divisibility, you can build the result string incrementally. 
#Here's a more concise version of your function:
def convert(number):
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result == "":
        result = str(number)
    return result
"""
