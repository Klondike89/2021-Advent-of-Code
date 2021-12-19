from pdb import set_trace as bp

# Input file 
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day8_TEST_input.txt'

##--- Get Data from Input File ---##
testing_data = []
data = []

with open(f,'r') as file:
    for line in file:
        input_data = line.strip().split(' | ')
        testing_data.append(input_data[0].split())
        data.append(input_data[1].split())
        #print(testing_data)        

##--- Part 1 ---##
unique_segments = (2,4,3,7)
count = 0

for data_set in data:
    for node in data_set:
        if len(node) in unique_segments:
            count += 1

print(count)


##--- Reference Info ---##
Pin_Count_Name_Dict = {'2':'One',
                        '3':'Seven',
                        '4':'Four',
                        '5':['Two','Three','Five'],
                        '6':['Zero','Six','Nine'],
                        '7':'Eight'
                        }

Name_Pin_Dict = {'Zero':[0,1,2,4,5,6],
                    'One':[2,5],
                    'Two':[0,2,3,4,6],
                    'Three':[0,2,3,5,6],
                    'Four':[1,2,3,5],
                    'Five':[0,1,3,5,6],
                    'Six':[0,1,3,4,5,6],
                    'Seven':[0,2,5],
                    'Eight':[0,1,2,3,4,5,6],
                    'Nine':[0,1,2,3,5,6]
                    }


##--- Part 2 ---##
def Sorting(lst):
    lst.sort(key=len)
    return lst

def Alpha(elmnt):
    sorted_element_lst = sorted(elmnt)
    sorted_element = "".join(sorted_element_lst)
    return sorted_element

def contains_set(index):
    index = pin_sets[index]
    return element_set.issuperset(index)

def solve_five():
    pin_sets[2].difference_update(element_set)
    pin_sets[5].intersection_update(element_set)
    pin_sets[2].add('solved')
    pin_sets[5].add('solved')

# Do for each line of data. First do test data then data.
for case in range(len(testing_data)):

    # Initialize lists for tracking set
    # Take line of data and sort inputs 
    for node in testing_data:
        pin_posibilities = [[] for x in range(7)]
        pin_sets = [set() for y in range(7)]
        used_pins = []
        element_name_dict = {'Zero':'',
                    'One':'',
                    'Two':'',
                    'Three':'',
                    'Four':'',
                    'Five':'',
                    'Six':'',
                    'Seven':'',
                    'Eight':'',
                    'Nine':''}
        Sorting(node)
        # print(node)

        # Organize each 'input'(element) by counting the pins
        # then reference Pin_Count_Option_Dict to get 
        # possible correct displays
        for element in node:
            name = 'none'
            # print(element)
            pin_count = str(len(element))
            element_name = Pin_Count_Name_Dict.get(pin_count)

            # Starting with Ones, Sevens, Fours, Eights
            # Use process of elimination to find correct pin layout
            if type(element_name) is str:
                display_pos = Name_Pin_Dict.get(element_name)
                if pin_count == '2':
                    element_name_dict[element_name] = element
                    for pin in element:
                        for pos in display_pos:
                            pin_sets[pos].add(pin)
                            used_pins.append(pin)
                elif pin_count == '3':
                    element_name_dict[element_name] = element
                    for pin in element:
                        if pin not in used_pins:
                            pin_sets[0].add(pin)
                            pin_sets[0].add('solved')
                            used_pins.append(pin)
                elif pin_count == '4':
                    element_name_dict[element_name] = element
                    for pin in element:
                        if pin not in used_pins:
                            pin_sets[1].add(pin)
                            pin_sets[3].add(pin)
                            used_pins.append(pin)
                else:
                    element_name_dict[element_name] = element

                
            
            else:
                element_set = {x for x in element}
                if len(element) == 5:
                    if contains_set(2) and not contains_set(3):
                        name = 'Three'
                        element_name_dict[name] = element
                    elif contains_set(1):
                        name = 'Five'
                        element_name_dict[name] = element
                    else:
                        name = 'Two'
                        element_name_dict[name] = element
                    

                elif len(element) == 6:
                    if contains_set(2) and contains_set(1):
                        name = 'Nine'
                        element_name_dict[name] = element
                    elif contains_set(1) and not contains_set(2):
                        name = 'Six'
                        element_name_dict[name] = element
                    else:
                        name = 'Zero'
                        element_name_dict[name] = element

                # print(element)    
        print(element_name_dict); bp()
                # print(name);print(pin_sets);bp()
                    
                        

                    # for pin in name_pin_lst:
                    #     if 'solved' not in pin_sets[pin]:
                    #         print(pin_sets[pin])
                    #         if len(pin_sets[pin]) < 2:
                    #             pin_sets[pin].add(element_set.difference(used_set))
                    #             used_set.add(element_set.difference(used_set))
                    #             print(pin_sets[pin],element_set,used_set);bp()
                    #         if pin_sets[pin].issubset(element_set):
                    #             print(element_set)
                    #             print(pin_sets[pin])
                    #             is_name = True
                    #         else:
                    #             is_name = False
                    #             break
                   

                    






            