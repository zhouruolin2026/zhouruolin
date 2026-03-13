# 1. Python 使用规范
# Python 使用规范包括代码风格、命名约定和最佳实践。
# 主要遵循 PEP 8 风格指南。
# 使用 4 个空格缩进，不要使用制表符。
# 变量名使用小写字母和下划线，如 my_variable。
# 函数名也使用小写字母和下划线，如 my_function。
# 类名使用 PascalCase，如 MyClass。

# 示例代码：演示正确的命名和缩进
def greet_user(name):
    """问候用户的函数"""
    message = f"Hello, {name}!"
    print(message)

# 调用函数
greet_user("Alice")

# **重点总结**
# python的使用规则就两个点
# 1. python的注释是前面加#号
# 2. python的代码块通过缩进来表示，通常使用4个空格

print("Hello, World!")  # 打印问候语 这句话是注释

if 1 > 0:
    print("1 > 0") # 这行代码属于 if 语句块，因为它缩进了4个空格
    # 只有if条件成立的时候才会执行

print("程序结束") # 这行代码和 上面的if语句就没有任何从属关系了
# 无论if条件是否成立，这条语句都会执行