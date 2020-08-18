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

1.  创建项目:`$ django-admin startproject project_name`

2.  运行:

    -   `cd project_name/`
    -   `python3 manage.py runserver`
        -   `python3 manage.py runserver 5000`
            -   指定设备有5000端口
        -   `python3 manage.py runserver 192.168.40.129:8000`
            -   指定IP+端口
            -   指定IP需要修改settings.py
            -   ALLOWED_HOSTS = \[] #空列表只允许127.0.0.1访问
            -   ALLOWED_HOSTS = ['*'] 允许任意访问 仅限调试使用

3.  目录解析

    -   manage.py
        -   此文件是项目管理的主程序在开发阶段用于管理整个项目的开发运行的调式
        -   manage.py 包含项目管理的子命令
        -   `python3 manage.py runserver` 启动服务
        -   `python3 manage.py startapp` 创建应用
        -   `python3 manage.py migrate` 数据库迁移
    -   project_name(项目包文件夹[默认与项目名称一致])

        -   `__init__.py`

            -   项目初始化文件,服务启动时自动运行

        -   `wsgi.py`

            -   WEB服务网关接口的配置文件,仅部署项目时使用

        -   `urls.py`

            -   项目的基础路由配置文件,所有的动态路径必须先走该文件进行匹配

        -   `settings.py`

            -   Django的配置文件,此配置文件中的一些全局变量将为 Django框架的运行传递一些参数
            -   settings. py配置文件,启动服务时自动调用
            -   此配置文件中也可以定义一些自定义的变量用于作用全局作用域的数据传递

4.  文件详解

    -   settings.py 文件介绍

        1.  BASE_DIR
            -   用于绑定=当前项目的绝对路径(动态计算出来的),所有文件都可以依懒此路径
        2.  DEBUG用于配置 Django项目的启用模式
            1.  True表示开发环境中使用调试模式 (用于开发中)
            2.  False表示当前项目运行在生产环境中(不启用调试)
        3.  ALLOWED_HOSTS
            -   设置允许访问到本项目的网络地址列表
            -   取值：
                -   `ALLOWED_HOSTS = []` 如果为空列表，只允许127.0.0.1访问本项目
                -   `ALLOWED_HOSTS = ['*']`表示任何网络地址都能访问到当前项目 仅限调试使用
        4.  INSTALLED_APPS
            -   指定当前项目中安装的应用列表
        5.  MIDDLEWARE
            -   用于注册中间件
        6.  ROOT_URLCONF
            -   用于配置根级 url 配置
        7.  TEMPLATES
            -   用于指定模板的配置信息
        8.  DATABASES
            -   用于指定数据库的配置信息
        9.  LANGUAGE_CODE
            -   用于指定语言配置
            -   取值：
                -   中文：`LANGUAGE_CODE = "zh-Hans"`
        10. TIME_ZONE
            -   用于指定当前服务器端时区
            -   取值：
                -   中国时区：`TIME_ZONE = "Asia/Shanghai"`


        -   缺省配置
            -   模块
                -   `import django.conf.global_settings`
                -   Linux 下文件位置
                    -   `/usr/lib/python3/dist-packages/django/conf/global_settings.py`

#### 路由

> url 即统一资源定位符 Uniform Resource Locator

-   作用
    -   对互联网上得到的资源的位置和访问方法的一种简洁的表示,是互联网上标准资源的地址。互联网上的每个文件都 有一个唯一的URL,它包含的信息指出文件的位置以及浏览器应该怎么处理它。

> 路由：不看域名部分

##### 在Django 中的 URL 路由配置

1.  settings.py 中 的 ROOT_URLCONF

    -   通过 ROOT_URLCONF 指定顶级url配置
        -   默认存在于主文件夹内，主路由配置文件

2.  urlpatterns 是一个 url() 实例的列表

    -   作用：该文件会包含 urlpatterns的列表用于表示路由-视图映射,通过url()表示具体映射

3.  url() 函数

    -   用户描述路由与视图函数的对应关系
    -   模块
        -   `from django.conf.urls import url`
    -   语法：
        -   `url(regexp,views,kwargs=None,name=None)`
            1.  regexp:字符串类型,匹配的请求路径,允许是 正则表达式
                -   自上而下的匹配，遇到满足条件直接执行视图函数，后续匹配不再执行。
            2.  views:指定路径所对应的视图处理函数的名称
            3.  kwargs:向视图中传递的参数
            4.  name:为地址起别名,反向解析时使用
        -   注：
            -   每个正则表达式前面的 r 表示 \\ 不转义的原始字符串
            -   当 urlpatterns 内有多个url对象时,按自上而下的顺序进行配置,一但有路由与url配置成功,则后面的所有url被忽略

4.  视图 view

    -   用于接收请求,处理请求并做出响应
    -   视图处理的函数的语法格式

        ```py
            def xxx(request[,其他参数...]):
                return 响应对象
        ```

    -   url 和带有参数的视图函数

        -   在视图函数内,可以用正规表达式分组()提取参数后传送给视图函数
        -   一个分组表示一个参数,多个参数需要使用多个分组,并且使用个/隔开

    -   url 正则表达式命名分组(?Pxx)和带有参数的视图函数
        -   在url 的正则表达式中可以使用命名分组(捕获分组)
        -   正则表达式的名称必须在view中以关键字传参方式传入,因此视图函数能接收此参数
        -   每个捕获的参数都作为一个普通的 python字符串传递给视图
        -   urlpatterns中的每个正则表达式在第一次访问它们时被编译, 这使得系统相当快

    ```py
    ################### urls.py ###################
    from . import views

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', views.homepage),
        url(r'^year/(\d{4})$', views.pageyear),
        url(r'^birthday/(\d{4})/(\d{1,2})/(\d{1,2})$', views.birthday),
        url(r'^person/(?P<name>\w+)/(?P<age>\d+)', views.person),
    ]

    ################### views.py ###################
    from django.http import HttpResponse

    def homepage(request):
        return HttpResponse("this .is .homepage...")

    def pageyear(request, y):
        return HttpResponse("this.is.yearpage.%s" % y)

    def birthday(request, y, m, d):
        return HttpResponse('birthday is %s-%s-%s' % (y, m, d))

    def person(request, name, age):
        return HttpResponse("this is %s, %s" % (name, age))
    ```
