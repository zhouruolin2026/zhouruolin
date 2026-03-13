# 5. Python 的模块和包
# 模块是 .py 文件，包含函数、类等。
# 包是包含 __init__.py 的目录。
# 使用 import 导入模块。
# from module import item 导入特定项。

# 示例代码：导入和使用模块
import math  # 导入标准库模块
from datetime import datetime  # 从模块导入特定类

# 使用 math 模块
print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))

# 使用 datetime
now = datetime.now()
print("Current time:", now)