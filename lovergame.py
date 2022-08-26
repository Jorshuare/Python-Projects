import time

print('Hello mate, welcome to the True Love game')
a = input('\nAre you ready to play this game: ').lower()

list1 = []
list2 = []
list3 = ['t', 'r', 'u', 'e', 'l', 'o', 'v', 'e']
list4 = []
list5 = []

first_name1 = input('Please enter your first name Comrade: ').lower()
print('Nice to have you here, {}'.format(first_name1))
last_name1 = input('\nPlease enter your last name also, {}: '.format(first_name1)).lower()

list1 += first_name1
list1 += last_name1


time.sleep(2)
lover_name1 = input('\nPlease enter your lover\'s name: ').lower()
lover_name2 = input('Please enter your lover\'s surname: ').lower()

list2 += lover_name1
list2 += lover_name2

for i in list1:
    if i in list3:
        list4 += i
first_percent = len(list4)

for _ in list2:
    if _ in list3:
        list5 += _
second_percent = len(list5)

print(f'The percentage of you and your lover being together is {first_percent}{second_percent}%')


# Another way to solve it

# user_name = input('Enter your name: ')
# lover_name = input('Enter your lover\'s name: ')

# combined_name = user_name + lover_name
# print(combined_name)

# t = combined_name.count('t')
# r = combined_name.count('r')
# u = combined_name.count('u')
# e = combined_name.count('e')

# tr = t+r+u+e
# true = str(tr)

# l = combined_name.count('l')
# o = combined_name.count('o')
# v = combined_name.count('v')
# e = combined_name.count('e')

# lo = l+o+v+e
# love = str(lo)

# print(f'The percentage of you and your lover being together is {true}{love}%')

# Not totally the same but you can use the same idea to solve that same question in a shorter way.


