def run():
    ## Without list Comprehension
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # print(squares)

    # An comprehension, where make the potencial of a number, when its not divisble by 3
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    # Reto:
        # Crear, con un list comprehension, una lista de todos los múltiplos de 4 que a la vez también son múltiplos de 6 y de 9, hasta 5 dígitos.

    # In this case, in a range from 1 to 9999
    # Where the conditional is true, means that is multiple of 4, 6 and 9.
    squares2 = [i for i in range(1, 10000) if i % 36 == 0]
    print(squares2)
            

if __name__ == '__main__':
    run()