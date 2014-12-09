from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
#in_file equals calling open on from_file which is the file we are copying from
in_file = open(from_file)
#Then indata will equal reading the file we are copying from
indata = in_file.read()

#showing the length of the file we are copying from
print "The input file is %d bytes long" % len(indata)

#answering whether the file we are copying to exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#out_file equals opening the file we are copying to in write mode
out_file = open(to_file, 'w')
#copying the contents of the old file to the new file
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()