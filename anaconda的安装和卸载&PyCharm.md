# 如何创建Python (安装Anaconda)的运行环境
## Python 基础教程--解释器的创建和配置
### 以创建anaconda为例
======================================================================  <br>
（For more information, please go to ***[Alan D. Chen](https://github.com/Alan-D-Chen/Python-ABC)*** , upgrading~~）<br>

_**Anaconda与conda区别 
conda可以理解为一个工具，也是一个可执行命令，其核心功能是包管理与环境管理。包管理与pip的使用类似，环境管理则允许用户方便地安装不同版本的python并可以快速切换。 conda的设计理念——conda将几乎所有的工具、第三方包都当做package对待，甚至包括python和conda自身 Anaconda则是一个打包的集合，里面预装好了conda、某个版本的python、众多packages、科学计算工具等等。**_
##### (:-)[git 怎么在仓库里面上传一个文件夹到github?](https://www.zhihu.com/question/53015611/answer/594940741)
======================================================================  <br>
> ### python是解释性语言 <br>
[编译器和解释器之间有什么区别:](https://www.jianshu.com/p/5e0a34715693)(for more details)
 ### 根据他们的定义，编译器和解释器之间的区别貌似十分明显：
* 解释器：直接执行用编程语言编写的指令的程序
* 编译器：把源代码转换成（翻译）低级语言的程序

======================================================================  <br>
>> ## 特别提示：官网是最新版本的anaconda，对应的python是3.7的。<br>
我要找3.6的版本所有版本在这个网站都可以下载（清华大学开源软件镜像站）：<br>
https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/ 
<br>
Anaconda3-4.3.0.1-Windows-x86_64.exe 对应 python3.6.0<br>
Anaconda3-5.1.0-Windows-x86_64.exe 对应 python3.6.3<br>
Anaconda3-5.2.0-Windows-x86_64.exe 对应 python3.6.5<br>
Anaconda3-5.3.1-Windows-x86_64.exe  和 Anaconda3-5.3.0-Windows-x86_64.exe  对应 python3.7.0
Anaconda3-2020.02-Windows-x86_64.exe  对应python3.7.1<br>
>>> ### Anaconda 所有版本下载
因为在主机上配置Tensorflow环境，下载了最新的ananconda3-5.3.0，发现兼容性不是很好，<br>
于是又退回到Anaconda3-5.2.0。python 3.7.0（以及后继版本）兼容性不好，而且不稳定，<br>
不支持tensorflow框架，而且不支持numpy（在 `import numpy` 会报错~！！！），而pytorch框架需要numpy, <br>
python 3.7.0对机器学习的两大框架都不友好！！~~
[**Anaconda 所有版本下载**](https://blog.csdn.net/weixin_39653948/article/details/83214703)
 
[**anaconda历史版本下载**](https://www.cnblogs.com/xiaochouk/p/12081633.html)
anaconda历史版本安装：<br>
anaconda所有版本链接：https://repo.continuum.io/archive/
<br>
清华大学开源软件镜像站：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

![图片5](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/微信图片_20200403155043.png)

======================================================================  <br>
> ### 如何卸载anaconda？
优先选择这个教程：<br>
[**卸载Anaconda**](https://www.cnblogs.com/zhif97/p/12099903.html) (网速要好~！)<br>
[**如何使用Anaconda Prompt启动文件目录**](https://jingyan.baidu.com/article/ca41422f6e3d931eaf99ed71.html)<br>
[**Anaconda如何卸载？**](https://blog.csdn.net/u014723479/article/details/86738318)
<br>
* [如何彻底完全删除anaconda 进行重装](https://blog.csdn.net/qq_41549459/article/details/88323434)<br>
* [anaconda创建、删除、退出环境](https://blog.csdn.net/frank_ljiang/article/details/90317681)<br>
* [Anaconda之conda常用命令介绍(安装、更新、删除)](https://www.jb51.net/article/171350.htm)<br>
* [不能错过！超全Anaconda（Python整合包）导修（图文详解）](https://baijiahao.baidu.com/s?id=1650241306204278507&wfr=spider&for=pc)

======================================================================  <br>
> ### 如何安装 Anaconda？<br>
![图片](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200402163730.png)
<br>
[**Anaconda 的安装教程（图文）**](https://blog.csdn.net/weixin_43715458/article/details/100096496)
ps: 个人建议：记录好安装路径<br>

`１.下载anaconda ,可以是最新版本了; ` <br>
`２.输入命令：` `conda list` `,如果显示一系列安装包，证明安装完毕;` <br>

> ### 如何安装Pycharm？
<br>

>> Tips:

<br>

`where python`，查看python的解释器 interpreter .<br>

>> 在初始设置pycharm的时候，一定要注意设置文件夹和base interpreter的位置（路径），最起码要记录这些路径和文件的位置~！！<br>

![图片3](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200402220332.png)

* [pycharm的卸载和安装](https://www.pianshen.com/article/5474693243/)<br>
* [Python：查看解释器的位置](https://www.cnblogs.com/maoerbao/p/11519013.html)<br>

>>> 以前学Python时，有时出现这样的情况：明明记得装了scipy包，怎么打import scipy报错说我没这个包？<br>
>>> 有一些IDE会有自己默认的interpreter，在使用pycharm 终端修改interpreter有时，无法和我们想要的interpreter很好的对应，这个时候重装IDE（PyCharm）可以理清关系，节约不少时间。<br>
在git bash 、 CMD  或者 PyCharm 里面的 Terminal可以使用 `python -V` 或者 `where python`  与 PyCharm 页面化（Settings->）(如下图)进行比较！
![图片2](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200402220339.png)

问题出在，你的电脑上安装了不止一个Python...<br>
而每安装一个包，仅仅在这个Python安装路径里的Lib\site-packages\里，在别的里面并没有。<br>
这里介绍一个很轻巧的软件Everything，它方便你很快的查找本地计算机里的文件。我们输入python.exe，发现竟然出来了一堆python.<br>


* [PyCharm 使用教程看这篇就足够](https://www.jianshu.com/p/2a4d388b86e9)<br>
* [Pycharm简单使用教程](https://blog.csdn.net/qq_40130759/article/details/79421242)<br>
* [PyCharm彻底删除项目](https://zhuanlan.zhihu.com/p/93844554)<br>
* [Pycharm2020最新激活码汇总|pycharm永久激活](https://www.jianshu.com/p/16614b6ee4f8)<br>

>> pycharm 的美化

* [pycharm 的简单美化](https://hacpai.com/article/1566401537345)
* [PyCharm下载主题以及个性化设置(详细)](https://blog.csdn.net/qq_41782425/article/details/85081107)


