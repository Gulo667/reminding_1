dict1 = {"name":"John", "surname":"smith", "age": 24, "address": "NY"}
print(dict1["name"])
print("birthday" in dict1)
dict1["birthday"] = 2000
print(dict1)
del(dict1["age"])
print(dict1)
print(dict1.keys())

#sets
#sets do not record the element position - unordered one
#contains only unic ellements
set1 = {"cat", "dog", "monkey", "dog", "cat" "bear"} #duplicates will not be presented even tho they're in the list
print(set1)
#typecasting
list1 = [1,1,1,2,"cat",3,4,5,5,5,6,7,8]
set2=set(list1)
set2.add("perrot")
set2.remove("cat")
print(type(set2), set2)
#ven diagrams can be used to display the elements of the sets
set2={'bob', "cat", "john", "dog"}
set3={"cat", "perrot", "dog", "monkey"}
print(set2&set3)
print(set2.union(set3)) # puts all the unique elements in one whole set
set4={"cat", "dog"}
print(set4.issubset(set2))
