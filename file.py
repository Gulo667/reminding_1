with open('text.txt', 'w') as file:
    file.write(f"hello")

with open('text.txt', 'r') as file:
    content = file.read() + " "+ "Alice"
    print(content)