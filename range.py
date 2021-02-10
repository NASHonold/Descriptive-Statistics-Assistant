


def list_from_string(string):
    if string == False:
        return False
    good_list = ['0','1','2','3','4','5','6','7','8','9','.']
    a_list = []
    final_index = len(string)
    working_string = ''
    
    for index in range(final_index):
        if string[index] in good_list:
            working_string += string[index]
        if string[index] not in good_list or index == (final_index - 1):
            if len(working_string) == 1:
                if working_string == '.':
                    working_string = ''
            if len(working_string) > 0:
                a_list.append(float(working_string))
                working_string = ''
        
    a_list.sort()
    print(a_list)
    return a_list


       
            
def get_data_set():
    run = True
    string = ''
    while run:
        data_set = input('Copy and paste or enter data set here: ')
        string += data_set
        
        if data_set.lower() == 'd':
            run = False
        string += ' '
        if data_set == 'q':
            run = False
            return False
    return string
print(list)


# list = [125.0, 254.0, 119.0, 186.0, 185.0, 139.0, 186.0, 204.0, 166.0, 
# 170.0, 203.0, 170.0, 177.0, 190.0, 139.0, 189.0, 165.0, 192.0, 156.0, 
# 151.0, 141.0, 114.0, 185.0, 153.0, 176.0, 286.0, 143.0, 219.0, 196.0, 
# 162.0]

def getRange(list):
    max_value = list[0]
    min_value = list[0]
    print(max_value)
    print(min_value)
    for index in list:
        if min_value >= index:
            min_value = index
        if max_value <= index:
            max_value = index

    range = max_value - min_value
    print('Your total range is {}'.format(range))
    return range, min_value, max_value


def getClassWidth(range, class_num):
    return range / class_num

def createClassBoundryList(graph_start,class_width, number):
    boundaries = []
    boundaries.append(graph_start)
    print(class_width)
    for i in range(number):
        var = boundaries[-1] + class_width
        boundaries.append(var)
    return boundaries

def build_graph(sorted_list, boundary_list):
    sorted_list.sort()
    number = len(boundary_list) - 1
    master_list = []
    for i in range(number):
        sublist = []
        for x in sorted_list:
            if x >= boundary_list[i] and x < boundary_list[i+1]:
                sublist.append(x)
            if x > boundary_list[i+1]:
                break
        master_list.append(sublist)
        print('For the class {} to {}'.format(boundary_list[i],boundary_list[i+1] ))
        print('Frequency is {}'.format(len(sublist)))
        print("Relative Frequency for this class is {}".format(len(sublist)/len(list)).format('.4f'))
        print(*sublist, sep=',')
        print('--------------------')
    print(master_list)


#===============================================================
class_num = int(input('How many classes would you like in your data?:'))



data_list = list_from_string(get_data_set())
total_range, min, max = getRange(data_list)
class_width = getClassWidth(total_range, class_num)
print('The class width is ' + str(class_width))
print('min is {} and max is {}'.format(min, max))

print('Your calculated class width is {}. Type in your desired class width below.\n'.format(class_width),
    '(If you want it to stay the same then just type the claculated value)')
class_width = float(input('Enter Desired Width Here: '))

print('Your current minimum value in your data set is {}'.format(min))
graph_start = float(input('Enter your desired starting point: '))



class_boundaries = createClassBoundryList(graph_start,class_width,class_num)


        

# print('The boundaries of your graph are the folling values:')
# print(*class_boundaries,sep=',')
# list.sort()
# print(*list, sep='\n')

build_graph(data_list,class_boundaries)










