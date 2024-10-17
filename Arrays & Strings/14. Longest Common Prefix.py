#URL: https://leetcode.com/problems/longest-common-prefix/description/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        largestPrefix = ""

        if len(strs) == 0:
            return largestPrefix

        if len(strs) == 1:
            return strs[0]
        
        index = 0
        minLength = min(len(words) for words in strs)
        while index < minLength:
            matchFound = True
            checkLetter = strs[0][index]
            for i in range(1, len(strs)):
                if checkLetter != strs[i][index]:
                    matchFound = False
                    break
            
            if not matchFound:
                break

            largestPrefix += checkLetter    
            index += 1
        
        return largestPrefix

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    print(result)
