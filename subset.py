
'''
If we're given a set of integers such that S = {1, 2, 3}, 
how can we find all the subsets of that set? 
For example, given S, the subsets are 
{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, and {1, 2, 3}.
'''

def subset(inputs):
    result = []
    num_of_subset = 1 << len(inputs) # << is a left bitwise shift. It takes the bits and shifts them left n places
    for i in xrange(num_of_subset):
        bitmask = i
        pos = len(inputs) - 1
        temp = []
        while bitmask > 0:
            if bitmask & 1 == 1:
                temp.append(inputs[pos])
            pos -= 1
            bitmask >>= 1
        result.append(temp)
    return result

#Test case

print len(subset([2,3,4,5,6]))


# alternative
# from itertools import combinations
# s=[1,2,3]
# print 
# print sum(map(lambda r: list(combinations(s, r)), range(1, len(s)+1)), [])
# [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
'''
L=[2,3,4,5,6]
subs = list([{L[j] for j in range(len(L)) if 1<<j&i} for i in range(1,1<<len(L))])
print len(subs)
'''

# inputs = [1,2,3]
# result = []
# num_of_subset = 1 << len(inputs) # << is a left bitwise shift. It takes the bits and shifts them left n places
# print num_of_subset
# print  1<< len(inputs) # 3 --> 8 
# # for i in xrange(num_of_subset): 
# #     print i