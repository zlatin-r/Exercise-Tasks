class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)

        return string == string[::-1]

result = Solution()
print(result.isPalindrome(-121))
