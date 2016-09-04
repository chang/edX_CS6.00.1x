'''
Problem 3 - Week 3
Find longest alphabetical substring in a given string
'''

def alphabetical_substring(string):
	'''
	Returns longest alphabetical substring.
	1. Iterate through each letter in string
	2. Check consecutive letters to find longest string
	3. Store all in a list, then return longest

	returns in list [string, length]
	'''
	stringList = []

	# Obtain list of all alphabetical substrings
	for i in range(0, len(string) - 2):

		counter = 0
		while string[i + counter] <= string[i + counter + 1]:
			counter += 1

			if (i + counter) == len(string) - 1:
				break

		stringList.append(string[i:(i + counter + 1)]) # Add string to the list

	# Find longest substring
	stringListLengths = [len(x) for x in stringList]
	longestStringIndex = stringListLengths.index(max(stringListLengths))


	return(stringList[longestStringIndex], max(stringListLengths))


x = alphabetical_substring("hojijxbhwmoawnmbyausrrky")
print("Longest alphabetical substring is '", x[0], " ' of length", x[1])


## Figure out why this is buggy later
# def alphabetical_substring(string):

# 	longest_length = 0
# 	longest_string = ""
	

# 	for i in range(0, len(string) - 2):
# 		length = 0
# 		increment = 0

# 		while string[i + increment] < string[i + increment + 1]:
# 			# Find largest alphabetical substring starting from index i 
# 			increment += 1

# 			print(i, ":", i+ increment) # debug statement

# 			if (i + increment + 1) == (len(string) - 1): # if string ends, break
# 				break
# 		else:
# 			length = increment + 1

# 		if length > longest_length:
# 			longest_string = string[i:(i + length)]
# 			longest_length = length

# 	print(longest_string)
# 	print(longest_length)

# alphabetical_substring("abcabcd")
