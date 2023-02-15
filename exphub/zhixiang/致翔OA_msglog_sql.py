import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import requests
import urllib3



def 致翔OA_msglog_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    target_url = urldata + "/mainpage/msglog.aspx?user=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    try:
        urllib3.disable_warnings()
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200:
            print(Vcolors.RED +"[+] 存在致翔OA msglog.aspx SQL注入漏洞:{}".format(target_url)+Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在致翔OA msglog.aspx SQL注入漏洞" +Vcolors.ENDC)
    except:
        logging.error("致翔OA_msglog_sql脚本出现异常")

            

   


