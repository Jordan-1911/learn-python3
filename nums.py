a = 2
b = 2.5
print(a + b)  # this will print 4.5

# python does not allow you to concatenate strings and numbers
# print('Hello world' + 2)  # this will throw an error') 

# however, multiplication does work with strings
print("hello" * 3)  # this will print hello 3 times

# Try the following mathematical calculations and guess what is happening: ((3 / 2)),
# ((3 // 2)), ((3 % 2)), ((3**2)).

print(3/2)
print(3//2)  # this will print 1 since it will floor the quotient

print(3 % 2)  # this will print 1 since it will return the remainder

print(3**2)  # this will print 9 since it will raise 3 to the power of 2

# 2. Calculate the average of the following sequences of numbers: (2, 4), (4, 8, 9), (12,
# 14/6, 15)

my_list = [2, 4, 4, 8, 9, 12, 14, 6, 15]
sumNums = sum(my_list)
print(sumNums)

count = len(my_list)
print(count)

avg = sumNums / count
print("The average is: ", avg)

# 3. The volume of a sphere is given by (4/3 * pi * rˆ3). Calculate the volume of a sphere
# of radius 5. Suggestion: create a variable named “pi” with the value of 3.1415

radius = 5
pi = 3.1415
volume = (4/3 * pi * radius**3)
print(volume)

# 4. Use the modulo operator (%) to check which of the following numbers is even or
# odd: (1, 5, 20, 60/7).

print(1 % 2)  # this will print 1 since it is odd
print(5 % 2)  # this will print 1 since it is odd
print(20 % 2)  # this will print 0 since it is even
print(60/7 % 2)  # this will print some fractional value 0.57 since it gives remainder

# 5. Find some values for (x) and (y) such that (x < 1/3 < y) returns “True” on the
# Python REPL. Suggestion: try (0 < 1/3 < 1) on the REPL.

x = -10
y = 10
print(x < 1/3 < y)  # this will print true since 1/3 is between -10 and 10

## Excercises with Strings
# 1. Initialize the string “abc” on a variable named “s”:
# 2. Use a function to get the length of the string.
# 3. Write the necessary sequence of operations to transform the string “abc” in
# “aaabbbccc”. Suggestion: Use string concatenation and string indexes.

s = "abc"
count = len(s)
# can use join method
new_string = ''.join([char*3 for char in s])
print(new_string)

# or a loop also works
new_string = ''
for char in s:
    new_string += char*3
print(new_string)


# 2. Initialize the string “aaabbbccc” on a variable named “s”:
# 1. Use a function that allows you to find the first occurence of “b” in the string,
# and the first occurence of “ccc”.
# 2. Use a function that allows you to replace all occurences of “a” to “X”, and
# then use the same function to change only the first occurence of “a” to “X”

s = 'aaabbbccc'
first_occurence = s.find('b')
print(first_occurence)  # will print 3 since b is at index 3

first_occurence = s.find('ccc')
print(first_occurence)  # will print 6 since ccc is at index 6

new_string = s.replace('a', 'X')
print(new_string)  # will print XXXbbbccc

# to change only first occurrence

index = s.index('a')
new_string = s[:index] + 'X' + s[index+1:]
print(new_string)  # will print Xaabbbccc

# converting string to list, since strings are mutable
new_list = list(s)
new_list[new_list.index('a')] = 'X'
new_string = ''.join(new_list)
print(new_string)

