# python2/3 版本的切换
## Python 基础教程--多个python版本的切换
### 以创建anaconda为例 linux 环境
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

=======================================================================
<br>

首先一个Linux
系统中有anaconda、conda、甚至是miniconda，这里建议大家还是安装anaconda3（python3）。
anaconda3 （linux）+ 本地 pycharm（wins）的形式还是比较合适。
在安装anaconda之前，最好能够了解server里面有没有其他的python安装环境，以免相互打扰。
遇到多个版本的python，切换环境： 

<br> 

##  [linux 服务器的python2、python3版本切换](https://blog.csdn.net/fu6543210/article/details/87876981)

在（base）环境下
 ![pic2](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/20190611142829189.png) 
``` 
这是由于环境变量未导入，或者环境变量导入了未更新。
输入命令打开配置文件
vim ~/.bashrc
```
```
在最后添加语句
export PATH=/home/XXX/anaconda3/bin:$PATH
```
这个export
语句，给linux系统添加了新的环境变量。请确保bashrc文件中关于python的文件的统一，
这个方法还可以解决多个安装环境，多个python版本，甚至是在terminal里创建虚拟环境，使用python
A，但是一些包却安装在python B的情况。 
```
XXX为你的用户名
```
最后输入如下命令，更新配置文件即可 
``` 
source ~/.bashrc 
```
## [linux下切换python2和python3(临时性和永久性)](https://www.cnblogs.com/zl1991/p/9041554.html)

首先先来看一下我们的默认Python版本 
```
$ python --version
Python 2.7.6
```
然后我们修改一下别名 
```
 $ alias python='/usr/bin/python3' $ python
--version Python 3.4.3
```
 版本已经改变 /usr/bin/python3 这个路径是怎么找到的呢？
 一般来说，软件的二进制文件都可以在 /usr/bin 或 /usr/local/bin
 (这个优先级高一点)找到。当然如果你是Debian系的Linux，可以这么找(前提是你已经安装了Python3)：
 ```
  $ dpkg -L python3
  ```
 上面的别名修改只是暂时性的，重开一个窗口后配置就不见了。如果要使每个窗口都使用这个别名，可以编辑
 ~/.bashrc (如果你是别的shell的话，就不是这个文件，如zsh是 ~/.zshrc
 )，把alias配置写入文件。 修改别名优点是足够简单，但是切换不灵活。
 
> > > 可以通过上面的链接 寻找永久性切换的方法。

## [linux安装或卸载miniconda](https://www.jianshu.com/p/fab0068a32b4)

Conda 是一个开源的软件包管理系统和环境管理系统，用于安装多个版本的软件包及其依赖关系，并在它们之间轻松切换。

## [linux - 卸载python](https://www.cnblogs.com/tnsay/p/11676895.html)

```
2019年10月15日12:05:42


[root@spider1 bin]# rpm -qa|grep python|xargs rpm -ev --allmatches --nodeps ##强制删除已安装程序及其关联
[root@spider1 bin]# whereis python |xargs rm -frv ##删除所有残余文件 ##xargs，允许你对输出执行其他某些命令
[root@spider1 bin]# whereis python ##验证删除，返回无结果
```

## [Linux下python的卸载与安装](https://blog.csdn.net/yimisiyang/article/details/104037739)

```
卸载：
1、卸载python3.5
sudo apt-get remove python3.5
1
2、卸载python3.5及其依赖
sudo apt-get remove --auto-remove python3.5
1
3、清除python3.5
sudo apt-get purge python3.5
1
or
sudo apt-get purge --auto-remove python3.5
1
安装：
下载python
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
wget -P /usr/lib https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz(下载文件到指定目录)
12
解压、编译安装
tar -zxvf Python-2.7.9.tgz
cd Python-2.7.9
./configure --prefix=/usr/local/python-2.7.9
make
make install
12345
系统自带了python版本，我们需要为新安装的版本添加一个软链
ln -s /usr/local/python-2.7.9/bin/python /usr/bin/python2.7.9

```

## [anaconda的安装和卸载&PyCharm](https://github.com/Alan-D-Chen/Python-ABC/blob/master/anaconda的安装和卸载%26PyCharm.md)