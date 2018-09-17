# -socket-UDP-
基于socket UDP 局域网聊天小软件

服务端文件目录

chat_service

           |——bin
           |    |——service.py
           |    
           |——conf
           |     |——settings.py
           |      
           |——db
           |   |——user
           |   | 
           |   |——db_handle.py
           |    
           |——interface
           |          |——service_interface.py
           |           
           |——lib
           |    |——common.py
           |     
           |——log
           |
           |——models
           |       |——user.py
           |        
           |——start.py

客户端文件目录

chat_client

           |——bin
           |    |——client.py
           |    
           |——conf
           |     |——settings.py
           |      
           |——db
           |   |——db_handle.py
           |    
           |——interface
           |          |——client_interface.py
           |           
           |——lib
           |    |——common.py
           |
           |——models
           |       |——user.py
           |        
           |——start.py


在学习完套接字和线程并发后才想写的这个小程序，基本实现了，注册、登录、添加好友，好友间通信。对自己来说是一个综合性的小作业吧。

但是还有很多明显的不足，由于使用的是udp协议，所以不能保证能及时收到消息，也没有写补发，预留了日志但是并没有写。

线程间通信应该用队列，由于程序太小了，所以不用加线程池

我自己设定的报头
"o"代表操作类型
1 注册
2 登录
3 转发
4 注销
5 添加好友
0 错误请求

"d"代表数据
a 账号
p 密码
m 消息
t 目标

客户端与服务端通信的数据是字典类型，用json模块转成字符串后，又使用encode()转成utf-8编码
接收到后，反过来解析成字典
