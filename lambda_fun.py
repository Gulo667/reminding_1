
example = [1,2,3,4,5,6,7,8,8,8,9,0,12]
even_numbers = tuple(filter(lambda x: x%2==0, example))
print (even_numbers)


#2
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 22},
    {'name': 'Eve', 'age': 19}
]
adults = tuple(filter(lambda person: person['age'] > 20, people))
print(adults)
sorted_people=sorted(people, key=lambda person: ['age'])
print(sorted_people)

#3

fruits = [
    {'name':'fragole', 'taste':'sweet'},
    {'name':'avocado', 'taste':'weird'},
    {'name':'peach', 'taste':'sweet'},
    {'name':'cherry', 'taste':'sour'},
    {'name':'apple', 'taste':'depends'},   
]

sweet_fruits = list(filter(lambda fruit: fruit['taste']=='sweet', fruits))
print(sweet_fruits)

#4
numbers = [1,2,3,4,5,6]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)