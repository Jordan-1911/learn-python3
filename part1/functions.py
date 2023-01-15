# This file will cover functions in python and writing reusable code

# recursive function to calculate the factorial of a number
# recursive functions are functions that call themselves
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))

# default argument values
# these allow a default value to be set for a function argument
# when no arg is passed in
def dog_to_human_age(dog_age=1):
    return dog_age * 7

print(dog_to_human_age())  # no arg passed in so default value is used
print(dog_to_human_age(5))

# it is possible to have both required arguments and default arguments

def calculate_price(price, tax=0.08, discount=0):
    return price - discount + (price * tax)

print(calculate_price(100, 10, 0.1))
print(calculate_price(100, 10))

## since optional arguments are assigned to the right of required arguments
## how do we invoke a function without explicit values for the optional arguments

def calculate_price(weight, price_per_pound=1.5, tax=0.08):
    return weight * price_per_pound * (1 + tax)

print(calculate_price(170, tax = 0.89))

# with this way of invoking a function, the order of the arguments does not matter
# the values for the arguments above would be weight = 170, price_per_pound = 1.5 (default value) tax = 0.89

# NONE
def safe_division(x, y):
    if y == 0:
        return None
    else:
        return x / y

# by specifying return None, we can prevent a divide by zero error

# Excercise
# Write a function sum_between that will take two args, a and b
# and return the sum of all numbers between a and b
# but if b < a, return None

def sum_between(a, b):
    if b < a:
        return None
    else:
        return sum(range(a, b + 1))

print(sum_between(1, 10))

# PASS
def do_nothing():
    pass

print(do_nothing())

# pass is a placeholder for code that has not been written yet
# almost like TODO in other languages

# functions can call other functions inside of them

def contains_digits(word):
    for letter in word:
        if letter.isnumeric():
            return True
    return False

def contains_letters(word):
    for letter in word:
        if letter.isalpha():
            return True
    return False

def validate_password(password):
    if not contains_letters(password) or not contains_digits(password):
        return False
    else:
        return True

password = "hello123"
print(validate_password(password))

# DOCUMENTING FUNCTIONS

def calculate_price(weight, price_per_pound=1.5, tax=0.08):
    """
    Calculates the price of an item given its weight, price per pound, and tax
    Keyword arguments:
    weight -- the weight of the item in pounds
    price_per_pound -- the price of the item per pound
    tax -- the tax rate of the item
    """
    return weight * price_per_pound * (1 + tax)

# documentation should come immediately after the line defining the function
# and it should be indented together with the function body

# Excercise
# write a function that will calculate the total cost of printing posters
# the ink costs $1.25 per poster, each roll on which posters will be printed costs $50,
# and each roll can make 200 posters

# num_posters = int(input("Please enter the number of posters to be printed: "))
num_posters = 250
price_per_roll = 50
price_ink_per_poster = 1.25
posters_per_roll = 200

def calculate_cost_poster(num_posters):
    num_rolls = num_posters // posters_per_roll
    if num_posters % posters_per_roll != 0:
        num_rolls += 1
    return num_rolls * price_per_roll + num_posters * price_ink_per_poster

price = calculate_cost_poster(num_posters)
print("The total cost of printing {} posters is ${}".format(num_posters, price))

# Ask the user to enter three integers and print the smallest of them

def smallest_of_three():
    a = int(input("Please enter the first integer: "))
    b = int(input("Please enter the second integer: "))
    c = int(input("Please enter the third integer: "))
    return min(a, b, c)

print(smallest_of_three())

