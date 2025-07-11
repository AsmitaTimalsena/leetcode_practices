'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lst = []
        temp = []

        for val in nums:
            if val == 0:
                if temp:
                    lst.append(temp)
                    temp = []
            else:
                temp.append(val)
        
        if temp:
            lst.append(temp)
        if not lst:
            return 0
        
        res = max(lst, key=len)
        return len(res)
        
