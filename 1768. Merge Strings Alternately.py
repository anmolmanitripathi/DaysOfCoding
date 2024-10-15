#URL: https://leetcode.com/problems/merge-strings-alternately/description/
from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mixedWord = ""
        for i in range(min(len(word1), len(word2))):
            mixedWord += word1[i] + word2[i]

        if len(word1) > len(word2):
            mixedWord += word1[len(word2):]
        
        if len(word1) < len(word2):
            mixedWord += word2[len(word1):]

        return mixedWord
        


if __name__ == '__main__':
    word1 = ""
    word2 = ""
    solution = Solution()
    result = solution.mergeAlternately(word1, word2)
    print(result)