# UA：user-Angent(请求载体的身份标识) 可以作为反爬机制即：UA伪装
# UA检测：门户网站的服务器就会检测相应的身份标识，如果检测到请求的载体身份标识为某一款浏览器时
# 说明该请求是一个正常的请求。但是，如果检测到的载体身份标识不是基于某一款浏览器时
# 则说明为不是正常的请求（即：爬虫），则服务器就很可能拒绝该次请求
import requests  # 导入模块
if __name__ == "__main__":
    # UA伪装防止被检测：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    # 上方利用进入搜狗搜索波晓张界面，右键检查找到network 中的web，找前缀User-Agent，复制后面的内容
    url = 'http://www.sogou.com/web'  # 指定的url并且以字符串的形式
    # 处理url携带的参数：封装到字典
    kw = input('enter a word:')
    param = {
        'query':kw           # 字典
    }
    # 对应的url发起的请求是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    # 使用get请求，用response接受请求响应第三步
    page_text = response.text                # 获取响应对象，返回值使用page接收
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)                 # 把源码写入本地文件
    print(fileName,'保存成功！！！')              # 打印提示
