class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0

        if len(nums)>1:
            for i in range(len(nums)-1):
                if target in nums:
                    return nums.index(target)
                elif nums[i] < target < nums[i+1]:
                    return i+1
                elif target > nums[-1] and target not in nums:
                    return len(nums)
        else:
            if target > nums[0]:
                return 1
            else:
                return 0
        return result