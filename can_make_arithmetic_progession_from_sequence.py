class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        result = ""
        if len(arr) > 2:
            for i in range(1, len(arr) - 1):
                if abs(arr[i - 1] - arr[i]) == abs(arr[i] - arr[i + 1]):
                    result = True
                else:
                    return False
        else:
            return True
        return result
