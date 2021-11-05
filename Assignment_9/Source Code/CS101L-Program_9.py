import csv
import functools
def month_from_number(num):
    dict = {1:'January', 2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    return dict.get(num,'Enter a valid input')
def read_in_file(name):
    file = open(name, encoding = 'utf-8')
    reader = csv.reader(file)
    lst = []
    for x in reader:
        lst.append(x)
    file.close()
    return lst
def create_reported_date_dict(lst):
    key_list = []
    for x in range(1,len(lst)):
        key_list.append(lst[x][1])
    dict = {}
    for x in key_list:
        if x in dict.keys():
            dict[x] = dict[x]+1
        else:
            dict[x] = 1
    return dict

def create_reported_dict_month(lst):
    key_list = []
    for x in range(1,len(lst)):
        key_list.append(int(lst[x][1][0:2]))
    dict = {}
    for x in key_list:
        if x in dict.keys():
            dict[x] = dict[x]+1
        else:
            dict[x] = 1
    return dict

def create_offense_dict(lst):
    key_list = []
    for x in range(1,len(lst)):
        key_list.append((lst[x][7]))
    dict = {}
    for x in key_list:
        if x in dict.keys():
            dict[x] = dict[x]+1
        else:
            dict[x] = 1
    return dict

def create_offense_by_zip(lst):
    dict = {}
    for x in range(1,len(lst)):
        zip_code = lst[x][13]
        offense = lst[x][7]
        if offense in dict and zip_code in dict[offense]:
            dict[offense][zip_code] += 1
        elif offense in dict and zip_code not in dict[offense]:
            dict[offense][zip_code] = 1
        else:
            dict[offense] = {zip_code:1}
    return dict

if __name__ == '__main__':
    while True:
        try:
            file_name = input('Enter the name of the crime data file ==>')
            file = read_in_file(file_name)
            break
        except FileNotFoundError:
            print('Please enter a valid file')
    print()
    dict_month = create_reported_dict_month(file)
    month,score = functools.reduce(lambda a,b: a if a[1]>b[1] else b, dict_month.items())
    print('The month with the highest # of crimes is {} with {} offenses'.format(month_from_number(month),score))
    offenses = create_offense_dict(file)
    offense,score2 = functools.reduce(lambda a,b: a if a[1]>b[1] else b, offenses.items())
    print('The offense with the highest # of crimes is {} with {} offenses'.format(offense,score2))
    print()
    zip = create_offense_by_zip(file)
    while True:
        try:
            offense_name = input('Enter an offense:')
            if offense_name not in zip:
                raise KeyError
            else:
                break
        except KeyError:
            print('Not a valid offense found, please try again')
    print('{} offenses by Zip code'.format(offense_name))
    print('{:<25}{:>25}'.format('Zip code','# offenses'))
    print('{:=^50}'.format(''))
    for x in zip[offense_name]:
        print('{:<25}{:>25}'.format(x,zip[offense_name][x]))
