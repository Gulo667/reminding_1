#create a class to return the strings with the implemented abs function in the object, which will print a string in lowercase
#buildin ABS function prints out the absolute value - which is a positive value of the given number
class implementabs:
    def __init__(self, string):
        self.string=string

    def __abs__(self):
        return self.string.lower()
    

custom_ob=implementabs("HELLO")
x = abs(9)
y = abs(-100.867)
z = abs(custom_ob)

print(f"{x}\n{y}\n{z}")

#all function - prints out if the values are true or false
#example 1
a= [1, 0, [0, 0], 3, 4,5 , 6, [0,1]]
print(all(a))

#example 2 - including any() function = prints out if the given condition is true for any value
languages = ['java', 'perl', 'PHP', 'python', 'js', "c++", 'ruby']
print(all(len(l) >= 2 for l in languages))
print(any('++' in l for l in languages))

#boolean
for falsy in ([], [], {}, range(2), None):
    print(falsy, bool(falsy))