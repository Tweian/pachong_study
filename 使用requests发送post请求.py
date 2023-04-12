import requests

# 爬取地址
url = "https://fanyi.baidu.com/sug"

# 数据字典
data = {"kw": input("请输入需要翻译的内容：")}

# 发送post请求
resp = requests.post(url, data=data)

# print(resp.text) # 拿到页面源代码

# 如果返回的数据是json，可直接resp.json
print(resp.json())