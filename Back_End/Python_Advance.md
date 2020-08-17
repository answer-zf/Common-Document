# Python 后端

## Django 框架

### 简介：

-   组件：

    1.  路由
    2.  URL解析
    3.  原生 HTML 模板系统
    4.  数据库连接 和 ORM 数据库管理
    5.  用户管理认证系统
    6.  ORM模型系统
    7.  电子邮件发送系统
    8.  CSRF跨站点请求伪造的保护
    9.  表单验证
    10. 数据库后台管理系统
    11. 自带强大的后台管理功能

-   DJango的用途

    1.  网站后端开发
    2.  微信公众号后台开发
    3.  微信小程序后台开发
    4.  基于HTTP/HTTPS 协议的后台服务器开发
        -   在线语音图像识别服务器
        -   在线第三方身份验证服务器等

### 安装：

1.  在线安装：`$ sudo pip3 install django==1.11.8`

2.  离线安装：

    -   下载安装包： `$ Django-1.11.8.tar.gz`
    -   `$ tar -xvf Django-1.11.8.tar.gz`
    -   `$ cd Django-1.11.8`
    -   `$ sudo python3 setup.py install`

3.  使用 wheel 安装

    -   下载:`pip3 download -d 路径`
    -   安装：`pip3 install Django-1.11.8.whl`

4.  卸载：`pip3 uninstall Django`

### Django 框架开发

1.  创建练习项目:`$ django-admin startproject 项目名`
