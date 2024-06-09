squares = ['red', 'yellow', 'green']
for i, square in enumerate(squares):
    print(i, square)

#while loop
squares2 = ['yellow', 'yellow', 'purple', 'yellow', 'yellow']
yellow_squares=[]
i=0
# while i < len(squares2):
#     if squares2[i]=='yellow':
#         yellow_squares.append(squares2[i])
#     else:
#         break
#     i+=1

# print(yellow_squares)

#easier way:
while(squares2[i]=='yellow'):
    yellow_squares.append(squares2[i])
    i+=1
#print(yellow_squares)

#functions
numbers = [1,4,6,8,9,43,2,5]

print(len(square))
print(sum(numbers))
sorted_numbers = sorted(numbers) #does not change the numbers list itself
print(numbers, sorted_numbers)
numbers.sort()
print(numbers)

def add1(a):
    b=a+1
    return b
print(add1(5))

numbers = [1,4,6,8,9,43,2,5]
def sorted_lists(a):
    a.sort()
    return a
sorted_def_nums=sorted_lists(numbers)
print(sorted_def_nums)

def mult(a, b):
    c=a*b
    return c
print(mult(2, 3.14))
print(mult(2, "hi there. "))

def printstuff(stuff):
    for i, square in enumerate(stuff):
        print("index is ", i, "the square is", square)
printstuff(squares)

def def_names(*names): #include as many names as u want
    for name in names:
        print(name)
def_names('nino', 'michael', 'john')

def new_variable():
    global x 
    x=5
new_variable() # calling the function is necessary if you want to define a variable x 
print(x)