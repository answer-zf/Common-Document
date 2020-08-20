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

#### 请求和响应

##### HTTP请求

-   根据HTTP标准,HTTP请求可以使用多种请求方法。
-   HTTP1.0 定义了三种请求方法: GET , POST 和 HEAD 方法(最常用)
-   HTTP1.1新增了五种请求方法: OPTIONS,PUT, DELETE, TRACE 和 CONNECT方法。
-   HTTP1.1请求详述:

|  序号 |    方法   | 描述                                                                    |
| :-: | :-----: | :-------------------------------------------------------------------- |
|  1  |   GET   | 请求指定的页面信息,并返回实体主体                                                     |
|  2  |   HEAD  | 类似于get请求,只不过返回的响应中没有具体的内容,用于获取报头                                      |
|  3  |   POST  | 向指定资源提交数据进行处理请求(例如提交表单或者上传文件)。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或巳有资源的修改 |
|  4  |   PUT   | 从客户端向服务器传送的数据取代指定的文档的内容。                                              |
|  5  |  DELETE | 请求服务器删除指定的页面。                                                         |
|  6  | CONNECT | HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。                                      |
|  7  | OPTIONS | 允许客户端查看服务器的性能。                                                        |
|  8  |  TRACE  | 回显服务器收到的请求,主要用于测试或诊断。                                                 |

-   HttpRequest 对象

    -   视图函数的第一个参数是 HttpRequest 对象
    -   服务器接收到http协议的请求后,会根据请求数据报文创建 HttpRequest 对象
    -   HttpRequest 属性
        -   path:字符串,表示请求的路由信息
        -   ✦ method:字符串,表示HTTP请求方法,常用值:'GET'、'POST'
        -   encoding:字符串,表示提交的数据的编码方式
            -   如果为 None 则表示使用浏览器的默认设置,一般为'utf-8'
            -   这个属性是可写的,可以通过修改它来修改访问表单数据使用的编码,接下来对属性的任何访问将使用新的 encoding值
        -   GET:QueryDict 查询字典的对象,包含 get 请求方式的所有数据
        -   POST: QueryDict 查询字典的对象,包含 post 请求方式的所有数据
        -   FILES:类似于字典的对象,包含所有的上传文件
        -   COOKIES: Python字典,包含所有的 cookie,键和值都为字符串
        -   session:似于字典的对象,表示当前的会话
        -   body:字符串,请求体的内容(POST或PUT)
        -   environ:字符串,客户端运行的环境变量信息
        -   scheme:请求协议('httpt'/'https')
        -   path_info:URL字符串
        -   request.get_full_path():请求的完整路径
        -   request.get_host():请求的主机
        -   request.META:请求中的元数据（消息头）
            -   request.META['REMOTE_ADDR']&#x3A;客户端IP地址
            -   request.META['HTTP_REFERER']&#x3A;请求源地址

##### HTTP响应

-   当浏览者访问一个网页时,浏览者的浏览器会向网页所在服务器发出请求。当浏览器接收并显示网页前,此网页所在的服多器会返回一个包含HTTP状态码的信息头(server header)用以响应浏览器的请求.

-   HTTP状态码的英文为 HTTP Status Code

-   下面是常见的 HTTP 状态码

    -   200: 请求成功
    -   301: 资源(网页等)被永久转移到其它URL
    -   404: 请求的资源(网页等)不存在
    -   500: 内部服务器错误

-   HTTP 状态码分类

    -   HTTP 状态码由三个十进制数字组成,第一个十进制数字定义了状态码的类型,后两个数字具有分类的作用。HTTP状态码共分为5种类型

|   分类  | 描述                      |
| :---: | ----------------------- |
| 1\*\* | 信息,服务器收到请求,需要请求者继续执行操作  |
| 2\*\* | 成功,操作被成功接收井处理           |
| 3\*\* | 重定向,需要进一步的操作以完成请求       |
| 4\*\* | 客户端错误,请求包含语法错误或无法完成请求   |
| 5\*\* | 服务器错误,服务器在处理请求的过程中发生了错误 |

