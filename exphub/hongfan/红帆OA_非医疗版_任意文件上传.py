import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3

def 红帆OA_非医疗版_任意文件上传(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    target_url1 = urldata + "/ioffice/prg/set/Report/ioRepPicAdd.aspx"
    data = '{ioffice}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-type": "application/x-www-form-urlencoded"
    }
    try:
        urllib3.disable_warnings()
        res1 = requests.post(url=target_url1, headers=headers, data=data, verify=False)
        if res1.status_code == 200:
            print(Vcolors.RED + "[+] 暂无exp，存在红帆任意文件上传:{}".format(target_url1) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在红帆任意文件上传" + Vcolors.ENDC)
    except Exception as e:
        logging.error("红帆OA_非医疗版_任意文件上传脚本出现异常")



