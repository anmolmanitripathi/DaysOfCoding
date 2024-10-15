#URL: https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        subSeqPointer = 0
        for i in range(len(t)):
            if s[subSeqPointer] == t[i]:
                subSeqPointer += 1
                if subSeqPointer == len(s):
                    return True
        
        return False

if __name__ == '__main__':
    word1 = "bhdkc  "
    word2 = "abcd"
    solution = Solution()
    result = solution.isSubsequence(word1, word2)
    print(result)