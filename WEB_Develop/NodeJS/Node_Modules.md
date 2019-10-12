# Node_Modules System



## Node中的模块系统



### 前 提

- 使用Node编写应用程序主要是使用
  - EcamScript 语言
  - 核心模块
  - 第三方模块
  - 用户自定义模块

### 模块化

- 文件作用域

- 通信规则

  - 加载

  - 导出

    

### CommonJS模块规范

JavaScript本身并不支持模块化 在Node中不仅支持，还有一个很重要的概念  **模块系统**

- 模块作用域
  - 默认模块中任何内容不能被外部访问
- 使用require方法加载模块
- 使用exports接口对象导出模块中的成员

#### 加载  `require`

##### 语法：

```js
var custom = require('module')
```

##### 作用：

1. 执行被加载模块中代码
2. 得到被加载模块中的  `exports`  导出接口对象

##### 加载规则：

模块查找机制：优先从缓存加载	=>  核心模块  =>  路径形式文件模块  =>  第三方模块

###### 优先从缓存加载

- 优先从缓存加载，不会重复加载，目的是为了避免重复加载，提高模块加载效率

- 可以拿到其中的接口对象，但是不会重复执行里面的代码

  ```js
  ## └─ducument
  ##    ├─a.js
  ##    ├─b.js
  ##    └─main.js
  
  ## ----  main.js content
  
  require('./a')
  var fn = require('./b')
  console.log(fn)
  ----------------------------------
  
  ## ----  a.js content
  
  console.log('a.js 被加载了')
  var fn = require('./b')
  console.log(fn)
  ----------------------------------
  
  ## ----  b.js content
  
  console.log('b.js 被加载了')
  module.exports = function () {
    console.log('hello bbb')
  }
  ----------------------------------
  
  ## ----	 main.js输出结果
  a.js 被加载了
  b.js 被加载了
  [Function]
  [Function]
  ```

  

###### 判断模块模块标识(符)

**require('模块标识')**

- 核心模块
  - 本质：文件。
  - 已被编译到了二进制文件中，只需要按名字加载即可
  - 模块标识 ：模块名
- 第三方模块
  - 凡是第三方模块必须通过npm下载，通过require('包名')进行加载使用
  - 不可能有一个第三方包 与 核心模块 重名
  - 模块标识 ：模块名
- 用户模块
  - 模块标识 ：路径



**路径形式的模块**：

- .js     后缀名可以省略
- ./      当前目录 （不可省略）
- ../     上一级目录 （不可省略）
- /xxx	绝对路径 ( 首位的  / 表示当前文件模块所属磁盘根路径)  ==>  几乎不用
- d:/xxxx  绝对路径   ==>  几乎不用 

**既不是核心模块，也不是路径形式的模块**

1. 模块加载规则
   - 先找到当前文件所属目录中的 `node_modules` 目录    ( 以art-template 为例 )
   - == >     node_modules/art-template
   - == >     node_modules/art-template/package.json 文件
   - == >     node_modules/art-template/package.json 文件中的 main 属性
   - main属性记录了art-template的入口模块 
   - 加载使用art-template
   - 实际上最终加载的还是文件
2. 特殊情况
   - 如果 package.json 文件不存在或者 main指定的入口模块也没有，则 node 会找该目录下的 index.js
     - index.js 会作为默认备选项
   - 若所述所有条件均不成立，则会进人上一级目录中的 node_modules 目录执行查找
   - 若上一级还没有，则继续往上上一级查找
   - 。。。
   - 如果直到当前磁盘根目录还找不到，最后报错  `can not find module xxx` 

**在项目中有且只有一个 `node_modules` ，不会出现多个**

**位置：放在项目根目录中，这样项目中所有子目录中的代码都可以加载第三方包**

#### 导出 `exports`

- Node中是模块作用域，默认文件中所有成员只在当前文件模块有效

- 想要做到模块间通信需要用到  `exports` ，把需要被外部访问的成员手动挂载到 `exports` 接口对象中
  - 导出多个成员（必须在对象中）：
    - 多次在 `exports` 添加成员，实现对外导出多个内部成员
    
      ```js
      exports.a = 123
      exports.b = 'string'
      exports.c =	function(){
        console.log('string')
      }
      exports.d = {
        foo = 'bar'
      }
      ```
    
  - 导出单个成员（拿到的是函数、字符串、数组。。。）：
    
    - 一个模块需要直接导出单个成员，而非挂载的方式必须使用
    
      ```js
      module.exports = 'string'
      ```
    
      ```js
      module.exports = function (x, y) {
        return x + y
      }
      ```
    
    - 若重复使用，则后者覆盖前者
    
    - 也可以用 `module.exports =` 的操作导出多个成员
    
      ```js
      module.exports = {
       add: function(x, y){
         return x + y
       },
       str: 'string'
      }
      ```
  
  

