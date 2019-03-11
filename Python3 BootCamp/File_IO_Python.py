
#* ============== Basic File Input Output ============= *#

# myfile = open('whoops_wrong.txt')													# will not open, as there is no file whoops_wrond
myfile = open('myfile.txt')															# open the file

print(myfile.read())																# read all the contents of the file
print(myfile.read())																# we observe that nothing is printed, since the cursor has reached the end
myfile.seek(0)																		# get the file pointer reader to start again

content = myfile.read()
myfile.seek(0)
lines = myfile.readlines()															# get all the lines separately in a list
print(lines)	
myfile.close()																		# important to close the file after use

myfile = open('/media/parthgoyal123/Data/Python3 BootCamp/myfile.txt')				# write the absolute path if file in other location
print(myfile.read())

# grabbing the contents of the file without worrying about closing the file
with open('myfile.txt') as my_new_file:
	contents = my_new_file.read()

print('')																			# printing new line
print(contents + '\tHello World')

''' 
Different modes while accessing a file

mode = 'r' read only
mode = 'w' write only (overwrite or create new!)
mode = 'a' append only
mode = 'r+' reading and writing
mode = 'w+' writing and reading (overwrites existing files or creates a new file!)
'''

with open(file = 'newfile.txt', mode = 'r') as f:									# reading from a file using mode = 'r'
	print(f.read())

with open(file = 'newfile.txt', mode = 'a') as f:									# appending to  a file using mode = 'a'
	f.write('\nFour on Four')

with open(file = 'newfile.txt', mode = 'r') as f:									# reading from a file using mode = 'r' and observing the change
	print(f.read())

with open(file = 'new_file_write.txt', mode = 'w') as f:							# creating a new file and writing into the file
	f.write('I created this file!!')

with open(file = 'new_file_write.txt', mode = 'r') as f:							# reading from a new_file using mode = 'r'
	print(f.read())