# 8. Python 的文件操作
# 文件操作包括打开、读取、写入、关闭文件。
# 使用 open() 函数，模式: 'r' 读, 'w' 写, 'a' 追加。
# 最好使用 with 语句自动关闭文件。
# read() 读取全部, readline() 读一行, readlines() 读所有行。

# 示例代码：读取和写入文件
# 写入文件
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# 读取文件
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# 逐行读取
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Lines:")
    for line in lines:
        print(line.strip())