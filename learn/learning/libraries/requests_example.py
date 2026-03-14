# requests - HTTP 请求库
# requests 是 Python 中最流行的 HTTP 请求库。
# 用于发送 HTTP 请求，如 GET, POST 等。
# 简单易用，支持 JSON、文件上传等。
# 需要安装：pip install requests

# 示例代码：发送 GET 请求
import requests

# 发送 GET 请求
response = requests.get('https://httpbin.org/get')

# 检查响应
if response.status_code == 200:
    print("Response status:", response.status_code)
    print("Response JSON:")
    print(response.json())
else:
    print("Request failed with status:", response.status_code)

# 发送 POST 请求
data = {'key': 'value'}
post_response = requests.post('https://httpbin.org/post', json=data)
print("\nPOST Response:")
print(post_response.json())