"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
"""

class Solution:
    def maxScore(self, s: str) -> int:
        scores = []
        for i, char in enumerate(list(s)):
            summ = s[0:min(i+1,len(s)-1)].count('0') + s[min(i+1,len(s)-1):len(s)].count('1')
            scores.append(summ)
        return max(scores)



if __name__ == '__main__':
    s = Solution()
    print(s.maxScore(s = "011101"))
    print(s.maxScore(s = "1111"))
    print(s.maxScore(s = "00"))

