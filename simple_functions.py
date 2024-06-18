#create a class to return the strings with the implemented abs function in the object, which will print a string in lowercase
class implementabs:
    def __init__(self, string):
        self.string=string

    def __abs__(self):
        return self.string.lower()
    

custom_ob=implementabs("HELLO")
x = abs(-9)
y = abs(-100.867)
z = abs(custom_ob)

print(f"{x}\n{y}\n{z}")