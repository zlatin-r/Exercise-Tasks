class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub_string = ""
        max_l = 0
        longest_sub_string = ""
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub_string = s[i:j]

                if sub_string == sub_string[::-1] and len(sub_string) > max_l:
                    longest_sub_string = sub_string
                    max_l = len(sub_string)

        return longest_sub_string


sol = Solution()
result1 = sol.longestPalindrome("babad")
result2 = sol.longestPalindrome("cbbd")

print(result1)
print(result2)
