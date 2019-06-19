# random_set = {4, 9, 15, 16, 299, 700, 21, 10830183}
# print(random_set)
# print(random_set)

# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
#* To double the above list, the code below will not work. It'll give an infinite loop.
# for elements in a:
#     a.append(elements)
#     print(a)
#* Instead, the list should be concatenated with itself as shown below:
# a += a
# print(a)

#* The following can be be used to create a list of random numbers in a certain range. Range works with only integers.
# random_numbers_list = list(range(0,21))
# print(random_numbers_list)
#* The method below is a more versatile approach to building lists
random_number_list = [each_number for each_number in range(0,21)]
first_two_numbers = random_number_list[:2]
numbers_2to5 = random_number_list[2:6]
numbers_10to15 = random_number_list[10:16]
multiples_of_2 = random_number_list[0:21:2] #* [start:stop:step]
#* To replace multiples of 2 with multiples of 3, we simply assign the former as the latter as shown below
random_number_list[0:21:2] = range(0,31,3) #* or list(range(0,31,3))
print(random_number_list)

