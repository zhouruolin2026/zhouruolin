# 3. Python 的流程控制
# 流程控制包括条件语句 (if-else)、循环 (for, while)。
# if 语句：根据条件执行代码。
# for 循环：遍历序列。
# while 循环：条件为真时重复执行。

# 示例代码：演示 if-else 和循环
number = 10

# if-else
if number > 5:
    print("Number is greater than 5")
else:
    print("Number is 5 or less")

# for 循环
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# while 循环
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1