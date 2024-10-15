#URL: https://leetcode.com/problems/find-closest-number-to-zero/description/
from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closestNumber = nums[0]

        if len(nums) == 1:
            return closestNumber

        for i in range(1,len(nums)):
            currentNumber = nums[i]
            if (abs(currentNumber) < abs(closestNumber)):
                closestNumber = currentNumber

            elif (abs(currentNumber) == abs(closestNumber)):
                closestNumber = currentNumber  if currentNumber > closestNumber else closestNumber
        return closestNumber


if __name__ == '__main__':
    nums = [-1,7,1]
    solution = Solution()
    result = solution.findClosestNumber(nums=nums)
    print(result)