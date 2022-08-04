def run():
    # my_dict = {}

    ## In a range of 1 to 100, all values that are not divisible by 3:
    ## Make it, the potencial of 3 and save it
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3
    
    # The same as the comment one, but in a dict comprehension.
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # Print it
    print(my_dict)

    # Reto:
        # Crear un diccionario, cuyas llaves sean los 1000 primeros números
        # naturales con sus raíces cuadradas como valor.

    # I used an comprehension, rounding the result number for 2 decimals
    my_new_dict = {i: round(i**0.5, 2) for i in range(1, 1001)}
    # And print it
    print(my_new_dict)

if __name__ == '__main__':
    run()