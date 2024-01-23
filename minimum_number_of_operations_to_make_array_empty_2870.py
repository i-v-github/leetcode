"""
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.


"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numsd = dict()
        for i in nums:
            numsd[i] = numsd.get(i, 0) + 1
        print(numsd)
        count = 0
        for v in numsd.values():
            if v // 3 >= 1:
                count += (v // 3 - 1) + (v - (v // 3 - 1) * 3) // 2
            elif not (v % 2 == 0 or v % 3 == 0):
                return -1
            elif v % 2 == 0 and v // 3 >= 2:
                count += (v // 3 - 1) + (v - (v // 3 - 1) * 3) // 2
            elif v % 2 == 0:
                count += v // 2
            elif v % 3 == 0:
                count += v // 3
            return count



if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]))
    print(s.minOperations(nums=[2, 1, 2, 2, 3, 3]))
    print(s.minOperations(nums=[1, 3, 4, 1, 2, 3, 1]))
    print(s.minOperations(nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))
    print(s.minOperations(nums = [19,19,19,19,19,19,19,19,19,19,19,19,19]))
