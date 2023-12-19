"""
There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

The company requires each employee to work for at least target hours.

You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

Return the integer denoting the number of employees who worked at least target hours.
"""
from typing import List
from functools import reduce


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        i = 0
        for hour in hours:
            if hour >= target:
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2))

