# Use this as to test whatever comes to your mind. Send previous trials as comments at the bottom.
# Greyed comments are parts of the code designed to be ran.

#* NEW SECTION: Testing out things you can do with lists
#* New variables are defined below
#! Defined variables can be added together to create a list.
first = 'hello'
second = 'my'
third = 'name'
last = 'is'
#! The list created below will be used to perform the operations in this TESTER.
#* The strings that constitute it could be changed above.
variable_list = [first, second, third, last]

#* NEW SECTION: Slicing lists.
#* Like strings, indices can be used to specify certain aspects or parts of a list. Example shown below.
# sliced_variable_list = variable_list[2:3]
# print(sliced_variable_list)

#* NEW SECTION: Using 'append'.
#* 'append' is used to add new stuff to the end of a list.
# last_again = 'Inioluwa'
# variable_list.append(last_again)
# print(variable_list)

#* NEW SECTION: Using 'insert'
#* Unlike 'append', 'insert' allows you to specify where you'd like to add stuff into the list.
#* To do this, 'insert' asks you for the index of position as well as character to be added.
# last_again = 'Inioluwa'
# variable_list.insert(1, last_again)
# print(variable_list)

#* NEW SECTION: Using 'extend'
#* 'extend' allows the insertion the content of a list into another list. For example:
# fourth = 'they'
# fifth = 'said'
# variable_list_2 = [fourth, fifth]
#* To add 'fourth' and 'fifth' from the above list into the 'variable_list', we use extend.
# variable_list.extend(variable_list_2)
# print(variable_list)

#* NEW SECTION: Using 'remove' and 'pop'
#* remove will get rid of a particular item in a list. for example:
# variable_list.remove('hello') #* or:
# variable_list.remove(first) #* same as above
# print(variable_list)
#* pop on the other hand, will just remove the last item in the list. for example:
# variable_list.pop()
# print(variable_list)
#* after popping you could get the pop item by defining it as a variable
# popped_item = variable_list.pop()
# print(popped_item)

#* NEW SECTION: re-defining characters in a list
#* To replace items in a list, define them in this way:
# variable_list[0] = 'Hi'
# print(variable_list)

#* NEW SECTION: Using 'sort'
#* sort will get numbers from smallest to largest or strings in alphabetical order. for example:
# variable_list.sort()
# print(variable_list)
#* To get the opposite effect: largest-to-smallest numbers/z-to-a alphabetical, you do:
# variable_list.sort(reverse = True)
# print(variable_list)

#* NEW SECTION: Using 'sorted' function
#* in cases where you do not want to change your original list, but will still like a sorted version. for example:
# sorted_variable_list = sorted(variable_list)
# print(sorted_variable_list)

#* NEW SECTION: The 'enumerate' operator.
#! This creates a line-by-line numbering of each item in your list. Run (below) to see an example.
#! Note that the 'enumerate' operator usually works with with/in 'for' loops.
# for i in enumerate(variable_list):
#         print(i)

#* NEW SECTION: Using the 'join' function on lists.
#! 'join' is essentially the reverse of 'split'. Split converts strings into list and join does the opposite.
#* In essence, when a list is joined, it's elements are concatenated (similar to the case of using '+', unless a delimiter is specified)
# joined_list = ' '.join(variable_list)
# print(joined_list)
#* above is: new_string = 'delimiter'.join(old_list). Performing a split on the resulting string is shown below.
# variable_list_again = joined_list.split(' ')
# print(variable_list_again)

#? WHAT ARE TUPLES?
#* Tuples are basically lists with brackets(parenthesis). The main difference is they cannot be modified unlike lists.
#* As a result, they are referred to as immutable data sets.
#* Looping and checking for items still work for tuples though.

#? WHAT ARE SETS?
#* Sets are like lists and tuples but they use curly braces and do not keep characters in a particular order.
#* Below is an example of a set.
# first_set_cities = {'amsterdam', 'kigali', 'bangkok', 'montreal'}
# print(first_set)
#* If a second set is created, both sets 1 and 2 can be manipulated together as shown below.
# second_set_cities ={'stockholm','monrovia', 'bangkok', 'guadalajara'}
#! the 'intersection', 'union' and 'difference' operators could be used on the lists.
#* 'intersection' finds common characters (in our case, Bangkok). for example:
# print(first_set_cities.intersection(second_set_cities))
#* 'difference' finds all characters unique to a certain. for example:
# print(first_set_cities.difference(second_set_cities)) #* give {'amsterdam', 'kigali', 'montreal'} unique to set 1
#* 'union' merges characters in both sets. for example:
# print(first_set_cities.union(second_set_cities))