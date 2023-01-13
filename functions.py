# user defined functions
# functions begin with the keyword def

def hello_world():
    print("Hello World")

# to call the function 
hello_world()

# parameters

def hello_name(name):
    print("Hello " + name + '!')
    
hello_name('John')

def print_between(lower, upper):
    for i in range(lower, upper):
        print("The current value is: ", i)

print_between(1,10)

# RETURN
