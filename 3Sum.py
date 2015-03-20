'''
Given an arry S of n integers, there are elements a, b, c in S 
such that a + b + c = 0, Find all unique triplets in the array 
which gives the sum of zero.

 i.e. given array S = {-1 0 1 2 -1 -4}
 A solution set: (-1, 0, 1) (-1, -1, 2)
 '''
class Solution:
 	# @return a list of lists of length 3, [[val1, val2, val3]]
 	def threeSum(self,num):
 		res = [] 
 		if len(num) < 3: 	# length of list less than 3, return []
 			return res

 		Slen, Snum = len(num), sorted(num) 	# sorted number length and number
 
 		for i in range(Slen - 2):   
 			if i == 0 or Snum[ i ] > Snum[ i - 1 ]: 	# 1st item 
 				j = i + 1 	# 2nd item
 				k = Slen - 1 	# 3rd item

 				while ( j < k ):
 					if -Snum[ i ] == Snum[ j ] + Snum[k]:
 						res.append([Snum[i], Snum[j], Snum[k]])
 						j += 1
 						k -= 1
 						# avoid duplicates
 						while j < k and Snum[j] == Snum[j-1]:
 							j += 1
 						while j < k and Snum[k] == Snum[k+1]:
 							k -= 1
 					elif -Snum[i] > Snum[j] + Snum[k]:
 						j += 1
 					else:
 						k -= 1
 		return res


S = [-1, 0, 1, 2, -1, -4]
S1 = [0,-1,1]
res1 =Solution().threeSum(S)
print res1
