'''
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

Example 1:

Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
Example 2:

Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
 

'''
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = { }
        flat = [element for row in grid for element in row]
        for i in flat:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        
        n = len(grid)
        twice = [key for key,value in count.items() if value>1]
        for k in range(1, n*n+1):
            if k not in flat: #can also do if k in count for repeated check
                twice.append(k)
        
        return twice

        
