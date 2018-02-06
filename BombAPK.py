#!/usr/bin/python
# -*- coding:utf-8 -*-

import argparse
import subprocess


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\33[93m'
    WARNING = '\033[91m'
    FAIL = '\033[35m'
    ENDC = '\033[0m'


class Tools:
    def __init__(self):
        self.apktool = '2.3.1'
        self.smali = '2.2.2'
        self.baksmali = '2.2.2'
        self.dex2jar = '2.1'
        self.jd_gui = '1.4.0'

    def list_all_member(self):
        for name, value in vars(self).items():
            print('%s : %s' % (name, value))


class BombAPK(object):
    def __init__(self, ToolID, Input, Output):
        self.ToolID = ToolID
        self.Input = Input
        self.Output = Output
        self.flag = 0

    def run(self, cmd):
        print(Color.OKBLUE + "[+] Current command: " + cmd + Color.ENDC)
        subprocess.call(cmd, shell=True)
        # try捕捉处理异常
        self.flag = 1

    def main(self):
        # 输入信息
        if self.Input != None:
            print(Color.HEADER +
                  "[+] BombBombAPK ready to start." + Color.ENDC)
            print(Color.OKBLUE +
                  "[+] Current command's input: " + self.Input + Color.ENDC)
        if self.Output != None:
            print(Color.OKBLUE +
                  "[+] Current command's output: " + self.Output + Color.ENDC)
        # 工具调用
        if self.ToolID == "0":
            print(Color.WARNING +
                  "[-] The specified tool ID number" + Color.ENDC)
            print(Color.WARNING +
                  "[-] Please look at the help document [-h]" + Color.ENDC)
        elif self.ToolID == "1":
            if self.Output != None:
                cmd = "java -jar bin/apktool.jar d -f " + self.Input + " -o " + self.Output
            else:
                cmd = "java -jar bin/apktool.jar d -f " + \
                    self.Input + " -o " + self.Input[:-4] + "-debug"
            self.run(cmd)
        elif self.ToolID == "2":
            if self.Output != None:
                cmd = "java -jar bin/apktool.jar b " + self.Input + " -o " + self.Output
            else:
                cmd = "java -jar bin/apktool.jar b " + \
                    self.Input + " -o " + self.Input[:-4] + "-debug.apk"
            self.run(cmd)
        elif self.ToolID == "3":
            if self.Output != None:
                cmd = "java -jar bin/signapk.jar bin/testkey.x509.pem bin/testkey.pk8 " + \
                    self.Input + " " + self.Output
            else:
                cmd = "java -jar bin/signapk.jar bin/testkey.x509.pem bin/testkey.pk8 " + \
                    self.Input + " " + self.Input[:-4] + "-S.apk"
            self.run(cmd)
        elif self.ToolID == "4":
            if self.Output != None:
                cmd = "unzip " + self.Input + " classes.dex -d " + self.Output
            else:
                cmd = "unzip " + self.Input + \
                    " classes.dex -d " + self.Input[:-4] + "-dex"
            self.run(cmd)
        elif self.ToolID == "5":
            if self.Output != None:
                cmd = "bash bin/dex2jar/d2j-dex2jar.sh --force " + \
                    self.Input + " -o " + self.Output
            else:
                cmd = "bash bin/dex2jar/d2j-dex2jar.sh --force " + \
                    self.Input + " -o " + self.Input[:-4] + ".jar"
            self.run(cmd)
        elif self.ToolID == "6":
            cmd = "java -jar bin/jd-gui.jar " + self.Input
            self.run(cmd)
        elif self.ToolID == "7":
            if self.Output != None:
                cmd = "bin/zipalign -f -v 4 " + \
                    self.Input + " " + self.Output
            else:
                cmd = "bin/zipalign -f -v 4 " + \
                    self.Input + " " + self.Input[:-4] + "-Z.apk"
            self.run(cmd)
        elif self.ToolID == "10":
            cmd = "bash bin/AmStart " + self.Input
            self.run(cmd)
        # 结束提示
        if self.flag == 1:
            print(Color.HEADER +
                  "[+] This command completed execution." + Color.ENDC)


if __name__ == '__main__':
    banner = '''\

      /\_/\          ____                  _       _    ____  _  __
    =( °w° )=       | __ )  ___  _ __ ___ | |__   / \  |  _ \| |/ /
   . ((   )) .      |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ | |_) | ' / 
  \\  )   (  //      | |_) | (_) | | | | | | |_) / ___ \|  __/| . \ 
   \\(__ __)//       |____/ \___/|_| |_| |_|_.__/_/   \_\_|   |_|\_\\
    
    Usage: python BombAPK.py [-h] -t[ToolID] -i[Input] [options]
    -t [ToolID] List:
            1 = apktool d
            2 = apktool b
            3 = signapk
            4 = classes.dex
            5 = dex2jar
            6 = jd-gui
            7 = zipalign
            10 = AmStart
    '''
    print(Color.OKYELLOW + banner + Color.ENDC)
    parser = argparse.ArgumentParser(
        description="Some common assembler / disassembler tools in Android development")
    # 可选参数
    parser.add_argument('-t', '--tool', dest="ToolID",
                        help="Selectable tools", type=str, choices=['0', '1', '2', '3', '4', '5', '6', '7', '10'], default='0')
    parser.add_argument('-i', '--input', dest="Input",
                        help="Source file or source directory", type=str)
    parser.add_argument('-o', '--output', dest="Output",
                        help="Destination file or destination directory", type=str)
    # 所有工具的版本号
    parser.add_argument('-v', '--version', dest="Version",
                        help="The current version number of all the tools", action="store_true")
    args = parser.parse_args()
    bombapk = BombAPK(args.ToolID, args.Input, args.Output)
    if args.Version:
        Tools().list_all_member()
    bombapk.main()
