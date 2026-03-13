import pandas as pd

# 示例数据
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'id': [2, 4, 5],
    'age': [25, 30, 22]
})

# INNER JOIN (只保留两个表中都出现的id)
inner_join = pd.merge(df1, df2, on='id', how='inner')
print("INNER JOIN:\n", inner_join)

# LEFT JOIN (保留df1中的全部数据，df2中匹配不上填NaN)
left_join = pd.merge(df1, df2, on='id', how='left')
print("\nLEFT JOIN:\n", left_join)

# RIGHT JOIN (保留df2中的全部数据，df1中匹配不上填NaN)
right_join = pd.merge(df1, df2, on='id', how='right')
print("\nRIGHT JOIN:\n", right_join)

# OUTER JOIN (全部数据都保留，匹配不上填NaN)
outer_join = pd.merge(df1, df2, on='id', how='outer')
print("\nOUTER JOIN:\n", outer_join)