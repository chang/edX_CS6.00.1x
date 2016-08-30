word = s

def countVowels(word):
	# Returns count of vowels in a word

	vowel_count = 0 

	for i in word:
		if i in ("a", "e", "i", "o", "u"):
			vowel_count += 1

	return(vowel_count)


print("Number of vowels:", str(countVowels(word)))