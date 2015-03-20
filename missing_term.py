''' you have n-1 numbers from 1 to n. task is to find missing number.
n = 5
v = [4,2,5,1]
result is 3
'''
'''
solution idea: add all numbers in the array as r1. calculate sum of n numbers
using n*(n+1)/2 = r2 substract r1 from r2. result is the missing number.
'''
def find_missing_value(l,n):  
	r1 = sum(l)
	r2 = n*(n+1)/2
	missing_value = r2 - r1
	return missing_value

# test
N = 10
L = [1,2,3,4,5,6,7,9,10]
print find_missing_value(L,N)