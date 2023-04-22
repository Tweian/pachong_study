import urllib
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, urlopen
from urllib.error import URLError, HTTPError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center'

p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except urllib.error.URLError as e:
    print(e.reason,sep='\n')
print('--------------------------------------')

try:
    response = urlopen('https://cuiqingcai.com/404')
    print(response.text)
except URLError as e:
    print(e.reason, e.code, e.headers, sep='\n')