##### 原理

- 在Node 中，每一个模块内部都有一个自己的 `module` 对象

- 该 `module` 对象中，有一个成员叫： `exports` 也是一个对象（ 默认为空 ）

- 若需要对外导出成员，只需要把导出的成员挂载到 `module.exports` 中

- 由于每次导出接口成员的时候都通过 `module.exports.xxx = xxx` 比较麻烦，node为了简化操作专门提供一个变量 `exports`  等价于  `module.exports`  

  ```js
  console.log(exports === module.exports)	// => true
  exports.foo = 'bar'
  //等价于
  module.exports.add = 'bar'
  ```
  
  固（混搭）：
  
  ```js
  exports.foo = 'bar'
  module.exports.add = function (x, y) {
    return x + y
  }
  -------------------
  // require结果
  { foo: 'bar', add: [Function] }
  ```

- 当一个模块需要导出单个成员的时候

  - 不能使用：` exports = 'string' ` 

    - `exports` 仅仅只是 `module.exports`  的引用,底层最后的代码是：
      - `var exports = module.exports`
      - `return module.exports`
    - 重新赋值不再指向 `module.exports` , 便丢失了引用关系 
    - 只是快捷方式，可以忽略

  - 只能使用：`module.exports = 'string'`

    - 重新赋值以后 `exports` 便直接失效。

      1. 底层代码：`return module.exports`
      2. 将对象赋值给变量，所存放的是地址

      ```js
      module.exports = 'string'
      exports.foo = 'bar'
      -------------
      // require结果
      'string'
      ```

      

##### 底层代码模拟

```js
var module = {
	exports: { 
	},
  ...
}
// 哪个文件 require 这个的模块，就可以得到 module.exports
// 在node最底层
// 还有一句
var exports = module.exports
// 默认在代码的最后 ：
return module.exports
```



### npm

**node package manager**

#### npm 网站

npmjs.com

#### npm 命令行工具

只要安装了node ,就安装了npm

npm也有版本概念

```shell
npm --version     ## 查看版本
```

```shell
npm install --global npm     ## 升级npm
```

#### npm 常用命令

- npm init [--yes]
  - npm init -y 跳过向导，快速生成
- npm install
  - 一次性把 dependencies 选项中的依赖项全部安装
  - npm i 
- npm install 包名
  - 只下载
  - npm i 包名
- npm install 包名 --save
  - 下载并保存依赖项（ package.json 文件中的 dependencies 选项）
  - npm i -S 包名
- npm uninstall 包名
  - 只删除，如果有依赖项会依然保存
  - npm un 包名
- npm uninstall --save 包名
  - 删除的同时也会把依赖信息也去除
  - npm un -S 包名
- npm help 
  - 查看使用帮助
- npm 命令 --help
  - 查看指定命令的使用帮助

#### 解决npm被墙问题

npm存储包文件的服务器在国外，有时候会被墙，速度很慢

https://npm.taobao.org/ 淘宝的开发团队，把npm在国内做了备份

步骤：

1. 安装淘宝的cnpm：

   ```shell
   npm install --global cnpm
   ## --global表示安装到全局，而非当前目录
   ## 这条命令中 --global不能省略
   ## 所有需要用 --global 来安装的包都可以在任意目录执行
   ```

2. 安装时包时将`npm` 替换成 `cnpm`

   ```shell
   # 这里还是走国外的npm服务器，速度比较慢
   npm install jquery
   # 使用 cnpm 通过淘宝的服务器下载
   cnpm install jquery
   ```

3. 如果不想安装 cnpm 又想使用淘宝的服务器来下载

   ```shell
   npm install jquery --registry=https://registry.npm.taobao.org
   ```

   - 每次手动加参数过于繁琐，可以把这个选项加入配置文件中：

     ```shell
     npm config set registry https://registry.npm.taobao.org
     
     ## 查看npm配置信息
     npm config list
     ```

   - 只要经过上面命令配置，以后所有的` npm install` 都会默认通过淘宝服务器来下载





### package.json

- 每个项目的根目录下都要有一个 package.json 文件 （包描述文件）

- 执行`npm install` 包名的时候都加上 --save，用来 保存依赖项信息

- package.json 可以通过 `npm init `的方式自动初始化出来
  - `dependencies` 选项，保存第三方包的依赖信息
- 若删除了node_modules 文件夹，且package.json 存在
  -  直接使用 `npm install` 找回
    - `npm install` 自动把package.json 中的dependencies 中所有的依赖项，都下载回来.



## Node_Express

**原生的http在某些方面不足以应对我们对开发的需求，需要使用框架加快开发效率，框架的目的就是提高效率，让代码更高度统一。**

