# ImageHosting
听说你想要一个图床，几行py代码，轻松使用github做免费图床，除了外网问题，其他。。。emm

* 首先，我使用是windows，电脑里要安装git，然后添加到环境变量
* 然后python环境配置，2和3都可以
* 新建一个仓库，将这里的update.py代码添加进仓库
* 然后将你新建的仓库克隆到本地，在需要添加图片的时候直接将图片放在本地仓库里，然后运行一下py代码就可以了（如果你的python文件打开方式默认是python.exe，那么双击一下就可以了，是不是很方便~(@^_^@)~ ）

很简单的py代码，看一下就懂了，就是使用os.system运行cmd指令而已，做了一点小优化，图片上传后会将图片的url地址输出到控制台上，如果只上传一张图片的话会将图片的url地址复制到剪切板上。

![](https://raw.githubusercontent.com/LittleFish33/ImageHosting/master/readme.png)

顺带一提，这里对delete的情况并没有做处理，delete的话也是会输出一个路径的，逃