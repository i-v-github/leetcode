"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        rl = []
        for l in s:
            try:
                rl.append(s.index(l, min(len(s), s.rindex(l))) - s.index(l))
            except ValueError:
                rl.append(-1)
        if all(el == -1 for el in rl):
            return -1
        else:
            return max(rl) - 1



if __name__ == '__main__':
    s = Solution()
    print(s.maxLengthBetweenEqualCharacters(s = "aa"))
    print(s.maxLengthBetweenEqualCharacters(s = "abca"))
    print(s.maxLengthBetweenEqualCharacters(s = "cbzxy"))
    print(s.maxLengthBetweenEqualCharacters(s ="mgntdygtxrvxjnwksqhxuxtrv"))
    print(s.maxLengthBetweenEqualCharacters(s ="rimkibmvpnhlgtdkazshyilqmywn"))
