# 获取网站代码
import urllib.request
response = urllib.request.urlopen('http://v.qq.com')  # 网址任意，获取介绍代码
html = response.read().decode('utf-8')
print(html)
