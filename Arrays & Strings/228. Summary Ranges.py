#URL: https://leetcode.com/problems/summary-ranges/description/
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        finalList = []
        
        index = 0
        startRangeIndex = index
        while index < len(nums):
            index += 1
            rangeLength = 1
            while index < len(nums) and nums[startRangeIndex] + rangeLength == nums [index]:
                index += 1
                rangeLength += 1

            if rangeLength == 1:
                finalList.append(str(nums[startRangeIndex]))
            else: 
                finalList.append(f"{nums[startRangeIndex]}->{nums[startRangeIndex] + rangeLength - 1 }")

            startRangeIndex = index

        return finalList
    
        # if len(nums) == 0:
        #     return []
        
        # if len(nums) == 1:
        #     return [str(nums[0])]
        
        # finalList = []
        # startRangeIndex = 0
        # rangeLength = 1
        # for i in range(1, len(nums)):
        #     if (nums[startRangeIndex] + rangeLength) == nums[i]:
        #         rangeLength += 1
        #     else:
        #         if rangeLength == 1:
        #             finalList.append(str(nums[startRangeIndex]))
        #         else: 
        #             finalList.append(f"{nums[startRangeIndex]}->{nums[startRangeIndex] + rangeLength - 1}")

        #         startRangeIndex = i
        #         rangeLength = 1

        # if rangeLength == 1:
        #     finalList.append(str(nums[startRangeIndex]))
        # else: 
        #     finalList.append(f"{nums[startRangeIndex]}->{nums[startRangeIndex] + rangeLength - 1 }")

        # return finalList
 
if __name__ == '__main__':
    nums = [-4,-3,-2,-1,0,1,2,3,4,6,8,9]
    solution = Solution()
    result = solution.summaryRanges(nums)
    print(result)