-   Django中的响应对象 Httpresponse

    -   构造函数格式:

        -   `HttpResponse(content=响应体,content_type=响应数据类型,status=状态码)`

    -   作用：

        -   向客户端浏览器返回响应,同时携带响应体内容

    -   参数：

        -   content：表示返回的内容
        -   status_code:返回的HTTP响应状态码。
        -   content\_ type:指定返回数据的的 MIME 类型(默认为"text/html")。浏览器会根据这个属性,来显示数据。如果是text/html,那么就会解析这个字符串,如果text/ plain,那么就会显示一个纯文本。

            -   常用的 Content-Type如下

                -   text/html (默认的，html文件)
                -   text/plain (纯文本)
                -   text/css  (css文件)
                -   text/javascript (js 文件)
                -   multipart/from-data (文件提交)
                -   application/json (json 传输)
                -   application/xml (xml 文件)

            -   关键字 MIME(Multipurpose Internet Mail Extensions)是指多用途互联网邮件扩展类型

-   其他 Httpresponse 响应对象

    -   HttpresponseRedirect   重定向，状态码 301
    -   HttpresponseNotModified   未修改，状态码 304
    -   HttpresponseBadRequest   错误请求，状态码 400
    -   HttpresponseNotFound   没有对应的资源，状态码 404
    -   HttpresponseForbidden    请求被禁止，状态码 403
    -   HttpresponseServerError   服务器错误，状态码 500

##### GET方式传参

>  GET请求方式中可以通过查询字符串( Query String)将数据传递给服务器

###### GET方式传参参数获取(查询字符串 Query String)

-   客户端传递参数给服务器端

    -   URL 格式：`网址?参数名1=值1&参数名2=值2...`

-   服务端接收参数

    1.  判断 request.method 的值判断请求方式是否是 get 请求

        ```py
        if request.method == 'GET':
            去往指定的模板进行显示
        else：
            接收其他请求提交的数据
        ```

    2.  获取客户端请求 GET 请求提交的数据

        1.  语法

            -   `request.GET['参数名']`
            -   `request.GET.get('参数名','默认值')`
            -   `request.GET.getlist('参数名')`

        2.  能产生 get 请求方式的场合

            1.  地址栏手动输入
            2.  `<a href='地址?参数=值&参数=值'>`
            3.  表单的method为get

                ```html
                    <form method="get" action="/user/login">
                        姓名：<input type="text" name="uname">
                    </form>
                ```

        ```py
            urlpatterns = [
                url(r'^get_birthday$', views.get_birthday),
            ]

            def get_birthday(request):
                if request.method == 'GET':
                    year = request.GET.get('year', '0000')
                    month = request.GET.get('month', '00')
                    day = request.GET.get('day', '00')
                    return HttpResponse("birthday is %s-%s-%s" % (year, month, day))
        ```

##### POST方式传参

-   客户端通过表单等POST 请求将数据传递给服务器端

    ```xml
        <form method="post" action="/user/login">
            姓名：<input type="text" name="uname">
        </form>
    ```

-   服务器端接收参数

    -   通过request.method 来判断是否为 POST 请求，如：

        ```py
        if request.method == 'POST':
            处理POST 请求的数据并响应
        else：
            处理其他请求提交的数据并响应
        ```

    -   使用 POST 方式接收客户端数据

        1.  语法

            -   `request.POST['参数名']`
            -   `request.POST.get('参数名','默认值')`
            -   `request.POST.getlist('参数名')`

    -   取消 csrf 验证，否则 Django 将会拒绝客户端发来的请求
        -   删除 settings.py 中 MIDDLEWARE 中的 CsrfViewMiddleware 的中间件

    ```py
        def search(request):
            html = '''
            <html lang="en">
            <head>
                <title>Document</title>
            </head>
            <body>
                <form action="/search" method="POST">
                    <input type="text" name="username">
                    <input type="submit">
                </form>
            </body>
            </html>
            '''
            if request.method == 'GET':
                return HttpResponse(html)
            elif request.method == 'POST':
                tbl = request.POST.get('username', 'zf')
                return HttpResponse('tbl : ' + tbl)
            else:
                return HttpResponse("other ....")
    ```

