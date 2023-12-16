"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        tl = list(t)
        for letter in s:
            if letter in tl:
                tl.pop(tl.index(letter))
            else:
                return False
        return True
    else:
        return False



if __name__ == '__main__':
    print(isAnagram(s = "anagram", t = "nagaram"))
    print(isAnagram(s = "rat", t = "car"))