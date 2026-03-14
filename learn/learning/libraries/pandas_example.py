# pandas - 数据分析库
# pandas 是 Python 中强大的数据分析和操作库。
# 主要用于数据清洗、分析和可视化。
# 核心数据结构：DataFrame (表格) 和 Series (一维数组)。
# 常用操作：读取 CSV、数据筛选、聚合等。

# 示例代码：创建 DataFrame 并进行基本操作
import pandas as pd

# 创建数据
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# 筛选年龄大于 25 的人
filtered = df[df['Age'] > 25]
print("\nFiltered (Age > 25):")
print(filtered)