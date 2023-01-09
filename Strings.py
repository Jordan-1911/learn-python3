## This covers the basics of strings

my_string = 'Hello World'
type(my_string)
len(my_string)

# Can have multi line long strings
long_story = ('This is a long story. '
              'It is a story that is so long that it needs to be on multiple lines. '
              'It will still print as one line')

print(long_story)

# str.replace()
# this does not modify the string. If you want to modify the string, you need to assign it to a new variable
# str.replace(old, new)

my_string.replace('Hello', 'Goodbye')  # this will not modify the string
print(my_string)
print()

my_new_string = my_string.replace('Hello', 'Goodbye')  # this will modify the string
print(my_new_string)
print()

# str.format()
secret = '{} is cool'.format('Python')
print(secret)  # this will print 'Python is cool'
print()

print('My name is {} and I am {} years old'.format('John', 25))


# str.upper() str.lower() str.title()
mixed_case = 'PyThOn Is AwEsOmE'
print(mixed_case.upper())
print()
print(mixed_case.lower())

# str.strip()
ugly_format = ' \n \t Some story to tell '
stripped = ugly_format.strip()

print('ugly: {}'.format(ugly_format))
print()
print('stripped: {}'.format(stripped))

# str.split()
sentence = 'This is a sentence'
words = sentence.split()
print()
print(words)
print(type(words))

secret_binary_data = '01001,101101,11100000'
binaries = secret_binary_data.split(',')
print()
print(binaries)

# Can call multiple methods in a row
ugly_mixed_case = ' PyThOn Is AwEsOmE '
pretty = ugly_mixed_case.strip().lower().replace('python', 'java')
print()
print(pretty)
print()

# Escape characters
two_lines = 'First line\nSecond line'
print(two_lines)

indent = '\t this line will be indented'
print(indent)

