<<<<<<< HEAD
# mem_dat
思路：
远程维护一个python的交互模式,通过http传输python操作，在远程主机上执行。达到将数据保持再内存中并运算的目的。

优点：
1、学习成本低，不用特别学习mem_data
2、代码量少
3、可以方便地操作数据

缺点：
通过python的exec执行远程代码，有较大风险
=======
# mem_data
requests.get('http://139.196.88.54:1320/?parameter='+base64.urlsafe_b64encode("self.data='oybb'  ".encode()).decode() ).text
>>>>>>> origin/master
