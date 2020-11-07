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
    
    def get(index):
        return numbers_dictionary[index]
    
    with open(filename, 'r') as file:
        
        tribes_counter = 0
        rows_number = int(file.readline())
        union_list, tribes_marker, boys_list, girls_list = [], [], [], []
        counter = 0
        
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
            
            if tribes_marker[get(first_number)] == 0 and tribes_marker[get(second_number)] == 0:
                
                tribes_counter += 1
                tribes_marker[get(first_number)] = tribes_counter
                tribes_marker[get(second_number)] = tribes_counter
                
                if first_number % 2 == 1:
                    boys_list[tribes_counter] += 1
                elif first_number % 2 == 0:
                    girls_list[tribes_counter] += 1
                
                if second_number % 2 == 1:
                    boys_list[tribes_counter] += 1
                elif second_number % 2 == 0:
                    girls_list[tribes_counter] += 1
            
            elif tribes_marker[get(first_number)] == 0 and tribes_marker[get(second_number)] != 0:
                
                current_tribe = find(union_list, tribes_marker[get(second_number)])
                tribes_marker[get(first_number)] = current_tribe
                
                if first_number % 2 == 1:
                    boys_list[current_tribe] += 1
                elif first_number % 2 == 0:
                    girls_list[current_tribe] += 1
            
            elif tribes_marker[get(first_number)] != 0 and tribes_marker[get(second_number)] == 0:
                
                current_tribe = find(union_list, tribes_marker[get(first_number)])
                tribes_marker[get(second_number)] = current_tribe
                
                if second_number % 2 == 1:
                    boys_list[current_tribe] += 1
                elif second_number % 2 == 0:
                    girls_list[current_tribe] += 1
            
            elif tribes_marker[get(first_number)] != 0 and tribes_marker[get(second_number)] != 0:
                
                if tribes_marker[get(first_number)] == tribes_marker[get(second_number)]:
                    continue
                
                elif tribes_marker[get(first_number)] > tribes_marker[get(second_number)]:
                    bigger_index = tribes_marker[get(first_number)]
                    smaller_index = tribes_marker[get(second_number)]
                    tribes_marker[get(second_number)] = bigger_index
                else:
                    smaller_index = tribes_marker[get(first_number)]
                    bigger_index = tribes_marker[get(second_number)]
                    tribes_marker[get(first_number)] = bigger_index
                
                union_list[smaller_index] = bigger_index
                girls_list[bigger_index] += girls_list[smaller_index]
                girls_list[smaller_index] = 0
                boys_list[bigger_index] += boys_list[smaller_index]
                boys_list[smaller_index] = 0
    
    return cross_product(girls_list, boys_list, tribes_counter)


if __name__ == '__main__':
    import doctest
    import time
    
    doctest.testmod(verbose=True)
    
    start_time = time.time()
    print(f'\n{solve("wedd6.txt")} combinations for 10K unique lines')
    print(f'10K lines file running time is {time.time() - start_time} seconds')
