#URL: https://leetcode.com/problems/roman-to-integer/description/
from typing import List

class Solution:
    def __init__(self):
        self.romanCovertion = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def romanToInt(self, s: str) -> int:
        preIndex = len(s) - 1
        totalValue = self.romanCovertion[s[preIndex]]
        for i in range(len(s)-2, -1, -1):
            currentValue = self.romanCovertion[s[i]]
            if currentValue < self.romanCovertion[s[preIndex]]:
                totalValue = totalValue - currentValue
            else:
                totalValue = totalValue + currentValue
                preIndex = i

        return totalValue

if __name__ == '__main__':
    word1 = "VIII"
    solution = Solution()
    result = solution.romanToInt(word1)
    print(result)