**在 Node 中有很多web开发框架，Express是其中一种**     http://expressjs.com/



### 起步

#### 安装：

```js
npm install --save express
```



#### hello world

```js
var express = require('express')
// 创建app   =>相当于 http.creataServer
var app = express()
app.get('/', function(req, res) {
  res.send('hello world')
})
app.listen(5000, function() {
  console.log('express app is running...')
})
```



#### 基本路由 router

路由

- 请求方法
- 请求路径
- 请求处理函数

get：

```js
// 当以 get 方法请求 / 的时候，执行对应的处理函数 => 路由 / 映射关系
app.get('/', function(req, res) {
  res.send('hello world')
})
```

post:

```js
// 当以 post 方法请求 / 的时候，执行对应的处理函数 => 路由 / 映射关系
app.post('/', function(req, res) {
  res.send('Got a POST request')
})
```

重定向：

```js
res.redirect('/')
```

#### 静态服务

```js
## └─Project Directory
##    └─public
## 			 └─main.js

// 当以 /public/ 开头的时候 ，去 ./public/ 目录中 查找对应的资源
app.use('/public/', express.static('./public/'))      ## 推荐
--------
## 访问路径：http://127.0.0.1:5000/public/main.js

// 当省略第一个参数的时候，可以通过省略/public的方式来访问
app.use(express.static('./public/'))
--------
## 访问路径：http://127.0.0.1:5000/main.js

// /a 相当于 /public的别名
app.use('/static/', express.static('./public/'))
--------
## 访问路径：http://127.0.0.1:5000/static/main.js

```

#### 在Express中获取表单 GET请求参数

Express内置了一个API，可以直接通过 `req.query` 来获取

```js
req.query
```

#### 在Express中获取表单 POST 请求体数据

在Express中没有内置获取表单 POST 请求体的API，需要主要使用第三方包：`body-parser` 中间件（插件，专门用来解析表单 post 请求体）

安装：

```js
npm install --save body-parser
```

配置：

```js
var express = require('express')
var bodyParser = require('body-parser')

var app = express()

// 配置 body-parser
// 加入这个配置后,则在 req 请求对象上会多出来一个属性： body
// 通过 req.body 获取表单 POST 请求体数据
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))
// parse application/json
app.use(bodyParser.json())

```

使用：

```js
app.use(function (req, res) {
  res.setHeader('Content-Type', 'text/plain')
  res.write('you posted:\n')
  // 可以通过 req.body 来获取表单 POST 请求体数据
  res.end(JSON.stringify(req.body, null, 2))
})
```



### 在Express中配置使用art-template模板引擎

- [art-template - GitHub 仓库](https://github.com/aui/art-template)

- [art-template - 官方文档](https://aui.github.io/art-template/zh-cn/index.html)

####安装：

```shell
npm install --save art-template
npm install --save express-art-template
```

####配置：

```js
app.engine('html', require('express-art-template'))
```

####使用：

```js
app.get('/', function(req, res) {
  // express 默认会去项目中的 views 目录中找 index.html
  // render方法 => 渲染文件 详解见说明
  res.render('index.html', {
     title: 'hello world'
  })
})
```

- 如果希望修改默认的 `views` 视图渲染存储目录

  ```js
  // 注意第一个参数 views 千万不能错
  app.set('views', 目录路径)
  ```

#### 说明:

- **配置art-template 模板引擎**

  ```js
  app.engine('art', require('express-art-template'))
  ```

  - 第一个参数表示：当渲染以 .art 结尾的文件的时候，使用 art-template 模板引擎
    - 个人习惯 `app.engine('html', require('express-art-template'))`
  - express-art-template 是专门用来在 Express 中 把 art-template 整合到 Express中
  - 虽然这里不需要加载 art-template 但是也必须安装
  - 原因是 express-art-template 依赖了 art-template

- **使用art-template 模板引擎**

  - Express 为 Response 相应对象提供了一个方法：render
  - render 方法默认是不可以使用的，但是如果配置了模板引擎就可以使用了

  ```js
  res.render('html模板名', {模板数据})
  ```

  - 第一个参数不能写路径，默认会去项目中的 views 目录查找该模板文件
  - Express有个约定，开发人员把所有的视图文件都放到 views 目录中

  ```js
  app.get('/', function(req, res) {
    res.render('index.html')// 若不需要模板引擎渲染，第二个参数不用传，直接渲染文件页面
  })
  ```

  - 若要访问 views 下目录中的文件，直接跳过 views/ 即可

  ```js
  ## └─ views
  ##    └─ admin
  ## 			 └─ index.js
  app.get('/admin', function(req, res) {
    res.render('admin/index.html', {
      title: 'index page'
    })
  })
  ```

  