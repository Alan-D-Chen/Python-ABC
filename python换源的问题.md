# Python 的换源问题
----------------------------------------------
（For more information, please go to
***[Alan D. Chen](https://github.com/Alan-D-Chen/Python-ABC)*** ,
upgrading~~）<br>  
### 直接上干货！！~~
<br>
--------------------------------------------------------------------------

## [更改Python下载源的小工具](https://www.cnblogs.com/sunyanqinyin/p/9787995.html)
<br>

> Pip默认的源在国外，所以下载Python包的时候会比较慢，一般在几百KB左右，有时候只有十几kb。国内也有Pypi的镜像源，速度快的多，大概有2到3M的速度。最近看到一个自动切换国内源的小工具，很不错，分享一下。
> `pqi`
> 这个小工具叫做pqi，可以通过pip安装，官网链接https://github.com/yhangf/PyQuickInstall

安装<br>
`pip install pqi`

列举所有支持的PyPi源<br>
`pqi ls`

改变PyPi源<br>
`pqi use <name>`，比如运行pqi use tuna即把当前PyPi源改为清华的PyPi源。<br>

显示当前PyPi源 <br> `pqi show` <br>

------------------------------------------------------------------

## [python pip使用国内镜像](https://blog.csdn.net/cunyizhang/article/details/95336957)

<br> 
python pip使用国内镜像 <br> `pip install -i
https://pypi.tuna.tsinghua.edu.cn/simple tensorflow==1.12.2`

------------------------------------------------------------------

## [python工具包下载及速度慢问题解决](https://blog.csdn.net/qq_41937076/article/details/88321759)<br>

下载时经常会出现超时、速度慢、连接不上等问题，是因为pip安装是是默认连接的国外的服务器地址进行下载，因此会出现上述问题。解决时有两种方法。
<br>1)去国外资源站或其他地方找到要安装包的资源，下载后就cd到你下载包的文件夹中即可。
<br>2)切换默认的下载地址到国内资源站上。
打开该文件夹C:\Users\DELL\AppData\Roaming或是C:\Users\Administrator\AppData\Roaming，AppData文件夹如果找不到就是被隐藏了，在文件管理中显示被隐藏的文件夹即可。
在Roaming文件夹下新建文件夹pip,然后在此文件夹下新建txt文档，并在其中输入以下内容：

`[global]`
<br>
`timeout = 60000`
<br>
`index-url = https://pypi.tuna.tsinghua.edu.cn/simple`
<br>
`[install]`
<br>
`use-mirrors = true`
<br>
`mirrors = https://pypi.tuna.tsinghua.edu.cn`
<br>

保存并命名为“pip.ini”
<br>
然后再去cmd上下载时，速度问题便会得到解决，亲测有效！

**文档中的链接地址还可以更换其他的如下：**
<br>
阿里云http://mirrors.aliyun.com/pypi/simple/ <br>
中国科技大学https://pypi.mirrors.ustc.edu.cn/simple/ <br>
豆瓣(douban)http://pypi.douban.com/simple/ <br>
清华大学https://pypi.tuna.tsinghua.edu.cn/simple/ <br>
中国科学技术大学http://pypi.mirrors.ustc.edu.cn/simple/

--------------------------------------------------------------------

## [pytorch第一步（win+anaconda+好用的换源方法）安装](https://blog.csdn.net/kaidikake/article/details/102517002)

直接看到最后“换源”这一步。