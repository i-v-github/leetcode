"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

"""
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = dict()
        for winner, loser in matches:
            losers[loser] = losers.get(loser, 0) + 1

        winners = set()
        for winner, loser in matches:
            if winner not in losers:
                winners.add(winner)

        losers = [k for k, v in losers.items() if v == 1]

        return [list(sorted(winners)), (sorted(losers))]


if __name__ == '__main__':
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
    print(s.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