#### Django框架模式

-   MVC设计模式

    -   MVC代表 Model-View-Controller(模型-视图-控制器)模式
    -   作用:降低模块间的耦合度(解耦)
    -   MVC
        -   M 模型层(Model),主要用于对数据库层的封装
        -   V 视图层(View),用于向用户展示结果
        -   C 控制 (Controller),用于处理请求、获取数据、返回结果(重要)

-   MTV模式

    -   MTV代表 Model-Template-View(模型-模板-视图)模式。这个模式用于应用程序的分层开发
    -   作用：降低模块间的耦合度(解耦)
    -   MTV
        -   M 模型层(Model),负责与数据库交互
        -   T 模板层(Templates),负责呈现网页内容
        -   V 视图层(View),负责接收请求 获取数据 返回结果（核心）

##### 模板 Templates

-   什么是模板

    1.  模板是html页面,可以根据视图中传递的数据填充值相应的√页面元素。
    2.  模板层提供了一个对设计者友好的语法用于渲染向用户呈现的信息。

-   模板的配置

    -   创建模板文件夹 &lt;项目名>/templates
    -   在 settings.py 中有一个 TEMPLATES 变量
        1.  BACKEND: 指定模板的引擎
        2.  DIRS：指定保存模板的目录
        3.  APP_DIRS：是否要在应用中搜素模板版本
        4.  OPTIONS:有关模板的选项

-   默认的模板文件夹 templates

-   默认settings.py 文件，设置 TEMPLATES 的 DIRS 值为

    -   `'DIRS':[os.path.join(BASE_DIR,'templates')],`

-   模板的加载方式

    1.  通过 loader 获取模板，通过 HttpResponse 进行响应

        ```py
            # views.py
            from django.http import HttpResponse
            from django.template import loader

            def page1_template(request):
                t = loader.get_template('page1.html')  # 加载模板
                html = t.render()  # 渲染成字符串
                return HttpResponse(html)
        ```

    2.  使用 render() 直接加载并响应模板

        ```py
            # views.py
            from django.shortcuts import render

            def page1_template(request):
                return render(request, 'page1.html')
        ```

-   模板的传参

    -   模板传参是指把数据形成字典,传参给模板,由模板渲染来填充数据

    1.  使用 loader 加载模板

        ```py
            t = loader.get_template('page1.html')
            html = t.render(字典数据)
            return HttpResponse(html)
        ```

    2.  使用 render 加载模板

        ```py
            return render(request,'xx.html',字典数据)
        ```

###### Django模板语言:( The Django template language)

-   模板的变量

    1.  在模板中使用变量语法：`{{ 变量名 }}`

        -   后端中必须将变量封裝到字典中才允许传递到模板上dic={'变量1':'值1','变量2':'值2',}

-   模板的标签

    1.  作用 将一些服务器端的功能嵌入到模板中
    2.  标签语法

    ```html
        {% 标签 %}
        ...
        {% 结束标签 %}
    ```

    3.  if标签

        ```html
            {% if 条件表达式 %}
            ...
            {% elif 条件表达式 %}
            ...
            {% else %}
            ...
            {% endif %}
        ```

        -   if 条件表达式 里可以使用的运算符

            -   `== != < > <= >= in not in is is not not and or`

        -   在 if 标记中使用实际括号是无效的语法，如果需要它们指定优先级，则应使用嵌套的 if 标记。

    4.  for 标签

        1.  语法

        ```html
            {% for 变量 in 可迭代对象 %}
            ...
            {% endfor %}

            # ex.
            <ul>
                {% for i in fav %}
                    <li>{{ i }}</li>
                {% endfor %}
            </ul>
        ```

        2.  内置变量 forloop

