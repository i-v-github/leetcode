"""
"""

import pandas as pd

data1 = [{
      "student_id": 1,
      "name": "Mason",
      "age": 8
    },
    {
      "student_id": 2,
      "name": "Ava",
      "age": 6
    },
    {
      "student_id": 3,
      "name": "Taylor",
      "age": 15
    },
    {
      "student_id": 4,
      "name": "Georgia",
      "age": 17
    }]

data2 = [
    {
        "student_id": 5,
        "name": "Leo",
        "age": 7
    },
    {
        "student_id": 6,
        "name": "Alex",
        "age": 7
    }
]

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis = 0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(concatenateTables(df1, df2))