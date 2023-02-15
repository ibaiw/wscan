from lib.ModelLoad import ONLoad
from lib import *
import os
import logging

dlist = []
#文件遍历
def FanWeiScan(url):  #函数名与文件名相同，建议为大写字母加上Scan
    for file in os.listdir("./exphub/fanwei/"):  #修改此处为路径名称，建议为小写
        if os.path.splitext(file)[1] == '.py':
            if os.path.join(file) != "__init__.py" and os.path.join(file) != "FanWeiScan.py":     #排除init文件以及主扫描文件OAScan.py文件
                dlist.append(os.path.join(os.path.splitext(file)[0]))
    ONLoad(dlist)
    try:
        for defclass in dlist:
            print(Vcolors.OKGREEN + "[?] 正在执行" + defclass + "脚本检测.......\r" + Vcolors.ENDC)
            exec("from exphub.fanwei.{0} import {1}".format(defclass, defclass))   #此处修改导入的exphub.路径信息
            defclass += "(\'{}\')".format(url)
            exec(defclass)
            
    except Exception as e:
        logging.error("FanWeiScan脚本出现异常")  #修改异常监控名称