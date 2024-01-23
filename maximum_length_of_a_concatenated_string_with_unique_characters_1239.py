"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
"""

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        Find the maximum length of a concatenated string of unique characters.

        Args:
            arr: List of strings

        Returns:
            int: Maximum length of a concatenated string
        """

        def is_unique(s):
            return len(s) == len(set(s))

        def backtrack(index, path):
            if index == len(arr):
                return len(path)

            # Exclude the current string
            length_without_current = backtrack(index + 1, path)

            # Include the current string if it's unique
            if is_unique(path + arr[index]):
                length_with_current = backtrack(index + 1, path + arr[index])
            else:
                length_with_current = 0

            return max(length_without_current, length_with_current)

        return backtrack(0, "")

if __name__ == '__main__':
    s = Solution()
    print(s.maxLength(arr = ["un","iq","ue"]))
    print(s.maxLength(arr = ["cha","r","act","ers"]))
    print(s.maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]))
    print(s.maxLength(arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))
    print(s.maxLength(arr = ["aa","bb"]))