<!--
 * @Author: your name
 * @Date: 2019-12-29 16:41:14
 * @LastEditTime : 2020-01-05 16:43:22
 * @LastEditors  : Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \pycharm-items-github\test.md
 -->
# 如何远程服务器使用虚拟环境（虚拟环境的解释器）
## Python 基础教程--虚拟环境的创建和配置
### 以pycharm和linux 服务器为例
======================================================================  <br>
（For more information, please go to ***[Alan D. Chen](https://github.com/Alan-D-Chen/Python-ABC)*** , upgrading~~）<br>

_**Anaconda与conda区别 
conda可以理解为一个工具，也是一个可执行命令，其核心功能是包管理与环境管理。包管理与pip的使用类似，环境管理则允许用户方便地安装不同版本的python并可以快速切换。 conda的设计理念——conda将几乎所有的工具、第三方包都当做package对待，甚至包括python和conda自身 Anaconda则是一个打包的集合，里面预装好了conda、某个版本的python、众多packages、科学计算工具等等。**_

======================================================================
  
* 在wins系统下使用pycharm，结合CMD可以很方便的创建虚拟环境和利用pycharm管理和使用虚拟环境。[for
help](https://github.com/Alan-D-Chen/Python-ABC/blob/master/WINS如何安装python虚拟环境%EF%BC%88pytorch%EF%BC%89.md)
<br>

* 在linux环境下创建python虚拟环境，也很简单。[for help](https://github.com/Alan-D-Chen/Python-ABC/blob/master/如何创建Python%20虚拟环境%EF%BC%88Pytorch%EF%BC%89.md)

在pycharm的setting-->project interpreter -->"add"
中一定要指向服务器的虚拟环境的解释器~！！！！(具体方法可以参考[如何远程服务器](https://www.cnblogs.com/zhuminghui/p/10947930.html))