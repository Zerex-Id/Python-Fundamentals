# 3.a. Looping (with for and while)

# Looping with for
print('\n===== Loop with for =====')

book_count = 10
print(f'Book count = {book_count} pieces')

print('Mother said, "Read all the books!"')

read_count = 0
print(f'Read count = {read_count}')

for read_count in range(1, book_count + 1):
    print(f'Book #{read_count} has been read')

print('Report to the mother that all books have been read')

# Looping with while
print('\n===== Loop with while =====')

book_count = 10
print(f'Book count = {book_count} pieces')

print('Mother said, "Read all the books!"')

read_count = 0
print(f'Read count = {read_count}')

while read_count < book_count:
    read_count = read_count + 1
    print(f'Book #{read_count} has been read')

print('Report to the mother that all books have been read')
