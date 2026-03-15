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


# 人工总结
# # pandas学习

# pandas 是 Python 中强大的数据分析库，主要用于数据清洗、分析和可视化。
# 核心数据结构：DataFrame (表格) 和 Series (一维数组)。
# 常用操作：读取 CSV、数据筛选、聚合等。

# ## 最实用操作

# 1. 获取数据 insert
# 2. 查数据 select
# 3. 改数据 update
# 4. 删数据 delete

# 使用例子

# 先读取当前py文件目录路径
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建CSV文件路径
csv_file_path = os.path.join(script_dir, 'data.csv')

print("py文件目录路径:", script_dir)
print("CSV文件路径:", csv_file_path)
print("当前工作目录:", os.getcwd()) # 执行python命令所在的目录路径，在哪个目录下执行python命令，就会显示哪个目录路径 -- 这个目录很不确定

# 1. 获取源数据
# 只需要知道pandas可以从外部文件或内部数据结构中获取数据，就可以了

df = pd.read_csv(csv_file_path)
print("原始数据:")
print(df)
print(type(df))

# 从内部数据结构中获取数据
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo'],
    'Salary': [70000, 80000, 90000]
}
df = pd.DataFrame(data)
print(df)
print(type(df))

