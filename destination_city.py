"""You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.



Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
"""
from typing import List


def destCity1(paths: List[List[str]]) -> str:
    """does not work, requires debugging"""
    i = 0
    destination = paths[0][1]
    paths.pop(i)

    for path in paths:
        print('1 ', paths)
        if destination == path[0]:
            destination = path[1]
        else:
            paths.pop(i)
            print('2 ', paths)

    return destination

def destCity(paths: List[List[str]]) -> str:
    s = []
    d = []
    for path in paths:
        s.append(path[0])
        d.append(path[1])
    common = list(set(d).intersection(s))
    for dest in common:
        d.pop(d.index(dest))
    return d[0]



if __name__ == '__main__':
    print(destCity([["B", "C"], ["D", "B"], ["C", "A"]]))
    print(destCity([["C", "A"]]))
