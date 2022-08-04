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

    num = input("Ingresa un número: ")
    # Assert statement
    assert num.isnumeric() and num > 0, 'Ingresa sólo numeros positivos'
    print(divisors(num))
    print("Terminó mi programa")

if __name__ == '__main__':
    run()