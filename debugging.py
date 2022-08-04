def divisors(num):
    # Made it in list comprehension
    divisors = [i for i in range(1, num+1) if num % i == 0]
    # for i in range(1, num+1):
    #     if num % i == 0:
    #         divisors.append(i)
    return divisors

# Reto:
    # Utiliza las palabras clave try, except y raise
    # para elevar un error si el usuario ingresa un número
    # negativo en nuestro programa de divisores

def run():
    try:
        num = int(input("Ingresa un número: "))
        if num <= 0:
            raise Exception('El número debe ser mayor a 0')
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    run()