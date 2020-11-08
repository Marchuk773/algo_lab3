from utils import find, cross_product


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
    numbers_dictionary = {}
    tribes_counter = 0
    union_list, tribes_marker, boys_list, girls_list = [], [], [], []
    counter = 0
    
    def get(index):
        return numbers_dictionary[index]
    
    def check_gender(number, tribe):
        if number % 2 == 1:
            boys_list[tribe] += 1
        elif number % 2 == 0:
            girls_list[tribe] += 1
    
    def add_to_tribe(member, newcomer):
        current_tribe = find(union_list, tribes_marker[get(member)])
        tribes_marker[get(newcomer)] = current_tribe
        check_gender(newcomer, current_tribe)
    
    def unite_tribes(bigger_number, smaller_number):
        actual_tribe = tribes_marker[get(bigger_number)]
        removed_tribe = tribes_marker[get(smaller_number)]
        tribes_marker[get(smaller_number)] = actual_tribe
        union_list[removed_tribe] = actual_tribe
        girls_list[actual_tribe] += girls_list[removed_tribe]
        girls_list[removed_tribe] = 0
        boys_list[actual_tribe] += boys_list[removed_tribe]
        boys_list[removed_tribe] = 0
    
    with open(filename, 'r') as file:
        rows_number = int(file.readline())
        
        for i in range(rows_number + 1):
            tribes_marker.append(0)
            tribes_marker.append(0)
            boys_list.append(0)
            girls_list.append(0)
            union_list.append(i)
        
        for line in file:
            pair = line.split()
            first_number = int(pair[0])
            second_number = int(pair[1])
            
            if first_number not in numbers_dictionary:
                numbers_dictionary[first_number] = counter
                counter += 1
            
            if second_number not in numbers_dictionary:
                numbers_dictionary[second_number] = counter
                counter += 1
            
            first_tribe = tribes_marker[get(first_number)]
            second_tribe = tribes_marker[get(second_number)]
            
            if first_tribe == 0 and second_tribe == 0:
                tribes_counter += 1
                tribes_marker[get(first_number)] = tribes_counter
                tribes_marker[get(second_number)] = tribes_counter
                check_gender(first_number, tribes_counter)
                check_gender(second_number, tribes_counter)
            
            elif first_tribe == 0 and second_tribe != 0:
                add_to_tribe(second_number, first_number)
            
            elif first_tribe != 0 and second_tribe == 0:
                add_to_tribe(first_number, second_number)
            
            elif first_tribe != 0 and second_tribe != 0:
                if first_tribe == second_tribe:
                    continue
                elif first_tribe > second_tribe:
                    unite_tribes(first_number, second_number)
                else:
                    unite_tribes(second_number, first_number)
    
    return cross_product(girls_list, boys_list, tribes_counter)


if __name__ == '__main__':
    import doctest
    import time
    
    doctest.testmod(verbose=True)
    
    start_time = time.time()
    print(f'\n{solve("wedd6.txt")} combinations for 10K unique lines')
    print(f'10K lines file running time is {time.time() - start_time} seconds')
