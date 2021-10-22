def get_mpg():
    while True:
        try:
            while True:
                mpg = int(input('Enter the minimum mpg ==> '))
                if mpg < 1:
                    print('Fuel economy given must be greater than 0')
                elif mpg > 100:
                    print('Fuel economy must be less than 100')
                else:
                    break
            return mpg
        except ValueError as excpt:
            print('You must enter a number for the fuel economy')
    print()
def read_write_file(mpg):
    count = 0
    while count < 1:
        try:
            name = input('Enter the name of the input vehicle file ==> ')
            with open(name,'r') as file:
                lines = file.readlines()
            out = input('Enter the name of the file to output to ==>')
            while True:
                try:
                    out = input('Enter the name of the file to output to ==>')
                    with open(out, 'w') as outfile:
                        count = 0
                        for x in lines:
                            if count ==0:
                                count +=1
                            else:
                                list = x.split('\t')
                                try:
                                    if int(list[7]) > mpg:
                                        outfile.write('{} {:<40} {:<40} {:>10.3f}\n'.format(list[0], list[1],list[2], float(list[7])))
                                except ValueError:
                                            print('Could not convert value {} for vehicle {} {} {}'.format(list[7], list[0],list[1],list[2]))
                    break
                except IOError:
                    print('There is an IO Error {}'.format(out))
            count+=1
        except FileNotFoundError:
            print('Could not open file %s'%name)
mpg = get_mpg()
read_write_file(mpg)