# 6. Python 的面向对象编程
# 面向对象编程 (OOP) 使用类和对象。
# 类是蓝图，对象是实例。
# 类有属性 (变量) 和方法 (函数)。
# 使用 class 关键字定义类。
# __init__ 是构造函数。

# 示例代码：定义类和创建对象
class Person:
    """人 的类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# 创建对象
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.greet())
print(person2.greet())