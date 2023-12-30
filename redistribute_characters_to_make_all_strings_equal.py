"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.
"""
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        if len(words) == 1:
            return True

        cd = []

        for word in words:
            chars = dict()
            for letter in word:
                chars.update({letter: word.count(letter)})
            cd.append(chars)
        print(cd)
        result_dict = dict()
        for d in cd:
            for key, value in d.items():
                result_dict[key] = result_dict.get(key, 0) + value
        print(result_dict)

        v_list = []

        for v in result_dict.values():
            v_list.append(v)

        print(v_list)

        return (all(element % len(words) == 0 for element in v_list)
                and not any(element == 1 for element in v_list))




if __name__ == '__main__':
    s = Solution()
    print(s.makeEqual(words = ["abc","aabc","bc"]))
    print(s.makeEqual(words = ["ab","a"]))
    print(s.makeEqual(words = ["a","b"]))
    print(s.makeEqual(words = ["b"]))

