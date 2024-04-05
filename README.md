# fastapi_demo

## mysql
### install
$ dpkg --list |grep mysql
$ sudo apt-get remove mysql-common
$ sudo apt-get update && sudo apt-get install mysql-server
### 启动和关闭mysql
$ sudo service mysql start # 启动
$ sudo service mysql restart # 重启
$ sudo service mysql stop # 停止
安装:https://blog.csdn.net/qq_37120477/article/details/130653390  
修改密码:https://blog.csdn.net/m0_70885101/article/details/127414184
### root 密码修改
(1) 其他用户登录
$ sudo cat /etc/mysql/debian.cnf
--> user = debian-sys-maint
--> password = 7F6TVXx......
使用该用户名和密码登录mysql:
$ mysql -u debian-sys-maint -p
查看user表:
mysql> use mysql;
mysql> select user, plugin from user;
--> root: auth_socket
修改密码格式
mysql> update user set plugin = "mysql_native_password" where user="root";
刷新权限:
mysql> flush privileges;
增加root密码:
mysql> alter user 'root'@'localhost' identified by 'yourpassword'
再次刷新权限:
mysql> flush privileges;
退出重启mysql:
$ sudo service mysql restart;
$ mysql -uroot -p
基础操作:https://juejin.cn/post/6844904196383195144  

## fastapi

## fastapi + mysql demo
https://juejin.cn/post/7223373957087936549
