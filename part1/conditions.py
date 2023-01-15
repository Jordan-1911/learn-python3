## This section will cover making decisions based on conditions

# three basic variable types in Python:
# strings, integers, and floats
# boolean is another variable type
# expressed as True or False (capital)

greeting = "Hello"
print(greeting.islower())  # returns False

user_age = input("Enter your age: ")
my_age = 30

if int(user_age) > my_age:
    print("You are older than me")
else:
    print("You are younger than me")
    
# note the example above does not render proper decision
# if the ages are equal
# an elif statment can fix that

if int(user_age) > my_age:
    print("You are older than me")
elif (int(user_age) == my_age):
    print("We are the same age")
else:
    print("You are younger than me")

"""
Comparison operators:
< less than
> greater than
<= less than or equal to
>= greater than or equal to
== equal to
!= not equal to

"""

password = input("please enter your password: ")
if password != 'sEcReT':
    print("Incorrect password")

# note how the above example is case sensitive

# IF STATEMENTS WITH MULTIPLE CONDITIONS

# AND operator
user_age = input("Enter your age: ")
if (int(user_age) >= 18 and int(user_age) >= 21):
    print("You can buy alcohol and tobacco")
elif (int(user_age) < 18 and int(user_age) < 21):
    print("You can't buy alcohol or tobacco")
elif (int(user_age) >= 18 and int(user_age) < 21):
    print("You can buy tobacco but not alcohol")
    
# OR operator
has_credit_card = input("Do you have a credit card? (Y/N): ")
has_debit_card = input("Do you have a debit card? (Y/N): ")
if (has_credit_card == "Y" or has_debit_card == "Y"):
    print("We can accept your payment")
else:
    print("We can't accept your payment")

# isnumeric() - returns True if all characters are numeric
# note: -1 and 1.5 are NOT numeric because ALL the chars in the string must be numeric
user_input = input("Enter a number: ")
if (not user_input.isnumeric()):
    print("You did not enter a number")
else: 
    print("You entered a number")
    
# Excercise - Write a program that will ask the user for a password
# and will check whether the it satisfies the conditions. 
# password must be at least 8 characters long and cannot start with the @ character

password = input("Enter a password: ")
if (len(password) < 8 or password[0] == "@"):
    print("Password does not meet requirements")
else:
    print("Password meets requirements")

# what happens when we combine and, or, and not together?

driver_nationality = input("What is your nationality? ")
driver_age = int(input("What is your age? "))

if (driver_nationality == 'Spanish' or driver_nationality != 'Spanish' and driver_age >= 26):
    print("You can drive")
else:
    print("You can't drive")

# Which operator - OR - or - AND - is evaluated first?
# is this condition really?

# (driver_nationality == 'Spanish' or driver_nationality != 'Spanish') and driver_age >= 26

# or is it:

# driver_nationality == 'Spanish' or (driver_nationality != 'Spanish' and driver_age >= 26)

# Python checks all conditions in the following order:
# NOT, AND, OR

# this means that the statement above would be:

# driver_nationality == 'Spanish' or (driver_nationality != 'Spanish' and driver_age >= 26)

# NESTED IF STATEMENTS

has_middle_name = input("Do you have a middle name? (Y/N): ")
if (has_middle_name == "Y"):
    likes_middle_name = input("Do you like your middle name? [Y/N]: ")
    if (likes_middle_name == 'Y'):
        print('That is good!')
    elif (likes_middle_name == 'N'):
        print('That is not good!')
    else:
        print("I do not understand your response")
elif (has_middle_name == 'N'):
    print("You don't have a middle name")
else:
    print("I do not understand your response")
    
# If the user answers Y to the first question, the next block executes
# and they are asked another question.
    
    