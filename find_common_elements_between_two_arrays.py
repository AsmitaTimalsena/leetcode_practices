'''
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].
Example 1:

Input: nums1 = [2,3,2], nums2 = [1,2]

Output: [2,1]
'''

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst1 = []
        lst2 = []
        
        for i in nums1:
            if i in nums2:
                lst1.append(i)
        
        for j in nums2:
            if j in nums1:
                lst2.append(j)

        lst = [len(lst1), len(lst2)]
        return lst
