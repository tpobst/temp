#imports argv from sys
from sys import argv

#unpacks the variables script and input_file from argv
script, input_file = argv

#first function: defines the command print_all which prints the command read called on f
def print_all(f):
	print f.read()

#second function: defines the command rewind which calls seek 0 on f.  seek 0 falls back to byte 0 of the file	
def rewind(f):
	f.seek(0)

#third function: defines the command print_a_line which will print the variable line_count which is typed with the function and will call readline on the variable f which is also typed with the funtion	
def print_a_line(line_count, f):
	print line_count, f.readline()

#defines the variable current_file as the command open called on the variable input_file	
current_file = open(input_file)

#prints some text and adds a new line
print "First let's print the whole file: \n"

#calls the function print_all on the variable current_file which will ultimately read and print the input file
print_all(current_file)

#prints some text
print "Now let's rewind, kind of like a tape."

#calls the function rewind on the variable current file, will ultimately track back to byte 0 of current_file
rewind(current_file)

#prints some text
print "Let's print three lines:"

#starts a counter for current_line at one
current_line = 1
#calls the function print_a_line on the variables: current_line and current_file, ultimately it prints the line of the current_line counter of the current_file
print_a_line(current_line, current_file)

#moves the counter up one, next line
current_line = current_line + 1
#prints the next line
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

