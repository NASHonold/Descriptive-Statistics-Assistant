run = True
count = 1
data_list = []
label_list =[]



def addValues(list):
        total = 0
        for dat in list:
            total = total + dat
        return total

def getPercentage(total, portion):
    percent = portion / total * 100
    return format(percent, '.2f')

def printValues(data_list, label_list, total):
    count = 0
    for data in data_list:
        percent = getPercentage(total, data) 
        print('Label: {},   Data: {} ,  Total Percentage: {},   Relative Frequency: {}'.format(label_list[count],data, percent, 
        (str(data / total)).format('.4f')))
        count += 1


print('Input the values on the bar graph you have from left to right',
'\nWhen you are done with inputs type d for done\n\n')



while run:
    name = input('Name of field: ')
    data = input('Data point {}:'.format(count))
    if data != 'd' or name != 'd':
        label_list.append(name)
        data_list.append(float(data))
        count += 1
    else:
        run = False

print('The total items on graph are {}'.format(addValues(data_list)))
printValues(data_list, label_list,addValues(data_list))
    
        
