
# Get52PojieTools

一个批量下载[52pojie](www.52pojie.cn)[爱盘](https://down.52pojie.cn/)中资源的小脚本。

```
爱盘地址：https://down.52pojie.cn/
爱盘限制多线程下载访问，请使用单线程进行下载访问，多并发会被禁止访问。
由于附件可能被安全软件误报，部分附件添加了压缩密码，默认解压密码：www.52pojie.cn
```

非常感谢吾爱破解整理提供的资源，包括各种教程、工具(破解版常用工具、各平台逆向分析工具)等。

## 使用

### 依赖

```
python 2.7
pip
pip install requests
pip install simplejson
```

### 运行

```
python main.py
```

如果不想下载所有的资源，可自行指定要下载目录

```
filter = [
    'Tools/Android_Tools/',
]
```

运行结果：

```
*********************************
* A downloader for 52pojie aipan 
* Site: https://down.52pojie.cn  
* Author: anhkgg
* Site: github.com/anhkgg, anhkgg.com
* CopyRight (c) 2019 
*********************************
 
 Start downloading ... 
 You want to download these dir: 
 -> Tools/
 ...
 Finish the job. 0.21s
```

## 赏杯咖啡

![img](./pay.png)