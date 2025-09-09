class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ""
        all_substrings = []
        max_l = 0
        longest_string = ""

        for i in range(len(s)):
            for b in range(len(s[:i])):

                sub_string = s[b:i]
                all_substrings.append(sub_string)

        return max_l, longest_string, all_substrings
    
result = Solution()

print(result.lengthOfLongestSubstring("abcabcabd"))
print(result.lengthOfLongestSubstring("dvdf"))
print(result.lengthOfLongestSubstring(" "))
print(result.lengthOfLongestSubstring("bbbbbbbb"))
print(result.lengthOfLongestSubstring("pwwkew"))
