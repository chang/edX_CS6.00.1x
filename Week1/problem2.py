def countbob(word):
	# Returns count of substring "bob" in word

	bob_count = 0

	for i in range(0, len(word) - 2):
		# Loop through all substrings
		substr = word[i:(i + 3)]

		if(substr == "bob"):
			bob_count += 1

	#print("Number of times bob occurs is:", str(bob_count))
	print(str(bob_count))

# Call function for grading
word = s
countbob(word)