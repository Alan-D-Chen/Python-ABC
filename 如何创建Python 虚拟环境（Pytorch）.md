<!--
 * @Author: your name
 * @Date: 2019-12-29 16:41:14
 * @LastEditTime : 2020-01-05 16:43:22
 * @LastEditors  : Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \pycharm-items-github\test.md
 -->
# 如何创建Python 虚拟环境（Pytorch）
## Python 基础教程--环境的创建和配置
### 以创建Pytorch为例
======================================================================  
_**Anaconda与conda区别 
conda可以理解为一个工具，也是一个可执行命令，其核心功能是包管理与环境管理。包管理与pip的使用类似，环境管理则允许用户方便地安装不同版本的python并可以快速切换。 conda的设计理念——conda将几乎所有的工具、第三方包都当做package对待，甚至包括python和conda自身 Anaconda则是一个打包的集合，里面预装好了conda、某个版本的python、众多packages、科学计算工具等等。**_

======================================================================  
要想成功建立一个pytorch环境

## １　下载anaconda ,可以是最新版本了

## ２  输入命令：`conda list`,如果显示一系列安装包，证明安装完毕

## ３  安装环境，内部有可能是自带python，但是最后建立一个自己的镜像：

　　`conda create -n py36 python=3.6    -n:name`

>使用 `conda create -n your_env_name python=X.X`（2.7、3.6等）    
anaconda 命令创建python版本为X.X、名字为your_env_name的虚拟环境。your_env_name文件可以在Anaconda安装目录envs文件下找到。
>#### 指定python版本为2.7，注意至少需要指定python版本或者要安装的包   # 后一种情况下，自动安装最新python版本
>`conda create -n env_name python=2.7`
#### 同时安装必要的包
>`conda create -n env_name numpy matplotlib python=2.7`

## ４　`conda info -e`:查看现在已经有的环境
* conda相关命令的tips：
 >1）`conda list` 查看安装了哪些包。  
 >2）`conda env list` 或 `conda info -e` 查看当前存在哪些虚拟环境  
 >3）`conda update conda` 检查更新当前conda


## ５　切换环境：`source activate py36`   切换回来：`source deactivate`

>使用激活(或切换不同python版本)的虚拟环境.
 > 打开命令行输入`python --version`可以检查当前python的版本。  
 > 使用如下命令即可 激活你的虚拟环境(即将python的版本改变)。  
 > Linux:  `source activate your_env_name`(虚拟环境名称)  
 > Windows: `activate your_env_name` (虚拟环境名称)  
 > 这是再使用`python --version`可以检查当前python版本是否为想要的。 
 >7、删除虚拟环境。

 =================================================================================

* 移除环境
   使用命令`conda remove -n your_env_name(虚拟环境名称) --all`， 即可删除。

* 删除环境中的某个包。
   使用命令`conda remove --name $your_env_name $package_name` 即可。


* 设置国内镜像

如果需要安装很多packages，你会发现conda下载的速度经常很慢，因为Anaconda.org的服务器在国外。所幸的是，清华TUNA镜像源有Anaconda仓库的镜像，我们将其加入conda的配置即可：


|    |   |
|  ----  | ----  |
|1|# 添加Anaconda的TUNA镜像|
|2|conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/|
|3|# TUNA的help中镜像地址加有引号，需要去掉|
|4|  |
|5|# 设置搜索时显示通道地址|
|6|conda config --set show_channel_urls yes |
|||  

=================================================================================

## ６　安装pytorch,可以网上下载好pytorch,注意版本一定要对应上，这里的版本主要指的是你的python的版本

## ７　下载好pytorch之后，`pip install torch.....`
>## [Pytorch官网](https://pytorch.org/)  
>#### 这里可以根据自己的机器选择安装版本。一定要注意安装pytorch的版本。
![示意图](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pytorch.png)

`conda install pytorch torchvision cudatoolkit=10.1 -c pytorch`


>对虚拟环境中安装额外的包。
   > 使用命令conda install -n your_env_name [package]即可安装package到your_env_name中  
   > 安装特定版本的`conda install pytorch=0.1.10 -c soumith `  
   
在安装完Pytorch 之后，还要安装torchvision：
`conda install torchvision`


## ８　查看是否安装好pytorch:import torch

## ９　接下来，可能会报错，是因为没有numpy.注：这里numpy安装需要pip,应该是版本问题，具体我还没了解，反正我用conda 安装会不兼容，这个好解决

## １０接下来再查看torch是否安装好

## １１接下来安装torchvision:`conda install torchvision`!



## 参考文献
1.[Anaconda+用conda创建python虚拟环境](https://www.cnblogs.com/swje/p/7642929.html)  
2.http://blog.csdn.net/lyy14011305/article/details/59500819  
3.https://zhuanlan.zhihu.com/p/22678445  
4.[Anaconda 4.2 ---conda使用（Windows）](https://blog.csdn.net/u010004460/article/details/54287556)  
5.[Anaconda使用总结](https://www.jianshu.com/p/2f3be7781451)  
6.https://blog.csdn.net/qinguanggai9953/article/details/88235043
7.https://blog.csdn.net/hao5335156/article/details/80798143
8.https://blog.csdn.net/qq_32408773/article/details/84112166
9.https://blog.csdn.net/li57681522/article/details/82491617
