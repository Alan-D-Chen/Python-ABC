# WINS如何创建Python 虚拟环境（Pytorch）
## Python 基础教程--环境的创建和配置
### 以创建Pytorch为例

----------------------------------------------
Thanks a lot for tongji501 [@Mr.Jiang](https://baike.baidu.com/item/吴彦祖/182990?fr=aladdin)<br>
（For more information, please go to ***[Alan D. Chen](https://github.com/Alan-D-Chen/Python-ABC)*** , upgrading~~）<br>  
conda可以理解为一个工具，也是一个可执行命令，其核心功能是包管理与环境管理。包管理与pip的使用类似，环境管理则允许用户方便地安装不同版本的python并可以快速切换。 conda的设计理念——conda将几乎所有的工具、第三方包都当做package对待，甚至包括python和conda自身 Anaconda则是一个打包的集合，里面预装好了conda、某个版本的python、众多packages、科学计算工具等等。
建议使用 pip、pip3或者conda,在使用包管理之前，建议查看pip、conda的版本和安装路径(使用`pip -V`，`conda -V`，这里可以用来鉴别虚拟环境的interpreter是否和原始的环境的共用一个interpreter。)
<br>
>>>强烈建议先使用命令行创建虚拟环境然后使用IDE加载虚拟环境，这样比较保险！！~~~
<br>

![图片1](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200330200813.png)

<br>

虽然网上有不少的教程，但是不少的细节没有介绍到。
首先是命令行：
## [windows安装Python虚拟环境](https://www.cnblogs.com/sisa/p/10824191.html)
这里只要做到第六步`退出virtualenv  deactivate.bat`，就可以了，当然也可以继续下面的步骤。
>>> 如果出现了
<br>

`ERROR: Exception:
Traceback (most recent call last):
  File "C:\Users\Anaconda3\lib\site-packages\pip\_internal\cli\base_command.py", line 186, in _main
    status = self.run(options, args)
  File "C:\Users\Anaconda3\lib\site-packages\pip\_internal\commands\install.py", line 258, in run
    isolated_mode=options.isolated_mode,
  File "C:\Users\Anaconda3\lib\site-packages\pip\_internal\commands\install.py", line 604, in decide_user_install
    if site_packages_writable(root=root_path, isolated=isolated_mode):
  File "C:\Users\Anaconda3\lib\site-packages\pip\_internal\commands\install.py", line 549, in site_packages_writable
    test_writable_dir(d) for d in set(get_lib_location_guesses(**kwargs))
  File "C:\Users\Anaconda3\lib\site-packages\pip\_internal\commands\install.py", line 549, in <genexpr>
    test_writable_dir(d) for d in set(get_lib_location_guesses(**kwargs))
  File "C:\Users\Anaconda3\lib\site-packages\pip\_internal\utils\filesystem.py", line 140, in test_writable_dir
    return _test_writable_dir_win(path)
  File "C:\Users\Anaconda3\lib\site-packages\pip\_internal\utils\filesystem.py", line 153, in _test_writable_dir_win
    fd = os.open(file, os.O_RDWR | os.O_CREAT | os.O_EXCL)
PermissionError: [Errno 13] Permission denied: 'C:\\Users\\Anaconda3\\Lib\\site-packages\\accesstest_deleteme_fishfingers_custard_n0oqqf'
`

<br>
>>> 可以尝试以管理员身份启动CMD，然后再次尝试。
<br>
>>> 这里有这个问题的详细分析，具体情况，具体分析：

>>> [Python报错：PermissionError: Errno 13 Permission denied解决方案详解](https://blog.csdn.net/shuiyixin/article/details/90370387)
<br>
<br>
此处，如果出现了问题，可以参考一下教程：
* [Windows下搭建Python虚拟环境](https://www.jianshu.com/p/ad2d8ee4a679)
* [windows下python虚拟环境virtualenv安装和使用](https://www.cnblogs.com/sunyllove/p/9748995.html)
* [笔记1](https://www.jianshu.com/p/3b9b218b66a3)
* [Python学习笔记：虚拟环境和包](https://blog.csdn.net/lvsehaiyang1993/article/details/82749360)
* [win10+python3 Pytorch安装](https://blog.csdn.net/ZHUJIYAO/article/details/89554096)

---------------------------------------------------------------------------

<br>

![图片2](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/Inked%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200330182919_LI.jpg)

<br>

>>> tips:<br>在使用pycharm创建虚拟环境之后，<br> 
1.使用 B 来创建python虚拟环境，发现到最后无法激活环境，<br> 
2.而且AC处无法使用 cd ls 等命令，变得有些难用~<br> 
B无法激活环境很有可能跟pycharm无法区分pip有关系~<br>C是cmd，ls 是bash命令，C可以用cd，只是不能这样进根目录，直接`d:`，其他的都可以cd，除了换盘的时候，你现在再cd 进d盘的其他目录是可以的，除了切换cde盘的时候直接`c: d: e:`,不用cd。
<br>
---------------------------------------------------------------------------------
<br>
当你使用命令行，激活完成虚拟环境之后会出现前缀（虚拟环境名称）的符头。
<br>

![图片3](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200330200821.png)

如果你喜欢命令行操作的话，工作已经基本完成了。<br>


## python IDE (以pycharm为例)

可以参考一下教程：（加载已有的虚拟环境和创建全新的虚拟环境）
* [手把手教你如何在Pycharm中加载和使用虚拟环境](https://www.cnblogs.com/dcpeng/p/12257331.html)<br>
  注意：`6、根据目录，依次找到自己创建的虚拟环境路径，我的路径是I:->Virtual_environment_list->Scripts->python.exe，如下图所示。`
  这一步的路径一定要替换为你自己的(上面的自己建立的)interpreter~！
* [pycharm配置本地python虚拟环境](https://blog.csdn.net/guying4875/article/details/80905472)
  这里一定要注意1234的选择，尤其是 1 2 的路径，不然很有可能会占用你原始环境的ntetpreter
  
  <br>
  
 ## 正常创建的虚拟环境，应该是下面的画面：（pycharm）
 
 <br>
 
 ![图片4](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200330200835.png)
 
 <br> 
module 应该比较干净。此时，需要做一下检查：

 `pip -V` , `conda -V` , `pip list` , `conda list` ,
 <br>
 
 以上语句，可以帮助你查明新建的虚拟环境与原始环境是否公用一个interpreter，或者公用一副 pip/conda 管理包。一旦发现公用一个interpreter，或者公用一副 pip/conda 管理包，之后安装pytorch，就会出现error。
 
 <br>
 pytorch 的 依赖包：
 <br>
 
 ### [PyTorch入门教程](https://www.jianshu.com/p/d66319506dd7)
 
 <br>
 pytorch需要numpy~，请确保numpy的正常~~
 <br>
 
 ### [pytorch在windows10上安装使用](https://blog.csdn.net/cuixing001/article/details/81952116)
 
 <br>
 测试pytorch 是否安装完好：
 <br>
 
 `import torch`
 <br>
 `A = torch.randn(3,3)`
 <br>
 `print(A)`
 <br>
 如是出现：<br>
 `from torch._C import * ImportError: DLL load failed: 找不到指定的模块。`
 <br>
 可以切换为原始的环境，再次测试：
 <br>
 
 `import torch`
 <br>
 `A = torch.randn(3,3)`
 <br>
 `print(A)`
 <br>
  因为你很有可能将pytorch安装到原始环境去了。
  
然后再去阅读下面的教程：
 
* https://blog.csdn.net/sunny_580/article/details/89476176?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
* https://cloud.tencent.com/developer/article/1451477
* https://www.cnblogs.com/pythoner6833/p/10682390.html
* https://blog.csdn.net/ha010/article/details/87872852
* https://blog.csdn.net/sunny_580/article/details/89476176?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
* https://blog.csdn.net/qq_38627475/article/details/89735995
