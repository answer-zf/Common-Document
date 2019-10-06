# Node.js 概述

- Node.js 是JavaScript运行时环境

- 可以解析执行JavaScript代码

- 没有BOM 、DOM

- 遵循EcmaScript

- 为JavaScript提供了服务器级别的操作API

- 构建与Chrome的V8引擎之上

  - Google Chrome 中的V8引擎世界上公认的解析执行JavaScript代码最快的

  - Node.js作者把Google Chrome 中的V8引擎移出来，开发了独立的JavaScript运行时环境

  

# Node.js 特性

- event-driven 事件驱动

- non-blocking I/O model 非阻塞IO模型（异步）

- lightweight and efficient 轻量和高效



# Node.js 功能

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



# Node.js 基本操作



## 执行文件

```shell

## 创建编写js脚本文件
## 打开终端，定位到脚本文件所属目录
## 输入node '文件名' 执行对应的文件  -- 文件名不能以node.js命名否则会打开这个文件

$node begin.js

```



## 读取文件

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



## 写入文件

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



## 创建服务器

```js

// Node中有一个核心模块 http ,职责创建编写服务器

// 加载http核心模块
var http = require('http')

// 使用http.createServer() 方法创建web服务    ## 返回一个Server实例
var server = http.createServer()

// 接受请求
// 处理请求
// 返回响应


var http = require('http')

var server = http.createServer()

// 注册 request 请求事件
// 当客户端请求时，自动触发服务器的 request 请求事件，然后执行第二个参数：回调处理函数 
server.on('request', function(request,response){
    console.log('收到请求,请求路径' + request.url) 
    response.write('hello')
    response.write(' node.js')
    response.end()
})

## request 请求事件处理函数，需接收两个参数：
## Request  请求对象（获取客户端请求信息：如请求路径）
## Response 响应对象（给客户端发送响应信息）有 writer方法 ：给客户端发送响应数据
			## 有 writer方法 ：给客户端发送响应数据
            ## write 可以使用多次，但是最后一定要使用end结束响应，否则客户端会一直等待。
// 绑定端口号，启动服务器。

server.listen(3000,function(){
    console.log('服务器启动成功，可以通过 http://127.0.0.1:3000/，进行访问')
})

// 此时终端被服务占用，关闭终端即关闭服务器（X掉，或者 Ctrl+c 终止），有响应便返回响应

```



