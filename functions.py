#password generator example
wordlist = ['password', 'john', 'qwerty', 'admin']

for word in wordlist:
    counter = 0
    while counter < 100:
        print(f'{word}{counter}')
        counter = counter + 1

#functions-let us define code blocks that perform a range of actions,produce range of values and optionally return one or more of these values.
#FIRST FUNCTION
#def-is used to define functions in python.
#defining f(x)=2 * X + 5

def f(x):
    return 2 * x + 5
print(f(10))

#Power_Of Function-a function to calculate and return that one value to the power of another value
def power_of(x, exponent):
    return x ** exponent
print(power_of(4, 2))

#Function Call-allows us to pipe the function,s output  to the input of another.
def power_of(x, exponent):
    return x ** exponent

power_of(4,2)
eight = power_of(2, 3)
print('My favourite number is:')
print(power_of(4, 2))