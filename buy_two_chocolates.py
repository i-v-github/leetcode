"""
You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.
"""
from typing import List
from functools import reduce


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        two_choco = prices[0] + prices[1]
        if two_choco <= money:
            return money-two_choco
        else:
            return money


if __name__ == '__main__':
    s = Solution()
    print(s.buyChoco(prices = [1,2,2], money = 3))

