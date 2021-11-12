def open_file():
    invalid_list = ['.','!',',']
    while True:
        try:
            words = []
            name = input('Enter the name of the file to open: ')
            with open(name) as file:
                lines = file.readlines()
            for line in lines:
                for word in line.split():
                    if word[-1] in invalid_list:
                        words.append(word[0:-1].lower())
                    else:
                        words.append(word.lower())
            return words
        except FileNotFoundError:
            print('Could not open file {}'.format(name))
            print('Please try again')

def count_words(lst):
    dct = {}
    for word in lst:
        if len(word) > 3:
            if word not in dct:
                dct[word] = 1
            else:
                dct[word] += 1 
    return dct

def sort(dct):
    dct2 = ({k:v for k,v in sorted(dct.items(),key = lambda item:item[1], reverse = True)})
    return dct2

def occur_once(dct):
    lst = list(filter(lambda item: item == 1, dct.values()))
    return len(lst)

def unique(dct):
    set1 = set(dct.keys())
    return len(set1)

words = open_file()
dict1 = count_words(words)
dict2 = sort(dict1)
print('Most frequently used words')
print('{:<5}{:>15}{:>10}'.format('#','Word','Freq.'))
print('{:=>31}'.format(''))
count = 1
for x in dict2:
        while count < 11:
            print('{:<5}{:>15}{:>10}'.format(count,x,dict2[x]))
            count += 1
            break
print()
print('There are {} words that occur once'.format(occur_once(dict1)))
print('There are {} unique words in the document'.format(unique(dict1)))

