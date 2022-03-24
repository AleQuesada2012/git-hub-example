print("Hello world!")

#diferentes funciones
def suma (valor1, valor2):
    try:
        result  = valor1 + valor2
        print("Resultado de la suma: " + str(result))
        return result
    except:
        print("los valores deben ser tipos numéricos que se puedan sumar")
    return 0

def resta (valor1, valor2):
    try:
        result = valor1 - valor2
        print("Resultado de la resta: " + str(result))
        return result
    except:
        print("Los valores deben ser tipos numéricos que se puedan restar")
    return 0

def multi ( valor1, valor2):
    try:
        result = valor1 * valor2
        print("Resultado de la multiplicación: " + str(result))
        return result
    except:
        print ("Los valores deben ser tipos numéricos que se puedan multiplicar")
    return 0

def producto_punto(vector1, vector2):
    try:
        # asumiendo que los dos vectores sean del mismo largo
        result = 0
        for i in range(len(vector1)):
            result += (vector1[i] * vector2[i])
        print(result)
        return  result
    except:
        print("Los valores de entrada deben ser listas de una dimensión y del mismo largo")
    return 0

# Valores de prueba
TestVec1 = [1, 5, 8, 10]
TestVec2 = [-1, 50, 20, 2]

#invocaciones de prueba
suma(10, -50)
resta(-5, -5)
multi(7, 3)
a = multi (5, 8) + producto_punto(testVec1, testVec2) #Primera línea agregada en esta modificación del archivo
print(a)                                              #Segunda línea agregada en esta modificación del archivo
producto_punto(TestVec1, TestVec2)
