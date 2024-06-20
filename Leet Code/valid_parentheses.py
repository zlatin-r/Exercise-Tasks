s = input().strip('"')

while len(s) > 0:
    lst = len(s)
    s = s.replace('()', '').replace('{}', '').replace('[]', '')

    if lst == len(s):
        print("False")

print("True")

# class Solution(object):
#    def isValid(self, s):
#        """
#        :type s: str
#        :rtype: bool
#        """
#        while len(s) > 0:
#            lst = len(s)
#            s = s.replace('()', '').replace('{}', '').replace('[]', '')
#            if lst == len(s):
#                return False
#       return True
