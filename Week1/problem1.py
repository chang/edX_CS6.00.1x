'''
Problem 1 - Week 1
Return the count of vowels in a string
'''

def countVowels(word):
	vowel_count = 0 

	for i in word:
		if i in ("a", "e", "i", "o", "u"):
			vowel_count += 1

	return(vowel_count)


# # Call function for grading
# word = s
word = "foobar"
print("Number of vowels:", str(countVowels(word)))


