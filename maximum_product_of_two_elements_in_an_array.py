"""Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
"""
from typing import List


def maxProduct(nums: List[int]) -> int:
    max = (nums[0]-1)*(nums[1]-1)
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i < j and (nums[i]-1)*(nums[j]-1) > max:
                max = (nums[i]-1)*(nums[j]-1)
    return max


if __name__ == '__main__':
    print(maxProduct([3,4,5,2]))
    print(maxProduct([1,5,4,5]))
    print(maxProduct([3,7]))
