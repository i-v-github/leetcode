"""Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.



Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.


Constraints:

1 <= n <= 1000
"""


def totalMoney(n: int) -> int:
    # n // 7, n % 7
    monday = 1
    total_money = 0
    day_money = 0
    weeks = n // 7
    for full_week in range(0, weeks):
        for day in range(1, 8):
            day_money += 1
            total_money += day_money
            # print(f'week: {full_week+1}, day: {day}, day money: {day_money}, total_money: {total_money}')
        monday += 1
        day_money = monday - 1
    # print(monday, total_money)
    day_money = monday - 1
    for day in range(1, n % 7 + 1):
        day_money += 1
        total_money += day_money
        # print(f'day: {day}, day money: {day_money}, total_money: {total_money}')
    return total_money


if __name__ == '__main__':
    print(totalMoney(4))
    print(totalMoney(10))
    print(totalMoney(20))