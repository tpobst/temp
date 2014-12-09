#The defining of a function called cheese and crackers that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#a print statement within a function that takes the cheese_count argument from the definition of the function and places it into the string using %d or decimal place-holder
	print "You have %d cheeses!" % cheese_count
	#a print statement within a function that takes the boxes_of_crackers argument from the definition of the function and places it into the string using %d or decimal place-holder
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#always prints this sting
	print "Man that's enough for a party!"
	#prints this string and then makes a new line with \n
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
#runs the cheese_and_crackers function with 20 as the cheese_count argument and 30 as the boxes_of_crackers argument
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
#sets amount_of_cheese and amount_of_crackers arguments outside of calling the cheese_and_crackers function
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
#the amounts are still set as 10 and 50 here from lines 19 and 20
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)