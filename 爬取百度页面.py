import requests  # 导入模块
if __name__ == "__main__":
    url = 'https://www.baidu.com/'           # 指定的url并且以字符串的形式
    response = requests.get(url=url)         # 使用get请求，用response接受请求响应第三步
    page_text = response.text                # 获取响应对象，返回值使用page接收
    print(page_text)                         # 测试
    with open('./baidu.html','w',encoding='utf-8') as fp:
        fp.write(page_text)                 # 把源码写入本地文件
    print('爬取数据结束！！！')