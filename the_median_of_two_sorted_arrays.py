from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_lst = sorted(nums1 + nums2)
        n = len(merged_lst)

        if n % 2 == 1:
            return float(merged_lst[n //2])
        else:
            return (merged_lst[n // 2 - 1] + merged_lst[n // 2]) /2

sol = Solution()

result = sol.findMedianSortedArrays([5,2],[1,4])

print(result)
