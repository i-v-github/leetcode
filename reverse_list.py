"""
Simple revere list exersice
"""
from typing import List


class Solution:
    def reverse_list(self, nums: List[int]) -> List[int]:
        return nums[::-1]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = Solution()
    assert s.reverse_list([1,2,3,4,5]) == [5,4,3,2,1]
    print(s.reverse_list([1,2,3,4,5]))