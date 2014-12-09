#import argv from sys
from sys import argv
#argv wants a filename with the run command (%run C:/Users/Tim/temp/ex15.py C:/Users/Tim/temp/ex15_sample.txt
#)
#argv unpacks the variables script and filename and filename is assigned the file typed with the run command
script, filename = argv

#the variable txt is assigned the command to open the variable filename
txt = open(filename)

#line below prints a line filling in the name of the variable filename
print "Here's your file %r:" % filename
#line below prints the results of the command read() which is called on the variable txt
print txt.read()
txt.close()

#prints a prompt
print "Type the filename again:"
#assignes the filename to the variable file_again via the raw_input command and uses a greater than symbol to show where to type
file_again = raw_input("> ")#C:/Users/Tim/temp/ex15_sample.txt


#assigns the variable txt_again with the command open which is called on the variable file_again
txt_again = open(file_again)

#prints the results of read() called on the variable txt_again
print txt_again.read()
txt_again.close()