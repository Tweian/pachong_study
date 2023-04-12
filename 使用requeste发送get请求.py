import requests

# 爬取网站地址
url = "http://www.baidu.com"

# 发送请求
resp = requests.get(url)

# 设置字符集
resp.encoding = 'utf-8'

# print(resp.text) #拿到页面源代码

# 把页面源代码保存在文件中
with open("baidu.html", mode="w", encoding='utf-8') as f:
    f.write(resp.text)

print("over!!")