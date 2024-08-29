user = input("Enter a username: ")
letter_count = 0
for char in user:
    if char.isalpha():
        letter_count += 1
print(user.upper(), "tiene", letter_count, "letras")
