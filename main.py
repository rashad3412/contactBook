# create a contact book.
# create a list of contacts.
# existing contacts,add, and delete.

names = []
phone_numbers = []
new_contact = 3

sub = input("Would like to create new contacts? ")
while sub != 'no':
    name = input("Enter contact name: ")
    phone_number = input('Enter contact phone number: ')
    names.append(name)
    phone_numbers.append(phone_number)
    with open('contacts.txt', 'a') as f:
        f.write(name + ", " + phone_number + "\n")

    sub = input("\nWould like to add more contacts? ")
    if sub == 'yes':
        continue

print("\tName\t\t\tPhone Numbers")

for i in range(new_contact):
    print(f'\t{names[i]}\t\t\t{phone_numbers[i]}')

s = input('\nSearch Contact: ')
if s in names:
    index = names.index(s)
    name = names[index]
    phone_number = phone_numbers[index]
    print(f"Name: {name}\nPhone Number: {phone_number}")
else:
    print('contact not found: ')




