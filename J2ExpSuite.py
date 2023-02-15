# encoding: utf-8

import multiprocessing
import sys
from lib import *
from exphub import *

#程序开始
if __name__ == '__main__':
    #判断py版本
    if sys.version_info.major < 3:
        sys.stdout.write(Vcolors.PURPLE + "J2ExpSuite 仅支持Python 3.x版本~\n" + Vcolors.ENDC)
        exit()
    #模块部分
    import argparse
    import pyfiglet

    #头部信息部分
    ascii_banner = pyfiglet.figlet_format("J2.ExpSuite")
    print(Vcolors.RED + ascii_banner+Vcolors.ENDC)
    print(Vcolors.OKBLUE + "\t\t\t\tPower by JE2Se" +"   "+ Vcolors.PURPLE + "V1.0" +"\n" +Vcolors.ENDC)
    parser = argparse.ArgumentParser()

    #脚本执行帮助部分
    print(Vcolors.PURPLE + "\t~请输入 -h 获取命令帮助~" + "\n" + Vcolors.ENDC +Vcolors.OKBLUE)
    parser.add_argument("-u" , "--url",type=str, help="填写待测试的URL链接~~(必填)")
    arser.add_argument("-tm" , "--tomcat", help='添加 -tomcat 参数，将进行Tomcat漏洞检测  ~~', action='store_true')
    parser.add_argument("-ps", "--phpstudy", help='添加 -phpstudy 参数，将进行PhpStudy后门漏洞检测  ~~', action='store_true')
    parser.add_argument("-je", "--jellyfin", help='添加 -jellyfin 参数，将进行jellyfin漏洞检测  ~~', action='store_true')
    parser.add_argument("-tq", "--tianqing", help='添加 -tianqing 参数，将进行天擎漏洞检测  ~~', action='store_true')
    parser.add_argument("-zy", "--zhiyuan", help='添加 -zhiyuan 参数，将进行致远漏洞检测  ~~', action='store_true')
    parser.add_argument("-yy", "--yiyou", help='添加 -yiyou 参数，将进行亿邮漏洞检测  ~~', action='store_true')
    parser.add_argument("-yu", "--yongyou", help='添加 -yongyou 参数，将进行用友漏洞检测  ~~', action='store_true')
    parser.add_argument("-fw", "--fanwei", help='添加 -fanwei 参数，将进行泛微漏洞检测  ~~', action='store_true')
    parser.add_argument("-td", "--tongda", help='添加 -tongda 参数，将进行通达漏洞检测  ~~', action='store_true')
    parser.add_argument("-fr", "--fanruan", help='添加 -fanruan 参数，将进行帆软漏洞检测  ~~', action='store_true')
    parser.add_argument("-ht", "--huatian", help='添加 -huatian 参数，将进行华天动力漏洞检测  ~~', action='store_true')
    parser.add_argument("-jh", "--jinhe", help='添加 -jinhe 参数，将进行金和漏洞检测  ~~', action='store_true')
    parser.add_argument("-ll", "--lanling", help='添加 -lanling 参数，将进行蓝凌漏洞检测  ~~', action='store_true')
    parser.add_argument("-ql", "--qilai", help='添加 -qilai 参数，将进行启莱漏洞检测  ~~', action='store_true')
    parser.add_argument("-xd", "--xindian", help='添加 -xidian 参数，将进行新点漏洞检测  ~~', action='store_true')
    parser.add_argument("-ym", "--yimi", help='添加 -yimi 参数，将进行一米漏洞检测  ~~', action='store_true')
    parser.add_argument("-wh", "--wanhu", help='添加 -wanhu 参数，将进行万户漏洞检测  ~~', action='store_true')
    parser.add_argument("-hf", "--hongfan", help='添加 -hongfan 参数，将进行红帆漏洞检测  ~~', action='store_true')
    parser.add_argument("-jd", "--jindie", help='添加 -jindie 参数，将进行金蝶漏洞检测  ~~', action='store_true')
    parser.add_argument("-zx", "--zhixiang", help='添加 -zhixiang 参数，将进行致翔漏洞检测  ~~', action='store_true')
    parser.add_argument('-f', "--file",  help='Target Url File', type=argparse.FileType('r'))
    args = parser.parse_args()
    params = vars(args)

    #URL处理
    if args.url:
        url=args.url
        print(Vcolors.BROWN + " 感谢使用J2ExpSuite工具，正在运行，参数分析中......" + Vcolors.ENDC)
        print(Vcolors.CYAN + "[+] 待测试的链接为：" + Vcolors.ENDC + Vcolors.RED + url + Vcolors.ENDC)
        #导入文件处理簇
        if args.tomcat:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED +"Tomcat漏洞检测" + Vcolors.ENDC)
            TomcatScan(url)
        if args.phpstudy:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "PhpStudy漏洞检测" + Vcolors.ENDC)
            PhpstudyScan(url)
        if args.jellyfin:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "jellyfin漏洞检测" + Vcolors.ENDC)
            JellyfinScan(url)
        if args.tianqing:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "天擎漏洞检测" + Vcolors.ENDC)
            TianqingScan(url)
        if args.zhiyuan:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  致远漏洞检测" + Vcolors.ENDC)
            ZhiyuanScan(url)
            
        if args.yiyou:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  亿邮漏洞检测" + Vcolors.ENDC)
            YiyouScan(url)
        if args.yongyou:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  用友漏洞检测" + Vcolors.ENDC)
            YongYouScan(url)
        if args.fanwei:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  泛微漏洞检测" + Vcolors.ENDC)
            FanWeiScan(url)
        if args.tongda:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  通达漏洞检测" + Vcolors.ENDC)
            TdScan(url)
        if args.fanruan:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  帆软漏洞检测" + Vcolors.ENDC)
            FanRuanScan(url)
        if args.huatian:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  华天动力漏洞检测" + Vcolors.ENDC)
            HuaTianScan(url)
        if args.jinhe:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  金和漏洞检测" + Vcolors.ENDC)
            HuaTianScan(url)
        if args.lanling:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  蓝凌漏洞检测" + Vcolors.ENDC)
            LanLingScan(url)
        if args.qilai:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  启莱漏洞检测" + Vcolors.ENDC)
            QiLaiScan(url)
        if args.xindian:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  新点漏洞检测" + Vcolors.ENDC)
            XinDianScan(url)
        if args.yimi:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  一米漏洞检测" + Vcolors.ENDC)
            YiMiScan(url)
        if args.wanhu:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  万户漏洞检测" + Vcolors.ENDC)
            WanHuScan(url)
        if args.hongfan:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  红帆漏洞检测" + Vcolors.ENDC)
            HongFanScan(url)
        if args.jindie:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  金蝶漏洞检测" + Vcolors.ENDC)
            JinDieScan(url)
        if args.zhixiang:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "  致翔漏洞检测" + Vcolors.ENDC)
            ZhiXiangScan(url)

        print(Vcolors.CYAN + "[.]-----------扫描结束，感谢使用----------" + Vcolors.ENDC)
