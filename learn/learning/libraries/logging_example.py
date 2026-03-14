# log - 日志记录
# logging 是 Python 内置的日志模块。
# 用于记录程序运行时的信息、警告、错误等。
# 级别：DEBUG, INFO, WARNING, ERROR, CRITICAL。
# 可以输出到控制台或文件。

# 示例代码：配置日志并记录消息
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='example.log',
    filemode='w'
)

# 记录不同级别的日志
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print("Logs have been written to example.log")