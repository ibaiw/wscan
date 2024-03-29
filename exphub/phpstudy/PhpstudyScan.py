# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 18:28
@File:  PhpstudyScan.py
@Desc:
'''

from lib.ModelLoad import ONLoad
from lib import *
import os
import logging

dlist = []
#文件遍历
def PhpstudyScan(url):
    for file in os.listdir("./exphub/phpstudy/"):
        if os.path.splitext(file)[1] == '.py':
            if os.path.join(file) != "__init__.py" and os.path.join(file) != "PhpstudyScan.py":
                dlist.append(os.path.join(os.path.splitext(file)[0]))
    ONLoad(dlist)
    try:
        for defclass in dlist:
            print(Vcolors.OKGREEN + "[?] 正在执行" + defclass + "脚本检测.......\r" + Vcolors.ENDC)
            exec("from exphub.phpstudy.{0} import {1}".format(defclass,defclass))
            defclass += "(\'{}\')".format(url)
            exec(defclass)
    except:
        
        logging.error("PhpstudyScan脚本出现异常")