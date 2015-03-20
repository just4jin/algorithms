# given a list of words, write a function which
# takes in the list, and groups the words together
# according to which ones are anagrams of eachother
# e.g.
# input = ["art", "rat", "bats", "banana", "stab", "tar"]
# output = [["art", "rat", "tar], ["bats", "stab"], ["banana"]]

# Test if word b is an anagram of word a
# def readfile():
# 	file = open('anagrams\dict.txt')
# 	words = []
# 	for line in file:
# 		words.append(line)
# 	file.close()
# 	return words

# anagrams sorted in order
def anagrams_ordered(words):
    groups = {}
    i = 0
    for word in words:
        i += 1
        key = "".join(sorted(word))
        if not key in groups:
            groups[key] = [i]
        groups[key].append(word)
    output = []
    for value in sorted(groups.values()):
        output.append(value[1:])
    return output


input = ["art", "rat", "bats", "banana", "stab", "tar"]

print(anagrams_ordered(input))

# def check(word1, word2): 
# 	if (sorted(word1)==sorted(word2.rstrip())):
# 		return True
# 	else:
# 		return False

# rstrip function returns a copy of string all chars have been stripped  from the end of string
# sorted function returns sorted list 