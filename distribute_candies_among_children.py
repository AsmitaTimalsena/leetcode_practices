'''
  You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

 

Example 1:

Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
'''
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = []
        for i in range(limit+1):
            for j in range(limit+1):
                for k in range(limit+1):
                    if (i+j+k)==n:
                        result.append([i,j,k])
        
        return len(result)
        
