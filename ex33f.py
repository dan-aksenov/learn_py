def whileloop(low,high,incr):
	''' exercise 33 as function '''
	numbers = []
	while low < high:
		print "At the top it is % d" % low 
		numbers.append(low)
	
		low += incr
		print "Numbers now: ", numbers
		print "At the bottom it is %d" % low

	print "The numbers: "

	for num in numbers:
		print num
