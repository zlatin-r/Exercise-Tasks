class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ""
        l = 0

        for ch in s:
            if ch in sub_string:
                if len(sub_string) > l:
                    l = len(sub_string)
                
                break
            sub_string += ch

