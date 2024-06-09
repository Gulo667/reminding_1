"""
You need to create a simple contact list management system. This system should allow you to:

Add new contacts with their phone numbers.
Search for a contact by name.
Print a list of all contacts.
Instructions:
Create a list to store contact records. Each record should be a dictionary with keys 'name' and 'phone'.
Implement the following functions:
add_contact(contacts, name, phone): Adds a new contact with the given name and phone number.
search_contact(contacts, name): Searches for a contact by name and returns the phone number.
print_contacts(contacts): Prints a list of all contacts with their names and phone numbers.

"""

contacts =[]

def add_contact(contacts, name, phone):
    contacts.append({'name':name, 'phone':phone})

def search_contact(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact['phone']
    return None

def print_contacts(contacts):
    for contact in contacts:
        print (f"Name: {contact['name']}, phone: {contact['phone']}")

add_contact(contacts, 'Alice', '123-456-7890')
add_contact(contacts, 'Bob', '234-567-8901')
print_contacts(contacts)
phone = search_contact(contacts, 'Alice')
if phone:
    print(f"Alice's phone number is: {phone}")
else:
    print("Alice not found")