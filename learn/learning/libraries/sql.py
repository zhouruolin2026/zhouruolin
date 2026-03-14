# sql - 数据库操作
# SQL 是结构化查询语言，用于管理关系型数据库。
# 在 Python 中，可以使用 sqlite3 模块进行 SQL 操作。
# sqlite3 是内置模块，无需安装。
# 基本操作：连接数据库、创建表、插入数据、查询数据。

# 示例代码：使用 sqlite3 创建表并插入查询数据
import sqlite3

# 连接到数据库 (如果不存在会创建)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# 插入数据
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 30))

# 查询数据
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Users:")
for row in rows:
    print(row)

# 提交并关闭
conn.commit()
conn.close()