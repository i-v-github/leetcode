"""
You are given positive integers n and m.

Define two integers, num1 and num2, as follows:

num1: The sum of all integers in the range [1, n] that are not divisible by m.
num2: The sum of all integers in the range [1, n] that are divisible by m.
Return the integer num1 - num2.
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # lst = list(range(n+1))
        # num1 = sum(list(filter(lambda x: x if x%m != 0 else 0, lst)))
        # num2 = sum(list(filter(lambda x: x if x%m == 0 else 0, lst)))
        # return num1 - num2
        return sum(list(map(lambda x: x if x%m != 0 else -x, list(range(n+1)))))


if __name__ == '__main__':
    s = Solution()
    print(s.differenceOfSums(n = 10, m = 3))

