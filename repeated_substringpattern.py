'''
iven a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
'''



class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        n = len(s)
        for i in range(1,n):
            if n % i == 0:
                sub = s[:i]
                if sub * (n // i) == s:
                    return True
        
        return False



        '''s = "abab"
substring = set()
n = len(s)
for i in range(0, n):
    for j in range(i+1,n+1):
        substring.add(s[i:j])


lst = list(substring)
i = 0
while len(check) != n:
    check = ""
    check += lst[i]
    if check == s:
        result = "True"
    else:
        result = "False"
       
    
    i += 1
    
print(result)'''
