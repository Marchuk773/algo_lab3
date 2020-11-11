def cross_product(girls_list, boys_list, tribes_counter):
    """
    >>> cross_product([0, 1, 2, 3], [0, 1, 0, 3], 3)
    14
    """
    duplicates_number, girls_number, boys_number = 0, 0, 0
    for i in range(1, tribes_counter + 1):
        girls_number += girls_list[i]
        boys_number += boys_list[i]
        duplicates_number += girls_list[i] * boys_list[i]
    
    return (girls_number * boys_number) - duplicates_number


def find(union_list, index):
    """
    >>> find([0, 1, 2, 4, 5, 1], 3)
    1
    """
    if union_list[index] != index:
        union_list[index] = union_list[union_list[index]]
        return find(union_list, union_list[index])
    return index


if __name__ == '__main__':
    import doctest
    
    doctest.testmod(verbose=True)
