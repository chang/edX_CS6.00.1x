'''
Problem 2 - Week 1
Return the count of substring 'bob' in a string
'''

def countbob(word):
	bob_count = 0

	for i in range(0, len(word) - 2):
		# Loop through all substrings
		substr = word[i:(i + 3)]

		if(substr == "bob"):
			bob_count += 1

	print(str(bob_count))

# # Call function for grading
# word = s
word = "bob the builder had a friend named bob"
countbob(word)