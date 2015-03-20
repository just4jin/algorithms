# Given a string, determine if it's a palindrome
# now do it while ignoring spaces

import math

def palindrome(s):
	output= True
	for i in range(int(math.ceil(float(len(s))/2))):
		if s[i] != s[-(1+i)]:
			output = False
			break
	return output

s = "aca"
print palindrome("acb   ca")
print(s[0])
print (s[-(1)])