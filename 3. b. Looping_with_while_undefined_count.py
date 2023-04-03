# 3. b. Looping (while undefined count)

book_count = 10
print(f'Book count = {book_count} pieces')

print('Mother said, "Read all the books until you understand"')

read_count = 0
understood_count = 0
print(f'Read count = {read_count}')
print(f'Understood count = {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f'Book #{understood_count + 1} do not understand')
    else:
        understood_count = understood_count + 1
        print(f'Book #{understood_count} is understood')

print(f'The number of books that can be understood = {understood_count}')

if understood_count == book_count:
    print('Report to mother that all books have been read and understood')
else:
    print('Report to mother that not all books can be understood')
