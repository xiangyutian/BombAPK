# BombAPK

此脚本使用Python集成了Android逆向中常用的一些工具，力求省去各自繁琐的命令，方便自写脚本的整合，最终在一个终端下完成各种工具的调用。

## 工具

- APK反编译：apktool d
- 回编译APK：apktool b
- APK签名：signapk
- 提取dex：unzip
- dex转jar：dex2jar
- JAVA反编译：jd-gui
- APK优化：zipalign
- 入口Activity：AmStart

## 使用

查看帮助文档：

```
[Go0s]: ~/Desktop/BombAPK ✗ master
➜  python BombAPK.py -h

      /\_/\          ____                  _       _    ____  _  __
    =( °w° )=       | __ )  ___  _ __ ___ | |__   / \  |  _ \| |/ /
   . ((   )) .      |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ | |_) | ' / 
  \  )   (  //      | |_) | (_) | | | | | | |_) / ___ \|  __/| . \ 
   \(__ __)//       |____/ \___/|_| |_| |_|_.__/_/   \_\_|   |_|\_\
    
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
    
usage: BombAPK.py [-h] [-t {0,1,2,3,4,5,6,7,10}] [-i INPUT] [-o OUTPUT] [-v]

Some common assembler / disassembler tools in Android development

optional arguments:
  -h, --help            show this help message and exit
  -t {0,1,2,3,4,5,6,7,10}, --tool {0,1,2,3,4,5,6,7,10}
                        Selectable tools
  -i INPUT, --input INPUT
                        Source file or source directory
  -o OUTPUT, --output OUTPUT
                        Destination file or destination directory
  -v, --version         The current version number of all the tools
```

查看其中工具的版本号：

```
[Go0s]: ~/Desktop/BombAPK ✗ master
➜  python BombAPK.py -v
dex2jar : 2.1
jd_gui : 1.4.0
smali : 2.2.2
baksmali : 2.2.2
apktool : 2.3.1
[-] The specified tool ID number
[-] Please look at the help document [-h]
```

APK反编译：

```
[Go0s]: ~/Desktop/BombAPK ✗ master
➜  python BombAPK.py -t 1 -i crackme.apk 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: java -jar bin/apktool.jar d -f crackme.apk -o crackme-debug
I: Using Apktool 2.3.1 on crackme.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /Users/go0s/Library/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
[+] This command completed execution.
```

回编译APK：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 2 -i crackme-debug 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme-debug
[+] Current command: java -jar bin/apktool.jar b crackme-debug -o crackme-debug.apk
I: Using Apktool 2.3.1
I: Checking whether sources has changed...
I: Smaling smali folder into classes.dex...
I: Checking whether resources has changed...
I: Building resources...
I: Building apk file...
I: Copying unknown files/dir...
[+] This command completed execution.
```

APK签名：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 3 -i crackme.apk 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: java -jar bin/signapk.jar bin/testkey.x509.pem bin/testkey.pk8 crackme.apk crackme-S.apk
[+] This command completed execution.
```

提取dex：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 4 -i crackme.apk 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: unzip crackme.apk classes.dex -d crackme-dex
Archive:  crackme.apk
  inflating: crackme-dex/classes.dex  

[+] This command completed execution.
```

dex转jar：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 5 -i crackme-dex/classes.dex 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme-dex/classes.dex
[+] Current command: bash bin/dex2jar/d2j-dex2jar.sh --force crackme-dex/classes.dex -o crackme-dex/classes.jar
dex2jar crackme-dex/classes.dex -> crackme-dex/classes.jar
[+] This command completed execution.
```

JAVA反编译：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 6 -i crackme-dex/classes.jar 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme-dex/classes.jar
[+] Current command: java -jar bin/jd-gui.jar crackme-dex/classes.jar
[+] This command completed execution.
```

APK优化：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 7 -i crackme.apk    
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: bin/zipalign -f -v 4 crackme.apk crackme-Z.apk
Verifying alignment of crackme-Z.apk (4)...
      62 res/layout/activity_main.xml (OK - compressed)
     554 res/menu/main.xml (OK - compressed)
     865 AndroidManifest.xml (OK - compressed)
    1544 resources.arsc (OK)
    3996 res/drawable-hdpi/background.png (OK)
    9676 res/drawable-hdpi/ic_launcher.png (OK)
   15704 res/drawable-mdpi/ic_launcher.png (OK)
   18880 res/drawable-xhdpi/ic_launcher.png (OK)
   28300 res/drawable-xxhdpi/ic_launcher.png (OK)
   46230 classes.dex (OK - compressed)
  283646 META-INF/MANIFEST.MF (OK - compressed)
  284138 META-INF/CERT.SF (OK - compressed)
  284662 META-INF/CERT.RSA (OK - compressed)
Verification succesful
[+] This command completed execution.
```

入口Activity：调用aapt

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 10 -i crackme.apk
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: bash bin/AmStart crackme.apk
adb shell am start -D -n com.mzheng.crackme1/com.mzheng.crackme1.MainActivity
[+] This command completed execution.
```
