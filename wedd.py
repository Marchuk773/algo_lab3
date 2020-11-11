from utils import find, cross_product


class Wedd():
    
    def __init__(self, filename):
        self.filename = filename
        self.any_to_2n = {}
        self.tribes_counter = 0
        self.counter = 0
        self.union_list, self.tribes_marker = [], []
        self.boys_list, self.girls_list = [], []
        
        with open(filename, 'r') as file:
            for i in range(int(file.readline()) + 1):
                self.tribes_marker.append(0)
                self.tribes_marker.append(0)
                self.boys_list.append(0)
                self.girls_list.append(0)
                self.union_list.append(i)
    
    def calculate_result(self):
        with open(self.filename, 'r') as file:
            next(file)
            
            for line in file:
                pair = line.split()
                first_number = int(pair[0])
                second_number = int(pair[1])
                
                self.add_to_2n_dict(first_number)
                self.add_to_2n_dict(second_number)
                
                first_tribe = self.tribes_marker[self.get_2n(first_number)]
                second_tribe = self.tribes_marker[self.get_2n(second_number)]
                
                if first_tribe == 0 and second_tribe == 0:
                    self.create_tribe(first_number, second_number)
                
                elif first_tribe == 0 and second_tribe != 0:
                    self.add_to_tribe(second_number, first_number)
                
                elif first_tribe != 0 and second_tribe == 0:
                    self.add_to_tribe(first_number, second_number)
                
                elif first_tribe != 0 and second_tribe != 0:
                    if first_tribe != second_tribe:
                        if first_tribe > second_tribe:
                            self.unite_tribes(first_number, second_number)
                        else:
                            self.unite_tribes(second_number, first_number)
        
        return cross_product(self.girls_list, self.boys_list, self.tribes_counter)
    
    def get_2n(self, index):
        return self.any_to_2n[index]
    
    def add_to_2n_dict(self, number):
        if number not in self.any_to_2n:
            self.any_to_2n[number] = self.counter
            self.counter += 1
    
    def separate_genders(self, number, tribe):
        if number % 2 == 1:
            self.boys_list[tribe] += 1
        else:
            self.girls_list[tribe] += 1
    
    def add_to_tribe(self, member, newcomer):
        current_tribe = find(self.union_list, self.tribes_marker[self.get_2n(member)])
        self.tribes_marker[self.get_2n(newcomer)] = current_tribe
        self.separate_genders(newcomer, current_tribe)
    
    def unite_tribes(self, bigger_number, smaller_number):
        actual_tribe = self.tribes_marker[self.get_2n(bigger_number)]
        removed_tribe = self.tribes_marker[self.get_2n(smaller_number)]
        self.tribes_marker[self.get_2n(smaller_number)] = actual_tribe
        self.union_list[removed_tribe] = actual_tribe
        self.girls_list[actual_tribe] += self.girls_list[removed_tribe]
        self.girls_list[removed_tribe] = 0
        self.boys_list[actual_tribe] += self.boys_list[removed_tribe]
        self.boys_list[removed_tribe] = 0
    
    def create_tribe(self, first_number, second_number):
        self.tribes_counter += 1
        self.tribes_marker[self.get_2n(first_number)] = self.tribes_counter
        self.tribes_marker[self.get_2n(second_number)] = self.tribes_counter
        self.separate_genders(first_number, self.tribes_counter)
        self.separate_genders(second_number, self.tribes_counter)
