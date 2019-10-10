# Node.js_Basic



## Node.js 概述

- Node.js 是JavaScript运行时环境

- 可以解析执行JavaScript代码

- 没有BOM 、DOM

- 遵循EcmaScript

- 为JavaScript提供了服务器级别的操作API

- 构建与Chrome的V8引擎之上

  - Google Chrome 中的V8引擎世界上公认的解析执行JavaScript代码最快的

  - Node.js作者把Google Chrome 中的V8引擎移出来，开发了独立的JavaScript运行时环境

  

## Node.js 特性

- event-driven 事件驱动

- non-blocking I/O model 非阻塞IO模型（异步）

- lightweight and efficient 轻量和高效



## Node.js 功能

- WEB服务器后台
  - B/S编程模型（与语言无关）
  - 模块化编程 （类似less  @import('文件路径')  引用加载文件）
  - 异步编程
    - promise
    - async
    - generator 
  
  - Express Web开发框架
  - Ecmascript 6
  
- 命令行工具
  
  - git	（ C ）
  - npm（ Node ）
  - hexo（ Node ）



## Node.js 基本操作



### 执行文件

```shell

## 创建编写js脚本文件
## 打开终端，定位到脚本文件所属目录
## 输入node '文件名' 执行对应的文件  -- 文件名不能以node.js命名否则会打开这个文件

$node begin.js

```



### 读取文件

```js

// 执行文件操作必须引入fs这个核心模块（file-system）
// 使用 require 方法载入fs核心模块

var fs = require('fs')

fs.readFile('url',function(error,data){   // URL：要读取的文件路径 （统一资源定位符）
	if(error){
	 	console.log('读取错误')
        return
    }
    console.log(data.toString())
})
// 读取成功 error 返回 null   ，data 返回 数据									
// 读取失败 error 返回 错误对象，data 返回 undefined

## ps: data 返回的数据是将文件存储的二进制数据 转为 十六进制数据，展现
##	   可以用 toString 方法转为 字符串
```



### 读取目录

```javascript

var fs = require('fs')
fs.readdir('url', function(err, files) {  // files: 返回数组
  if (err) {
    res.end('Not Found Root Dir')
    return
  }
  console.log(files)  
})

```



### 写入文件

```js

var fs = require('fs')
fs.writeFile('url','content',function(error){ // content: 写入文件内容   error: 形参
     if(error){
		console.log('写入失败')
     }else{
        console.log('写入成功')
     }
})

## 写入成功 error 返回 null
## 写入失败 error 返回 错误对象

```



### 创建服务器

```javascript

// Node中有一个核心模块 http ,职责创建编写服务器

// 加载http核心模块
var http = require('http')

// 使用http.createServer() 方法创建web服务    ## 返回一个Server实例
var server = http.createServer()

// 接受请求
// 处理请求
// 返回响应

// 注册 request 请求事件
// 当客户端请求时，自动触发服务器的 request 请求事件，然后执行第二个参数：回调处理函数 
server.on('request', function(request,response){
    console.log('收到请求,请求路径' + request.url) 
    response.write('hello')
    response.write(' node.js')
    response.end()
  	// 简化
  	response.end('hello node.js')
})

## request  请求事件处理函数，需接收两个参数：
## Request  请求对象（获取客户端请求信息：如请求路径）
						## req.url 获取端口号以后的路径，所有url都是以 / 开头的 默认为 /
## Response 响应对象（给客户端发送响应信息）有 writer方法 ：给客户端发送响应数据
						## writer方法 ：给客户端发送响应数据
            ## write 可以使用多次，但是最后一定要使用end结束响应，否则客户端会一直等待。
            ## 简化操作 直接end的同时发送响应数据 response.end('str')
            ## response.end()支持两种数据类型：二进制 字符串
            
## response.end()	一次请求对应一次响应，响应结束这次请求也结束  不执行后续代码  类似return
## response.end() 必须存在

// 绑定端口号，启动服务器。

server.listen(3000,function(){
    console.log('服务器启动成功，可以通过 http://127.0.0.1:3000/，进行访问')
})

// 此时终端被服务占用，关闭终端即关闭服务器（X掉，或者 Ctrl+c 终止），有响应便返回响应

```



#### - 创建服务简写

```js

http
		.createServer(function (req, res) {
  
		})
		.listen(3000,function () {
  		console.log('Server is running')
		})
```



### 获取路径

- 采用URL模块，获取

```js

var url = require('url')

var obj =url.parse('http://127.0.0.1:3000/post?name=fasdf&mes= asdf', true)
														// true： 可以让里面的query 将所传入的参数转为对象
console.log(obj)

------------------------------------------
$
  protocol: 'http:',	// 协议
  slashes: true,
  auth: null,
  host: '127.0.0.1:3000',  
  port: '3000',	// 端口号
  hostname: '127.0.0.1',	// 主机名
  hash: null,
  search: '?name=fasdf&mes=%20asdf',	// 查询字符串（ GET参数 ）
  query: [Object: null prototype] { name: 'fasdf', mes: ' asdf' },
  pathname: '/post',
  path: '/post?name=fasdf&mes=%20asdf',
  href: 'http://127.0.0.1:3000/post?name=fasdf&mes=%20asdf' }
```





## Node.js 中 的 JavaScript

- EcmaScript
- 核心模块
- 第三方模块
- 用户自定义模块

### 核心模块

Node为JavaScript提供了很多服务器级别的API，而且这些API绝大多数都被包装到了一个具名的核心模块中。他们都有自己特殊的名称标识，若要使用这些模块，必须用  ***require***  加载模块。

