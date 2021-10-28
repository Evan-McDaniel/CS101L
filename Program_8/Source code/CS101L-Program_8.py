import math

def menu():
    print()
    print('{:^15}'.format('Grade menu'))
    print('1 -Add Test\n'
    '2 -Remove Test\n'
    '3 -Clear Tests\n'
    '4 -Add Assignment\n'
    '5 -Remove Assignment\n'
    '6 -Clear Assignments\n'
    'D -Display Scores\n'
    'Q -Quit')
    print()
    user_val = input('==>').upper()
    while user_val not in ['1','2','3','4','5','6','D','Q']:
        user_val = input('Please enter valid value==>').upper()
    print()
    return user_val

def add(lst,word):
    score = int(input('Enter the new {} score 0-100 ==>'.format(word)))
    while score < 0:
        score = int(input('please enter a score greater than 0 ==>'))
    lst.append(score)
    return lst

def remove(lst,word):
    test = int(input('Enter the {} to remove 0-100 ==>'.format(word)))
    if test not in lst:
        print('Could not find that score to remove')
    else:
        lst.remove(test)
        return lst

def display(assignments,tests):
    print('{:<20}{:<7}{:<8}{:<7}{:<8}{:>4}'.format('Type','#','min','max','avg','std'))
    print('='*55)
    if tests == []:
        print('{:<20}{:<7}{:<8}{:<7}{:<8}{:>4}'.format('Tests',0, 'n/a','n/a','n/a', 'n/a'))
    else:
        print('{:<20}{:<7}{:<8}{:<7}{:<8.2f}{:>4.2f}'.format('Tests',len(tests), min(tests),max(tests),sum(tests)/len(tests), std(tests)))
    if assignments == []:
        print('{:<20}{:<7}{:<8}{:<7}{:<8}{:>4}'.format('Assignments',0, 'n/a','n/a','n/a', 'n/a'))
    else:
        print('{:<20}{:<7}{:<8}{:<7}{:<8.2f}{:>4.2f}'.format('Assignemnts',len(assignments), min(assignments),max(assignments),sum(assignments)/len(assignments), std(assignments)))
    print()
    print('Weighted scores is {}'.format(weighted(assignments,tests)))

def avg(lst):
    try:
        lst2 = sum(lst)/len(lst)
        return lst2
    except ZeroDivisionError:
        return 0

def std(lst):
    lst2 = [math.pow(i-avg(lst),2) for i in lst]
    return math.sqrt(sum(lst2)/4)

def weighted(assignments, tests):
    return avg(assignments)*.4 + avg(tests)*.6
            

assignments = []
tests = []
val = 1
while val != 'Q':
    val = menu()
    if val == '1':
       add(tests,'Test')
    elif val == '2':
        remove(tests,'Test')
    elif val == '3':
        tests.clear()
    elif val == '4':
        add(assignments,'Assignment')
    elif val == '5':
        remove(assignments,'Assignment')
    elif val == '6':
        assignments.clear()
    elif val == 'D':
        display(assignments,tests)
    elif val == 'q':
        continue
