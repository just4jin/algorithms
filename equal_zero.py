'''
an array which has a set of positive and negative numbers,
print all subsets sum which is equal to zero.
i.e. 2, 1, -1, 0, 2, -1, -1
o/p: 1 -1, 1 -1 0, 0, 2 -1 -1

solution:
this is similar to 4SUM question, instead of 4 number add up
to A+B+C+D=0, you have many numbers add up to zero.
Use 4SUM problem method, and go through every possible soltuion from 
1-SUM + 2-SUM + 3-SUM + ...

Instead of doing hash table, we do one hash table and set target
as zero, find negative value in the keys
key = 1, we find key : -1
'''

import itertools

def makeHashTable(L): 
	'''
	return all the possible values in this list. access zero key in dictionary,
	also, because we use index to access he number in the array, 
	there could have duplicate values which makes zerio.

	use another function to clean duplicate values.
	we calculate all possible values provided by an array,we can easily find value we want, 
	but complexity is high O(n) * O(n^2long(n))
	'''
	d = {}
	for r in range(len(L)):
		# r-length tuples, in sorted order, no repeated elements
		for subset in itertools.combinations(L, r+1):
			V = sum(subset)

			if V in d.keys():
				d[V].append(subset)
			else:
				d[V] = [subset]
	return d

# test
L = [2, 1, -1, 0, 2, -1, -1]
print(makeHashTable(L).keys())
print(makeHashTable(L)[0])
