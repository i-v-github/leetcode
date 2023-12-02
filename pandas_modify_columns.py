"""
DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+
A company intends to give its employees a pay rise.

Write a solution to modify the salary column by multiplying each salary by 2.

The result format is in the following example.



Example 1:

Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
Output:
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
Explanation:
Every salary has been doubled.
"""

import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees


data = [dict(name="Jack", salary=19666), {"name": "Piper", "salary": 74754}, {"name": "Mia", "salary": 62509},
        {"name": "Ulysses", "salary": 5}]

df = pd.DataFrame(data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(df)
    # print(df['salary'].to_string(index=False))
    # print(df['salary']*2)
    # print(modifySalaryColumn(df))
    print(modifySalaryColumn(df))
