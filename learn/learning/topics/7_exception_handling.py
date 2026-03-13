# 7. Python 的异常处理
# 异常处理使用 try-except 块。
# try: 尝试执行代码。
# except: 捕获异常。
# finally: 总是执行。
# raise: 抛出异常。

# 示例代码：演示异常处理
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types"
    finally:
        print("Division attempt completed")

# 测试
print(divide(10, 2))  # 正常
print(divide(10, 0))  # 除零错误
print(divide(10, "a"))  # 类型错误