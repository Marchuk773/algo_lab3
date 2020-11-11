from wedd import Wedd


def solve(filename):
    """
    >>> solve('wedd1.txt')
    4
    >>> solve('wedd2.txt')
    6
    >>> solve('wedd3.txt')
    6
    >>> solve('wedd4.txt')
    6
    >>> solve('wedd5.txt')
    30
    """
    return Wedd(filename).calculate_result()


if __name__ == '__main__':
    import doctest
    import time
    
    doctest.testmod(verbose=True)
    
    start_time = time.time()
    print(f'\n{solve("wedd6.txt")} combinations for 10K unique lines')
    print(f'10K lines file running time is {time.time() - start_time} seconds')
