def alphabetical_substring(string):
	# Returns longest string in alphabetical order
	longest_length = 0
	longest_string = ""
	

	for i in range(0, len(string) - 2):
		length = 0
		increment = 0

		while string[i + increment] < string[i + increment + 1]:
			# Find largest alphabetical substring starting from index i 
			increment += 1

			print(i, ":", i+ increment) # debug statement

			if (i + increment + 1) == (len(string) - 1): # if string ends, break
				break
		else:
			length = increment + 1

		if length > longest_length:
			longest_string = string[i:(i + length)]
			longest_length = length

	print(longest_string)
	print(longest_length)

alphabetical_substring("abcabcd")
