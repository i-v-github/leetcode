"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums.count(num) == 2:
                res.append(num)
                break
        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums([1, 2, 2, 4]))
    print(s.findErrorNums([1, 1]))
    print(s.findErrorNums([2, 2]))
    print(s.findErrorNums([1,3,3]))