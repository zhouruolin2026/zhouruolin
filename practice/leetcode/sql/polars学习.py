import polars as pl

# polars学习

import polars as pl

# 示例表（我们后续都用这个 df 演示）
df = pl.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 28, 22],
    "city": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Hangzhou"],
    "score": [88.5, 92.0, 78.5, 95.0, 65.0]
})

print(df)

# select id, name from df;
print(df.select(["id", "name"]))

# select id, name as s_name from df;
print(df.select([pl.col("id"), pl.col("name").alias("s_name")]))

# select id, age, age % 2 as jiou from df;
df2 = df.select([pl.col("id"), pl.col("age"), (pl.col("age") % 2).alias("jiou")])
print(df2)

# left join
