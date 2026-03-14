# pytest - 测试框架
# pytest 是 Python 的强大测试框架。
# 用于编写和运行测试用例。
# 特点：简单语法、自动发现测试、丰富的断言。
# 测试函数以 test_ 开头。
# 使用 assert 进行断言。

# 示例代码：编写简单测试
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_fail():
    # 这个会失败，用于演示
    # assert add(2, 3) == 6  # 注释掉以避免失败
    pass

if __name__ == "__main__":
    test_add()
    test_add_fail()
    print("Tests completed")