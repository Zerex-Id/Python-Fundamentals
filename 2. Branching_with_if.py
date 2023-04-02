# 2. Branching (with if) : Step jump if the condition are met.

print('Mother said, "Go to the store"')
print('The child replies, "Okay, what should I do at the store?"')
print('Mother replied, "Buy one bottle of milk and if there are eggs buy 6 eggs')
print('So the child went to the shop. And start shopping')

print('=' * 30)

print('Store has:')
milk_count = 97
egg_count = 1776
print(f'Milk count = {milk_count} bottles')
print(f'Egg count = {egg_count} grains')

print('=' * 30)

if milk_count > 0:
    print('The child checked the price, it was enough')
    if egg_count == 0:
        print('The child bought a bottle of milk')
    else:
        print('The child bought a bottle of milk and 6 eggs')
else:
    print('The child does not buy milk')

print('The child returns home')
print('Give the proceeds to the mother')
