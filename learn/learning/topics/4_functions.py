# 4. Python 的函数
# 函数是可重用的代码块，使用 def 关键字定义。
# 函数可以接受参数，返回值。
# 有内置函数，如 print()，len()。
# 可以定义自己的函数。

# 示例代码：定义和调用函数
def add_numbers(a, b):
    """返回两个数的和"""
    return a + b

def greet(name="World"):
    """问候函数，默认参数"""
    return f"Hello, {name}!"

# 调用函数
result = add_numbers(5, 3)
print("Sum:", result)

greeting = greet()
print(greeting)

greeting2 = greet("Alice")
print(greeting2)