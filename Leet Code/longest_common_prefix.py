strs = ["flower", "flow", "flight"]
lst = list(zip(*strs))
prefix = ""

for i in lst:
    if len(set(i)) == 1:
        prefix += i[0]
    else:
        break

print(prefix)


# class Solution(object):
#    def longestCommonPrefix(self, strs):
#        """
#        :type strs: List[str]
#        :rtype: str
#        """
#        lst = list(zip(*strs))
#        prefix = ""

#        for i in lst:
#            if len(set(i)) == 1:
#                prefix += i[0]
#            else:
#                break
#
#       return (prefix)
