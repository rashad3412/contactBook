names = []
phone_numbers = []

num = 2

for i in range(num):
    name = input('Enter Name: ')
    phone_number = input('Enter phone number: ')
    names.append(name)
    phone_numbers.append(phone_number)


print("\tname\t\t\tphone_number")

for i in range(num):
    print(f"\t{names[i]}\t\t\t{phone_numbers[i]}")

s = input('Enter the name to search: ')
if s in names:
    index = names.index(s)
    name = names[index]
    phone_number = phone_numbers[index]
    print(f"Name:{name} , Phone Number: {phone_number}")
else:
    print('not found:')