- 文件操作的核心模块：fs
- 服务构建的核心模块：http
- 路径处理的核心模块：path
- 路径操作的核心模块：url
- 操作系统信息的核心模块：os
- ...



```javascript

var path = require('path')
console.log(path.extname('url'))

// 返回扩展名 .txt
```



### 用户定义模块

#### require  方法

​	**用来加载模块，并执行里面的代码**（ 可加载执行多个JavaScript脚本文件 ）

​    **拿到被加载文件模块导出的接口对象**



- node中模块分三种

  - 具名的核心模块 （ fs 、http ...）

  - 用户编写的文件模块

    ​    相对路径必须加 ./ 或 ../    （ ./ 不能省略，否则报错）

    ​	可以省略后缀名

  - 第三方模块

    

    ```js
    console.log('a.js => stat')
    require('./b')
    console.log('a.js => end')
    ```

    

- node中没有全局作用域，只有模块作用域（即文件作用域）

  - 模块是完全封闭的
    - 文件与文件之间可以完全避免变量命名冲突、污染问题
    - 外部访问不到内部，内部访问不到外部



#### exports 对象

**每个文件模块都提供了  *exports*  对象 （ 默认是空对象 ）**

- 由于node只有模块作用域，想要做到模块间通信需要用到  ***exports***

- 把需要被外部访问的成员手动挂载到 ***exports*** 接口对象中

- 多次在 **exports** 添加成员，实现对外导出多个内部成员

- 哪个文件 ***require*** 这个的模块，就可以得到模块内部的   ***exports***  接口对象

  - 即：***require***  的返回值
  
  ```javascript
  
  ## └─ducument
  ##    ├─a.js
  ##    └─b.js
  
  ## ----  b.js content
  
  var foo = '1231234'
  exports.foo = foo
  
  exports.add = function (x, y) {
      return x + y
  }
  
  ------------------------------------------
  
  ## ----  a.js content
  
  var bExports = require('./b')
  console.log(bExports.foo)
  console.log(bExports.add(10, 210))
  
  ```

- 一个模块需要直接导出某个成员，而非挂载的方式必须使用

  `module.exports = add`

  - add 可为 function，string， array。。都可以


## Web 服务端开发



### IP地址  与  端口号



- 所有联网的程序都要进行网络通信

- 计算机中只有一个物理网卡，且同一个局域网中的网卡地址必须唯一。

- 网卡是通过唯一的ip地址进行定位



**IP 地址用来定位计算机**

**端口号用来定位应用程序**

- 所有需要网络通信的软件都必须有端口号
- 端口号使用范围 0 ~ 65536 之间
- 计算机中有一些默认端口号 尽量不去使用 ex : 80 ..
- 一台计算机，同一个端口号在同一时间，只能被一个 
- Node.js 可以开启多个服务，但是一定确保不同服务占用不同端口号



### Content-Type

- 服务端发送的数据默认，是utf-8编码的

- 浏览器在不知道服务器响应内容的编码的情况下，会按照当前操作系统默认的编码去解析
  - 中文操作系统默认编码是 GBK
  - 在http协议中 Content-Type是用来告知，对方给你发送数据内容的数据类型
  - 图片不需要指定编码，常说的编码一般指的是：字符编码，一般只为字符数据指定编码

- **通过设置响应头的方式设置Content-Type的方式解决乱码问题**

  ```js
  
  server.on('request', function(req, res){
      res.setHeader('Content-Type','text/plain; charset=utf-8')
      res.end('hello 世界')
  })
  
  ```

  - 服务器最好把每次响应的数据是什么内容类型 ，正确的告诉客户端
  - 不同的资源对应的 Content-Type 是不一样，具体参照：http://tool.oschina.net/commons
  - 对于文本类型的数据，最好都加上编码，目的是为了防止中文解析乱码问题

  

- 除了用 Content-Type 指定编码，也可以在HTML页面，通过meta元数据（用来 描述、特征、信息，存储内容的数据）来声明当前文本的编码格式



### 请求与响应

- 当浏览器收到HTML的响应内容以后，开始从上到下一次解析，
- 在解析过程中若发现
  - link
  - script
  - img
  - iframe
  - video
  - audio

- 等带有src href属性标签的时候，浏览器会自动对这些资源发起新的请求

  

### 统一资源管理

- 为了方便统一处理静态资源，顾将静态资源存放在同一位置
- 通过代码灵活控制那些资源能被访问，那些资源不允许访问

```js

var http = require('http')
var fs = require('fs')
http
  .createServer(function(req, res) {
    var url = req.url
    if (url === '/') {
      fs.readFile('./view/index.html', function(err, data) {
        if (err) {
          res.end('404 Not Found')
          return
        }
        res.end(data)
      })
    } else if (url.indexOf('/public/') === 0) {   // public 开启访问权限
      fs.readFile('.' + url, function(err, data) {
        if (err) {
          res.end('404 Not Found')
          return
        }
        res.end(data)
      })
    }
  })
  .listen(3000, function() {
    console.log('Server is running')
  })

```

- 上个实例，只有public目录可以提供访问，灵活控制访问资源

  

### 服务器重定向

- 状态码设置 302临时重定向

  - 301为永久重定向 浏览器会记住
  - a  => b ,下次请求a，不经过a 直接到b
  - 302为临时重定向 浏览器会记住
    - a  => b ,下次继续请求a，a  => b
  - response.statusCode = 302

- 响应头中通过 Location告诉客户端往哪重定向

  - response.setHeader( 'Location',  '/' )

- 客户端发现收到的服务器的响应状态码是302，会自动在响应头中找 Location，然后对改地址发起新的请求。

- 客户端自动跳转

  

  

  