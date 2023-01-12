# to make programs interacitve, you can use input() to get user input

age = input("How old are you? ")
print("You are", age, 'years old')

# user input is always treated as a string unless converted 
# basic functions = str(), int(), float()
"""
str(x) converts x to a string
int(x) converts x to an integer
float(x) converts x to a float

"""

# program to convrt km to miles

distance_km = input("Enter a distance in km: ")
distance_miles = float(distance_km) // 1.60934
print("That is", distance_miles, "miles")


"""
Excersises
- Write a program that asks the user for an hourly rate, the num of hours workd
and display the total amount earned
 
"""
hourly_rate = input("Enter your hourly rate: ")
num_hours = input("Enter the number of hours worked: ")
print("You have earned", float(hourly_rate) * float(num_hours), "in total")

# Excercise 2
# Write an interactive program that tells the user how much they can
# earn on a deposit when compound interest is applied

principal = input("Enter the principal amount: ")
principal = float(principal)  # must reassign variable
print(type(principal))


roi = .05
t = 365  # number of times the interest is compounded per year
num_years = 10
total = principal * (1 + roi/t) ** (t * num_years)
print(total)


