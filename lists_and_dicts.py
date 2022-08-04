def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Fabricio", "lastname": "Quintas"}

    super_list = [
        {"firstname": "Fabricio", "lastname": "Quintas"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "García"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    # Take key and values of the super_dict
    for key, value in super_dict.items():
        # Print them, separated with a '-'
        print(key, "-", value)

    # Take the values in super_list (dicts)
    for values in super_list:
        # Then print 'firstname' and 'lastname' separated by a space
        print(values["firstname"], values["lastname"])


if __name__ == '__main__':
    run()