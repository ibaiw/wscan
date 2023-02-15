import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def JellyfinAny(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    '''
    
    payload
    
    ''' 
   
    try:
        print(Vcolors.RED + "[!] 存在xxx漏洞\r" + Vcolors.ENDC)
            

    except:
        logging.error("xxxx脚本出现异常")


