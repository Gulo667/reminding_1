tuple1=(10, 2.3, "monkey", True)
print(tuple1)
print(tuple1[::-1])
tuple2=tuple1 + ("cat", 35.67, 12)
print(tuple2)

# for printing the 3 elements:
print(tuple2[0:3])
sorted_tuple= sorted((4,6,9,5.6,3,8,0))
print(sorted_tuple) # returns a sorted list
#nesting tuples
nesting_tuple = (10, ('dog', 3.5), 'cat', (3,6,9), (12, 3.45, 'monkey', (1.1)))
print(nesting_tuple[4][3])

#lists
L = [10, 15, 'cat', 34.56]
L.extend([12, 'perrot'])
print(L)
L.append([2,4,5]) #adds only one element
L[2]='kitty'
del(L[0])
print(L)
a="hard work pays off".split()
print(a)
a="A,B,C,D,E,F".split(",")
print(a)
#to avoid the affects of one list changing another:
b=a[:]
a[0]="bear"
print(a, b)