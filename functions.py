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