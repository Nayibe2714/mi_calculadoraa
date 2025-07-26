def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

def elevar_al_cubo(a):
    return a ** 3

print("Calculadora en Python")
print("Opciones:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Elevar al cubo") 

opcion = input("Elige una opción (1/2/3/4/5): ")

if opcion == '5':
    num = float(input("Ingresa el número que deseas elevar al cubo: "))
    print("Resultado:", elevar_al_cubo(num))

else:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))    


    if opcion == '1':
     print("Resultado:", sumar(num1, num2))
    elif opcion == '2':
     print("Resultado:", restar(num1, num2))
    elif opcion == '3':
     print("Resultado:", multiplicar(num1, num2))
    elif opcion == '4':
     print("Resultado:", dividir(num1, num2))
    else:
     print("Opción inválida.")