happy = True

if happy:
    print("Happy and we know it!")
else:
    print("Not happy...")
#Thiss section will go over and condition statements -ifs and elses- i.e if/else block

#The elif(else-if) expression means we continue with this one if the previous conditin is not met
happy = 2

if happy == 1:
    print("Happy and we know it!")
elif happy == 2:
    print("Excited about it!")
else:
    print("Not happy...")

#While-loop is a loop that will execute its content as long as the defined condition is True
counter = 0

while counter < 5:
    print(f'Hello #{counter}')
    counter = counter + 1

#f-string adds an f at the beginning allowing us to swap out parts of strings with other values and variables by enclosing them in a pair of curly braces.
equation = f'The meaning of life might be {6 * 7}.'
print(equation)
me = 'ogore'
greeting = f'Hello {me}!'
print(greeting)

#for each loop-is a kind of a loop too,loops and list
groceries = ['Walnuts', 'Grapes', 'Bird seeds']
print(groceries)
#square brackets[]indicates a list

#or alternative syntax
groceries = [
    'walnuts',
    'grapes',
    'bird seeds'
]
print(groceries)

#string indexing-it,s usefull when we want to filter out certain parts of some output.
#However there is negative string indexing,which allows to count string from the end.
var = "ABCDEF"
print(var[0], var[1], var[2], var[3], var[4], var[5])
print(var[-1], var[-2], var[-3], var[-4], var[-5], var[-6])

#Substrings
var = "ABCDEF"
print(var[:2])  #up to index 2
print(var[2:])   #ignore everything up to index 2
print(var[2:4]) #everything btwn index 2 and 4 where index 2 is also counted
print(var[-2:]) #up to negative index 2

#For-Each Loop-it has 'for' keyword as the first followed by 'in' keyword
groceries = ['walnuts', 'grapes', 'bird seeds']

for food in groceries:
    print(f'Ibought some {food} today.')

    list_1 = [5, 3, 'cake', True, 4, 5]
    print(list_1)
    list_2 = [4, 3, 2, 1]
    for num in list_2:
        print(num)
    list_3 = ['Accidental', '4daa7fe9', 'eM13Me', 'Y!.90']
    secret =[]

    for x in list_3:
        secret.append(x[:2])
    
    print(''.join(secret))