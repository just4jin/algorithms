'''
write code to generate all possible case combinations of a given lower-cased string
"0ab" -> ["0ab","0aB","0Ab","0AB",...]
Solution: use DP to solve permutation problem. For DP, always think about basic case 
and general case, base case is print out. Use break or return to end the for Loop

recursive sorting
'''

def permute(prefix,word):
	if len(word)==0:
		print prefix
	for i in range(len(word)):
		if word[i].isalpha(): # true if alphabetic
			permute(prefix + word[:i] + word[i].lower(), word[i+1:])
			permute(prefix + word[:i] + word[i].upper(), word[i+1:])
			return

permute("0","ab")