class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ""
        l = 0

        for i in range(len(s)):
            if s[i] in sub_string:
                sub_string = ""
            sub_string += s[i]

            if len(sub_string) > l:
                    l = len(sub_string)

        return l
    
result = Solution()

print(result.lengthOfLongestSubstring("dvdf"))
print(result.lengthOfLongestSubstring(" "))
print(result.lengthOfLongestSubstring("abcabcabd"))
print(result.lengthOfLongestSubstring("bbbbbbbb"))
print(result.lengthOfLongestSubstring("pwwkew"))
