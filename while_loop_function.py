i = 0 
numbers = []

#Ec 1
#numb = 6
#iplus = 10

def theloop(numb):
        global i
        #i = 0
        #number = []
        while i < numb:
            print "At the top of i is %d" % i
            numbers.append(i)

            i = i + 1
            print "Numbers now: ", numbers
            print "At the bottom i is %d" % i

        print "The numbers: "

        for num in numbers:
            print num

theloop(7)