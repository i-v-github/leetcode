"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = s[n // 2:]
        b = s[:n // 2]
        return sum(count.lower() in 'aeiou' for count in a) == sum(count.lower() in 'aeiou' for count in b)


if __name__ == '__main__':
    s = "book"
    print(Solution().halvesAreAlike(s))