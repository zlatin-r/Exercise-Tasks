class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
result = Solution()
print(result.lengthOfLongestSubstring("dvdf"))

print(result.lengthOfLongestSubstring("abcabcbb"))
print(result.lengthOfLongestSubstring(" "))
print(result.lengthOfLongestSubstring("bbbbbbbb"))
print(result.lengthOfLongestSubstring("pwwkew"))
