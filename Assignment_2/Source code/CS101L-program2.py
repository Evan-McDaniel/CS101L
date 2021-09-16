'''

CS 101 Lab
Section 5
program #2
weighted grade system
Evan McDaniel
emdby@umsystem.edu

Problem:
    Create software to calculate a users weighted grade and letter

Algorithm:
    step 1: get name, lab, exam, and attendence input
    step 2: validate input to make sure it is within 0 and 100 and change if necessary
    step 3: calculate weighted grade
    step 4: output users name and weighted grade and letter grade

Error handling:
    change users input of necessary if it is out of range of 0 and 100

Other comments:
    Adding welcome and ending statement
    
'''

print('***Welcome to the lab grade calculator!***'  )
print()
name = input('Who are we calculating grades for: \n')
print()
lab_grade = int(input('Enter the labs grade:\n'))
if lab_grade < 0:
    lab_grade = 0
    print('The lab value should have been zero or greater. it has been changed to 0')
elif lab_grade > 100:
    lab_grade = 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
print()
exam_grade = int(input('Enter the Exams grade:\n'))
if exam_grade < 0:
    exam_grade = 0
    print('The exam value should have been zero or greater. it has been changed to 0')
elif exam_grade > 100:
    exam_grade = 100
    print('The exam value should have been 100 or less. It has been changed to 100.')
print()
attendence_grade = int(input('Enter the Attendence grade:\n'))
if attendence_grade < 0:
    attendence_grade = 0
    print('The attendence value should have been zero or greater. It has been changed to 0')
elif attendence_grade > 100:
    attendence_grade = 100
    print('The attendence value should have been 100 or less. It has been changed to 100.')
weighted_grade = (lab_grade*.7)+(exam_grade*.2)+(attendence_grade*.2)
print()
print('The weighted grade for %s is %d'%(name,weighted_grade))
if weighted_grade < 60:
    letter = 'F'
elif weighted_grade < 70:
    letter = 'D'
elif weighted_grade < 80:
    letter = 'C'
elif weighted_grade < 90:
    letter = 'B'
elif weighted_grade < 101:
    letter = 'A'
print(name,'has a letter grade of', letter)
print()
print('*** Thanks for using the Lab grade calculator ***')
