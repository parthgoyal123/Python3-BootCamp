
#* ============== Basic Data Types ============= *#

integer = 3																			#int - whole numbers
floating_point = 2.3																#float - Numbers with a decimal point
string = 'Hello'																	#str - ordered sequence of characters
lists = [10, 'hello', '2000']														#list - ordered sequence of objects
dictionaries = {'hello': '100', 'goodbye': '200000'}								#dict - unordered key:value pairs
tuples = (10, 'hello', 200.3)														#tup - ordered immutable sequence of objects
sets = {'a', 'b'}																	#set - unordered collection of unique objects
booleans = True																		#bool - logical value indication True or False

#! Python uses dynamic typing

# type() may help in determining the type of variable
print(type(integer))
print(type(sets))

#*  ----------- Numbers ------------ *#

2+1																					# addition
2-1																					# subtraction
2*4																					# multiply
7/4																					# division
2**4																				# power to 4
4%3																					# modulo
7//4																				# floor division (returns int)

#* ----------- Strings ------------ *#

# '' or "" both work
# Indexing starts from 0 (In octave, it starts from 1)

print(string)
length_string = len(string)															# returns the length of the string
print(length_string)

# Since strings are ordered sequence it means we can use indexing [] and slicing [start:stop:step] to grab sub-sections of the string.
mystring = 'Hello World'
indexing1 = mystring[0]																# grabbing a single character
# Python has reverse indexing i.e let string = 'hello', then string[0] = 'h', string[-4] = string[1] = 'e', etc..
indexing2 = mystring[-1]															# grabbing the last character using reverse indexing

# In splicing, start index is included, but not stops (i.e. stop index is excluded)
slicing1 = mystring[2:]																# from index 2 to last
slicing2 = mystring[:3]																# upto index 3 but not including 3
slicing3 = mystring[3:6]															# grabbing a sub-section
slicing4 = mystring[::2]															# from start to end with step size 2
slicing5 = mystring[::-1]															# reversing a string

#! Strings are immutable i.e if mystring = 'hello', then we cannot do mystring[2] = 'h'... (assign it to a new string instead)

print(mystring + ' Hello' + ' World')												# concatenation	
letter = 'zy'
print(letter * 10)																	# multiplying string repeats all the characters n times

print(mystring.upper())																# upper FUNCTION #! do not forget (), since it is a method
print(mystring.lower())
mystring = 'My name is Parth'
print(mystring.split())																# split whenever encounter whitespace
print(mystring.split('i'))															# split whenever encounter 'i'

# .format() method for string formatting
print('This is a string {}'.format('Inserted'))
print('The {f} {b} {q}'.format(f = 'fox', b = 'brown', q = 'quick'))				# we can use indexing numbers too, but the indicated method is best

# float formatting '{value:width.precision f}'
result = 100/777
print('The result was {r:10.5f}'.format(r = result))								# upto 5 floating point precision, but by using 10- we are adding whitespace

# f string method for string formatting
print(f'Hello there, how are you?\n{mystring}')										# variable name within the braces {}

#* ----------- Lists ------------ *#

mylist = [1,2,3]
mylist = ['String', 10, 100.0]														# can be reassigned
print (len(mylist))
# indexing and slicing same as in Strings
# list concatenation is also possible
# lists are mutable
mylist.append(6)																	# appending the list at last (check into other methods)
mylist.pop()
popped_item = mylist.pop(1)															# by default .pop(-1) acts
mylist = [45, -89, 56, 100, -78]
mylist.sort()																		# sorting the list
print(mylist)

mylist.reverse()																	# reverse the list
print(mylist)

#* ----------- Dictionaries ------------ *#

#! unordered and cannot be sorted, indexed or sliced

mydict = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(mydict['apple'])																# returns the value of key 'apple'
print(mydict.values())
print(mydict.keys())
print(mydict.items())																# get all the items stored in the dictionary

mydict = {'k1': [0,1,2], 'k2': ['hello', 'apple', 'world']}
print(mydict['k2'][2].upper())														# get the value of k2, then string at index 2 and return upper of it

#* ----------- Tuples ------------ *#

# Similar to lists (indexing, splicing etc) but immutable
mytuple = (1, 2, 3)
mylist = [1, 2, 3]
mytuple = ('a', 'a', 'b')
print(mytuple.count('a'))															# number of times 'a' in the tuple
print(mytuple.index('b'))															# first index of 'b'

#! mytuple[0] = 'hello' will not work, immutable

#* ----------- Sets ------------ *#

# keeps distinct elements in sorted order
myset = [1,1,1,2,2,6,5,3,5,6,5,6,2,3,3,4]
myset = set(myset)
print(myset)																		# only distinct items kept in set
myset.add(4)																		# adding a previously added object won't have any impact
myset.add(7)																		# this will be added
print(myset)

#* ----------- Booleans ------------ *#

print(1 > 2)
print(1 == 2)
print(1 <= 2)
print(1 != 2)

mybool = 1 != 2
print(type(mybool))
print(mybool)

mybool = None
print(type(mybool))																	# NoneType variable