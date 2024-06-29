numbers = [1, 5, 0, 3, 5]


def Solution(nums: list[int]) -> int:
    nums = set(nums)
    nums.discard(0)
    return len(nums)


print(Solution(numbers))
