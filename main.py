# Alex Williams
# 10/1/2024
# Python if-else statments


# Task 1

# Read if-else statements, pp.79-80 in the yellow PCC
# Read


# Task 2

alien_color = 'Green'
if alien_color == 'Green':
    print('You have earned 5 points')
else:
    print('You have earned ten points')


# Task 3
    
first_name = input('Please enter your first name: \n')
first_name_num = len(first_name)

if first_name_num <= 5:
    print('Your first name is too short')
else:
    print('You have a long name frist name')


# Task 4
    
letter = input('please enter a letter of the alphabet\n')
vowels = ['a','e','i','o','u']

if letter.lower() in vowels:
    print('That letter is a vowel')
else:
    print('That letter is a consonent') 



# Task 5
    
integer1 = int(input('Please enter an integer: \n'))
integer2 = int(input('Please enter another integer: \n'))

if (integer1) % (integer2) == 0:
    print('The first integer can be divided by the second integer')
else:
    print("That first integer cannot be divided by the second integer")
 