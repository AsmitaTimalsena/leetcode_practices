'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1 = format(x, 'b')
        y1 = format(y, 'b')

        val = max(len(x1), len(y1))
        a = x1.zfill(val)
        b = y1.zfill(val)
        dist = 0

        for i in range(val):
            if a[i] != b[i]:
                dist += 1

        return dist
        
