#  1. Given two sorted lists, produce the intersection of the list.
#  2. Now don't include duplicates.

# Some questions that come up in this process:

#  1. What is the worst case computational time of your algorithm?
#  2. What is the additional memory requirement of your algorithm (beyond
#    the provided lists)

def intersect_nodupes5(j,k):
	i1 = 0
	i2 = 0
	ret = []
	while i1 < len(j) and i2 < len(k):
		if j[i1] < k[i2]:
			i1 += 1
		elif k[i2] < j[i1]:
			i2 += 1
		elif j[i1] == k[i2]:
			if (not ret or ret[-1] != j[i1]): # exclude duplicates
				ret.append(j[i1])
			i1+=1
			i2+=1
	return ret

# test
l1 = [-1, 4, 5, 8, 12]
l2 = [1,2,3,4,5,6]

l1_dupes = [1,4,5,5,8,12] #j
l2_dupes = [2,4,5,5,9] #k

print intersect_nodupes5(l1_dupes, l2_dupes)
print intersect_nodupes5(l1, l2)