# python2/3 �汾���л�
## Python �����̳�--���python�汾���л�
### �Դ���anacondaΪ�� linux ����
======================================================================  <br>
��For more information, please go to ***[Alan D. Chen](https://github.com/Alan-D-Chen/Python-ABC)*** , upgrading~~��<br>

_**Anaconda��conda���� 
conda�������Ϊһ�����ߣ�Ҳ��һ����ִ���������Ĺ����ǰ������뻷��������������pip��ʹ�����ƣ����������������û�����ذ�װ��ͬ�汾��python�����Կ����л��� conda����������conda���������еĹ��ߡ���������������package�Դ�����������python��conda���� Anaconda����һ������ļ��ϣ�����Ԥװ����conda��ĳ���汾��python���ڶ�packages����ѧ���㹤�ߵȵȡ�**_
##### (:-)[git ��ô�ڲֿ������ϴ�һ���ļ��е�github?](https://www.zhihu.com/question/53015611/answer/594940741)
======================================================================  <br>
> ### python�ǽ��������� <br>
[�������ͽ�����֮����ʲô����:](https://www.jianshu.com/p/5e0a34715693)(for more details)
 ### �������ǵĶ��壬�������ͽ�����֮�������ò��ʮ�����ԣ�
* ��������ֱ��ִ���ñ�����Ա�д��ָ��ĳ���
* ����������Դ����ת���ɣ����룩�ͼ����Եĳ���

=======================================================================
<br>

����һ��Linux
ϵͳ����anaconda��conda��������miniconda�����ｨ���һ��ǰ�װanaconda3��python3����
anaconda3 ��linux��+ ���� pycharm��wins������ʽ���ǱȽϺ��ʡ�
�ڰ�װanaconda֮ǰ������ܹ��˽�server������û��������python��װ�����������໥���š�
��������汾��python���л������� 

<br> 

##  [linux ��������python2��python3�汾�л�](https://blog.csdn.net/fu6543210/article/details/87876981)

�ڣ�base��������
 ![pic2](https://github.com/Alan-D-Chen/Python-ABC/blob/master/pics/20190611142829189.png) 
``` 
�������ڻ�������δ���룬���߻�������������δ���¡�
��������������ļ�
vim ~/.bashrc
```
```
�����������
export PATH=/home/XXX/anaconda3/bin:$PATH
```
���export
��䣬��linuxϵͳ������µĻ�����������ȷ��bashrc�ļ��й���python���ļ���ͳһ��
������������Խ�������װ���������python�汾����������terminal�ﴴ�����⻷����ʹ��python
A������һЩ��ȴ��װ��python B������� 
```
XXXΪ����û���
```
�����������������������ļ����� 
``` 
source ~/.bashrc 
```
## [linux���л�python2��python3(��ʱ�Ժ�������)](https://www.cnblogs.com/zl1991/p/9041554.html)

����������һ�����ǵ�Ĭ��Python�汾 
```
$ python --version
Python 2.7.6
```
Ȼ�������޸�һ�±��� 
```
 $ alias python='/usr/bin/python3' $ python
--version Python 3.4.3
```
 �汾�Ѿ��ı� /usr/bin/python3 ���·������ô�ҵ����أ�
 һ����˵������Ķ������ļ��������� /usr/bin �� /usr/local/bin
 (������ȼ���һ��)�ҵ�����Ȼ�������Debianϵ��Linux��������ô��(ǰ�������Ѿ���װ��Python3)��
 ```
  $ dpkg -L python3
  ```
 ����ı����޸�ֻ����ʱ�Եģ��ؿ�һ�����ں����þͲ����ˡ����Ҫʹÿ�����ڶ�ʹ��������������Ա༭
 ~/.bashrc (������Ǳ��shell�Ļ����Ͳ�������ļ�����zsh�� ~/.zshrc
 )����alias����д���ļ��� �޸ı����ŵ����㹻�򵥣������л�����
 
> > > ����ͨ����������� Ѱ���������л��ķ�����

## [linux��װ��ж��miniconda](https://www.jianshu.com/p/fab0068a32b4)

Conda ��һ����Դ�����������ϵͳ�ͻ�������ϵͳ�����ڰ�װ����汾�����������������ϵ����������֮�������л���

## [linux - ж��python](https://www.cnblogs.com/tnsay/p/11676895.html)

```
2019��10��15��12:05:42


[root@spider1 bin]# rpm -qa|grep python|xargs rpm -ev --allmatches --nodeps ##ǿ��ɾ���Ѱ�װ���������
[root@spider1 bin]# whereis python |xargs rm -frv ##ɾ�����в����ļ� ##xargs������������ִ������ĳЩ����
[root@spider1 bin]# whereis python ##��֤ɾ���������޽��
```

## [Linux��python��ж���밲װ](https://blog.csdn.net/yimisiyang/article/details/104037739)

```
ж�أ�
1��ж��python3.5
sudo apt-get remove python3.5
1
2��ж��python3.5��������
sudo apt-get remove --auto-remove python3.5
1
3�����python3.5
sudo apt-get purge python3.5
1
or
sudo apt-get purge --auto-remove python3.5
1
��װ��
����python
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
wget -P /usr/lib https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz(�����ļ���ָ��Ŀ¼)
12
��ѹ�����밲װ
tar -zxvf Python-2.7.9.tgz
cd Python-2.7.9
./configure --prefix=/usr/local/python-2.7.9
make
make install
12345
ϵͳ�Դ���python�汾��������ҪΪ�°�װ�İ汾���һ������
ln -s /usr/local/python-2.7.9/bin/python /usr/bin/python2.7.9

```

## [anaconda�İ�װ��ж��&PyCharm](https://github.com/Alan-D-Chen/Python-ABC/blob/master/anaconda�İ�װ��ж��%26PyCharm.md)