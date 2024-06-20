class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        result = 0
        if needle == "":
            return 0
        if len(haystack) >= len(needle):

            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i + len(needle)] == needle:
                    result = int(i)
                    break
                else:
                    result = -1
        else:
            return -1
        return result
