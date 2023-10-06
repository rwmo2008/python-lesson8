#lists
days_of_week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat']
'''This should print Tuesday'''
print(days_of_week[2])
'''This should print all days of the week'''
#for count in range(7):
for count in range(len(days_of_week)):
    print(days_of_week [count])

'''Changes Sun to Sunday'''
days_of_week[0] = 'Sunday'
print(days_of_week)

'''Slicing list'''
print(days_of_week[2:5])

'''Nesting list'''
child1 = ['Pat', 5, 6.5]
family = [child1]
'''Should print 5'''
print(family[0][1])

'''Appending to list'''
my_list=[]
my_list.append(10)
my_list.append('ten')
print(my_list)
'''Extend function'''
my_list.extend([20, 'twenty'])
print(my_list)
'''Concantenate to list'''
my_list = my_list + [30, 'thirty']
print(my_list)
'''Insert to list'''
'''inserts string to index #3'''
my_list.insert(3, 'hi there!')
print(my_list)
'''remove item from list (only removes 1st instance)'''
my_list.remove('hi there!')
print(my_list)

'''find largest value'''
my_numbers = [16, 8, 15, 42, 23, 4]
print(max(my_numbers))
'''Sorting list'''
my_numbers.sort()
print(my_numbers)
'''reverse list'''
my_numbers = [16, 8, 15, 42, 23, 4]
print(my_numbers)
my_numbers.reverse()
print(my_numbers)
