'''
ou are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
'''


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        # Method 1
        s1 = s.replace('-','').upper()
        i = len(s1)
        group = []
        while i>0:
            group.append(s1[max(i-k,0):i])
            i -= k

        group = group[::-1]
        res = '-'.join(group)
        return res
        
        # Method 2
        s1 = s1[::-1]
        val = [  s1[i:i+k] for i in range(0, len(s1),k)]
        res = '-'.join(values[::-1] for values in val[::-1])
        return res