|          变量         | 描述                 |
| :-----------------: | ------------------ |
|   forloop.counter   | 循环的当前迭代(从1开始索引)    |
|   forloop.counter0  | 循环的当前迭代(从0开始索引)    |
|  forloop.revcounter | 循环结束的迭代次数(从1开始索引)  |
| forloop.revcounter0 | 循环结束的迭代次数(从0开始索引)  |
|    forloop.first    | 如果这是第一次通过循环,则为真    |
|     forloop.last    | 如果这是最后一次循环,则为真     |
|  forloop.parentloop | 对于嵌套循环，这是围绕当前循环的循环 |

        2.  for ... empty 标签

            ```html
            /* 可迭代对象没用任何数据时 */
            {% for 变量 in 可迭代对象 %}

            {% empty %}

            {% endfor %}
            ```

    4.  cycle 标签

        -   循环从 cycle 列表后的参数中进行取值，每次调用进行一次更换
        -   这个标签经常用于循环中，ex. 处理表格的隔行变色
        -   语法：

            ```html
                {% for o in some_list %}
                    <tr class="{% cycle 'row1' 'row2' %}">
                        ...
                    </tr>
                {% endfor %}

                /* ex. */
                {% for i in fav %}
                    <tr class="{% cycle 'row1' 'row2' %}">
                        <td>{{ forloop.counter }}</td>
                        <td>{{ i }}</td>
                    </tr>
                {% endfor %}
            ```

    4.  注释 和 comment 标签

        -   单行注释：`{# ...注释 #}` 该范围内的文字信息会被模板的渲染系统忽略
        -   多行注释：`{% comment %} ...注释 {% endcomment %}` 之间的内容会被忽略
            -   comment 标签不能嵌套使用
        -   模板级的注释，html 源码不显示

###### 过滤器

1.  作用：

    -   在变量输出前对变量的值进行处理
    -   您可以通过使用过滤器来改变变量的显示。

2.  语法:`{{ 变量1 | 过滤器1:值1 }}`

    -   ex.: `{{ string | truncatechars:9 | upper }}`

3.  常用过滤器

| 过滤器             | 备注                                               |
| --------------- | ------------------------------------------------ |
| default         | 如果 value 的计算结果为 False,则使用给定的默认值。否则使用该 value      |
| default_if_none | 如果(且仅当) value 为 None ,则使用给定的默认值。否则,使用该 value     |
| floatformat     | 当不使用参数时,将浮点数舍入到小数点后一位,但前提是要显示小数部分。               |
| truncatechars   | 如果字符串字符多于指定的字符数量,那么会被截断。截断的字符串将以可翻译的省略号序列("…")结尾 |
| truncatewords   | 在一定数量的字后截断字符串                                    |
| lower           | 将字符串转换为全部小写                                      |
| upper           | 将字符串转换为大写形式                                      |

###### escape 转译

-   escape 转义字符串的HTML。具体来说,它使这些替换:

-   `<`转换为`&lt;`
-   `>`转换为`&gt;`
-   `'`转换为`&#39;`
-   `"`转换为`&quot;`
-   `&`转换为`&amp;`

```html
    {% autoescape on/off %} # 启动 / 关闭 转译
        {{ a }}
    {% endautoescape %}
```

###### 模板的继承

-   模板继承可以使父模板的內容重用，子模板直接继承父模板的全部内容并可以覆盖父模板中相应的块
-   定义父模板中的块 blcok 标签
    -   标识出哪些在子模块中是允许被修改的
    -   block 标签：在父模板中定义，可以在子模板中覆盖
