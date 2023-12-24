"""
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1'
or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating,
while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""


class Solution:
    def minOperations1(self, s: str) -> int:
        lst = list(s)
        count_0 = lst.count('0')
        count_1 = lst.count('1')
        if count_0 == 0 or count_1 == 0:
            return max(count_0, count_1) // 2
        elif count_0 == count_1: # wrong assumption for this branch
           pass
        else:
            j = 0
            for i in range(len(lst) - 1):
                if lst[i] == lst[i+1]:
                    j +=1
            return j

    def minOperations(self, s: str) -> int:
        s1 = ''
        s2 = ''
        i = 0
        for char in s:
            if i%2 == 0:
                s1 += '0'
                s2 += '1'
            else:
                s1 += '1'
                s2 += '0'
            i +=1
        # print(s)
        # print(s1)
        # print(s2)
        # print('-----')
        lst = list(s)
        lst1 = list(s1)
        lst2 = list(s2)
        i = 0
        for char in range(len(lst)):
            if lst[char] != lst1[char]:
                i += 1
        j = 0
        for char in range(len(lst)):
            if lst[char] != lst2[char]:
                j += 1
        return min(i,j)




if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(s = "0100"))
    print(s.minOperations(s = "10"))
    print(s.minOperations(s = "1111"))
    print(s.minOperations(s = "110010"))
    print(s.minOperations(s = "10010100"))
    print(s.minOperations(s = "1100010111"))


