# This file covers loops in Python 3

# basic loop
for i in range(1, 11):
    print("Current value: ", i)
    
# the above will print 1-10
# range(start, stop, step) 
# stop is not inclusive
# the above will print 1-10, but not 11. 
message = "Hello World"
count = 0
for char in message:
    count = count + 1
    print("The string contains: ", char, ' and the count is: ', count)
    
# while loops work as you would expect
count = 0
while (count < 10):
    print("The count is: ", count)
    count += 1

# write a program that checks a scret_number and asks the user to guess it
secret_number = 8
user_num = 0
while (secret_number != user_num):
    user_num = int(input("Guess the secret number: "))

# general rule of thumb: use for loops when you know how many times you want to loop
count_inner = 0
count_outer = 0
for i in range(1, 11):
    print("Current value of i: ", i)
    count_outer += 1
    for j in range(1, 11):
        print("Current value of j: ", j)
        count_inner += 1
print("The inner loop ran: ", count_inner, " times")
print("The outer loop ran: ", count_outer, " times")

# using BREAK in loops
user_input = input("Enter a number: ")
while True:
    if user_input.isnumeric():
        break
    user_input = input('Not a number, try again: ')
print("You entered number: ", user_input)

# Excerecise: Write a program that will ask the user to specfiy when 
# Python was first released
user_guess = input('when was Python first released? ')
while True:
    if user_guess == '1990':
        break
    user_guess = input('Incorrect, try again: ')

# break also works for for loops

user_input = input("Please enter your first name, without digits: ")
is_valid = True
for char in user_input:
    if char.isdigit():
        print("You entered a digit")
        is_valid = False
        break
    
if is_valid == True:
    print('Name format is correct')
else:
    print('Name format is incorrect')

# CONTINUE
# continue will skip the rest of the loop and go to the next iteration
# in the following example, we will print all numbers from 1-10, but skip 5
counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        continue
    print('Current value: ', counter)

# Excerise: Write a program that shows all even numbers less than 100 and are divisible by 6

current_value = 0
while current_value < 100:
    if (current_value % 6 == 0):
        print('The value: ', current_value, ' is divisible by 6')
    current_value += 1

# Excercise
# use a loop to calculate and print the value of 10 factorial
# or for any user input

user_input = int(input('Enter a number: '))
for i in range(1, user_input):
    user_input *= i
print(user_input)
