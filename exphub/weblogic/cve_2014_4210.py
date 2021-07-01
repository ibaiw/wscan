#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# CVE-2014-4210
# updated 2019/10/23
# by 0xn0ne
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging


def cve_2014_4210(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vulurl = urldata + 'uddiexplorer/SearchPublicRegistries.jsp'
    vulnhub = requests.get(url=vulurl)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    try:
        if vulnhub.status_code == 200:
            print(Vcolors.RED + "[!] weblogic存在cve_2014_4210漏洞\r" + Vcolors.ENDC)
    
    except Exception as e :
        logging.error("cve_2014_4210脚本出现异常")
