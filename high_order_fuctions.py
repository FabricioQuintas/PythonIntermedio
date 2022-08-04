from functools import reduce

def run():
    # Filter
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list(filter(lambda x: x%2 != 0, my_list))

    print(odd)

    # Map
    my_list2 = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, my_list2))

    print(squares)

    # Reduce
    my_list3 = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a, b: a*b, my_list3)

    print(all_multiplied)

if __name__ == '__main__':
    run()