class Solution:
    def plusOne(digits):
        strings = ""
        for number in digits:
            strings += str(number)

        temp = str(int(strings) + 1)

        return [int(temp[i]) for i in range(len(temp))]


print(Solution.plusOne([9]))
