



# WINS��δ���Python ���⻷����Pytorch��
## Python �����̳�--�����Ĵ���������
### �Դ���PytorchΪ��

----------------------------------------------
Thanks a lot for tongji501 [@Mr.Jiang](https://baike.baidu.com/item/������/182990?fr=aladdin)<br>
��For more information, please go to ***[Alan D. Chen](https://github.com/Alan-D-Chen/Python-ABC)*** , upgrading~~��<br>  
conda�������Ϊһ�����ߣ�Ҳ��һ����ִ���������Ĺ����ǰ������뻷��������������pip��ʹ�����ƣ����������������û�����ذ�װ��ͬ�汾��python�����Կ����л��� conda����������conda���������еĹ��ߡ���������������package�Դ�����������python��conda���� Anaconda����һ������ļ��ϣ�����Ԥװ����conda��ĳ���汾��python���ڶ�packages����ѧ���㹤�ߵȵȡ�
����ʹ�� pip��pip3����conda,��ʹ�ð�����֮ǰ������鿴pip��conda�İ汾�Ͱ�װ·��(ʹ��`pip -V`��`conda -V`��������������������⻷����interpreter�Ƿ��ԭʼ�Ļ����Ĺ���һ��interpreter��)
<br>
ͼƬ1
<br>
��Ȼ�����в��ٵĽ̳̣����ǲ��ٵ�ϸ��û�н��ܵ���
�����������У�
## [windows��װPython���⻷��](https://www.cnblogs.com/sisa/p/10824191.html)
����ֻҪ����������`�˳�virtualenv  deactivate.bat`���Ϳ����ˣ���ȻҲ���Լ�������Ĳ��衣

�˴���������������⣬���Բο�һ�½̳̣�
* [Windows�´Python���⻷��](https://www.jianshu.com/p/ad2d8ee4a679)
* [windows��python���⻷��virtualenv��װ��ʹ��](https://www.cnblogs.com/sunyllove/p/9748995.html)
* [�ʼ�1](https://www.jianshu.com/p/3b9b218b66a3)
* [Pythonѧϰ�ʼǣ����⻷���Ͱ�](https://blog.csdn.net/lvsehaiyang1993/article/details/82749360)
* [win10+python3 Pytorch��װ](https://blog.csdn.net/ZHUJIYAO/article/details/89554096)

---------------------------------------------------------------------------
## tips:
<br>
ͼƬ2
<br>

��ʹ��pycharm�������⻷��֮��<br>
1.ʹ�� B ������python���⻷�������ֵ�����޷��������<br>
2.����AC���޷�ʹ�� cd ls ����������Щ����~<br>
B�޷���������п��ܸ�pycharm�޷�����pip�й�ϵ~<br>
C��cmd��ls ��bash���C������cd��ֻ�ǲ�����������Ŀ¼��ֱ��d:�������Ķ�����cd��
���˻��̵�ʱ����������cd ��d�̵�����Ŀ¼�ǿ��Եģ������л�cde�̵�ʱ��ֱ��c: d: e:
����cd
<br>
---------------------------------------------------------------
����ʹ�������У�����������⻷��֮������ǰ׺�����⻷�����ƣ��ķ�ͷ��
�����ϲ�������в����Ļ��������Ѿ���������ˡ�<br>


## python IDE (��pycharmΪ��)

���Բο�һ�½̳̣����������е����⻷���ʹ���ȫ�µ����⻷����
* [�ְ��ֽ��������Pycharm�м��غ�ʹ�����⻷��](https://www.cnblogs.com/dcpeng/p/12257331.html)<br>
  ע�⣺``  6������Ŀ¼�������ҵ��Լ����������⻷��·�����ҵ�·����I:->Virtual_environment_list->Scripts->python.exe������ͼ��ʾ��`
  ��һ����·��һ��Ҫ�滻Ϊ���Լ���(������Լ�������)interpreter~��
* [pycharm���ñ���python���⻷��](https://blog.csdn.net/guying4875/article/details/80905472)
  ����һ��Ҫע��1234��ѡ�������� 1 2 ��·������Ȼ���п��ܻ�ռ����ԭʼ������ntetpreter
  
  <br>
  
 ## �������������⻷����Ӧ��������Ļ��棺��pycharm��
 <br>
 ͼƬ3
  <br> 
module Ӧ�ñȽϸɾ���
��ʱ����Ҫ��һ�£���飺
`pip -V`,`conda -V` ,`pip list`,`conda list` ,������䣬���԰���������½������⻷����ԭʼ�����Ƿ���һ��interpreter�����߹���һ�� pip/conda �������
<br>
һ�����ֹ���һ��interpreter�����߹���һ�� pip/conda �������֮��װpytorch���ͻ����error��
 
 <br>
 pytorch �� ��������<br>
 [PyTorch���Ž̳�](https://www.jianshu.com/p/d66319506dd7)<br>
 pytorch��Ҫnumpy~����ȷ��numpy������~~
### [pytorch��windows10�ϰ�װʹ��](https://blog.csdn.net/cuixing001/article/details/81952116)
 <br>
 ����pytorch �Ƿ�װ��ã�
 `import torch
  A = torch.randn(3,3)
  print(A)
  `
 ���ǳ���`from torch._C import * ImportError: DLL load failed: �Ҳ���ָ����ģ�顣`
 <br>
 �����л�Ϊԭʼ�Ļ������ٴβ��ԣ�<br>
 `import torch
  A = torch.randn(3,3)
  print(A)
  `
  ��Ϊ����п��ܽ�pytorch��װ��ԭʼ����ȥ�ˡ�
  
Ȼ����ȥ�Ķ�����Ľ̳̣�
 
* https://blog.csdn.net/sunny_580/article/details/89476176?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
* https://cloud.tencent.com/developer/article/1451477
* https://www.cnblogs.com/pythoner6833/p/10682390.html
* https://blog.csdn.net/ha010/article/details/87872852
* https://blog.csdn.net/sunny_580/article/details/89476176?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
* https://blog.csdn.net/qq_38627475/article/details/89735995