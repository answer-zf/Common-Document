# Webpack

> webpack 是前端的一个项目构建工具，它是基于 Node.js 开发出来的一个前端工具；

## 前提

### 网站构建中：网页中引入的静态资源过多，出现的问题

1. 网页加载速度慢， 因为 我们要发起很多的二次请求；
2. 要处理错综复杂的依赖关系

### 如何解决上述两个问题

1. 合并、压缩、精灵图、图片的Base64编码
2. 可以使用`requireJS`、也可以使用`webpack`可以解决各个包之间的复杂依赖关系；

### 解决方案

1. 使用Gulp， 是基于 task 任务的；
2. 使用`Webpack`， 是基于整个项目进行构建的；
   - 借助于`webpack`这个前端自动化构建工具，可以完美实现资源的合并、打包、压缩、混淆等诸多功能。
   - 根据官网的图片介绍`webpack`打包的过程

## 起步：

### 安装

1. 运行`npm i webpack -g`全局安装`webpack`，这样就能在全局使用`webpack`的命令
2. 在项目根目录中运行`npm i webpack --save-dev`安装到项目依赖中

### 初步使用`webpack`打包构建列表隔行变色案例

1. 运行`npm init`初始化项目，使用 `npm` 管理项目中的依赖包
2. 创建项目基本的目录结构
3. 使用`cnpm i jquery --save`安装 `jquery` 类库
4. 创建`main.js`并书写各行变色的代码逻辑：

```js
// 导入jquery类库
import $ from 'jquery'
// 设置偶数行背景色，索引从0开始，0是偶数
$('#list li:even').css('backgroundColor','lightblue');
// 设置奇数行背景色
$('#list li:odd').css('backgroundColor','pink');
```

5. 直接在页面上引用 `main.js` 会报错，因为浏览器不认识 `import` 这种高级的JS语法，需要使用 `webpack` 进行处理，`webpack` 默认会把这种高级的语法转换为低级的浏览器能识别的语法；
6. 运行 `webpack 入口文件路径 输出文件路径` 对 `main.js` 进行处理：

```shell
webpack src/js/main.js dist/bundle.js
```

总结：

1. `webpack` 能够处理 JS 文件的互相依赖关系；
2. `webpack` 能够处理JS的兼容问题，把 高级的、浏览器不是别的语法，转为 低级的，浏览器能正常识别的语法

### 使用 `webpack` 的配置文件简化打包时候的命令

1. 在项目根目录中创建`webpack.config.js`
2. 由于运行 `webpack` 命令的时候，`webpack` 需要指定入口文件和输出文件的路径，所以，我们需要在`webpack.config.js`中配置这两个路径：

```js
const path = require('path')
module.exports = {
  entry: path.join(__dirname, './src/main.js'), // 项目入口文件
  output: { // 配置输出选项
    path: path.join(__dirname, './dist'), // 配置输出的路径
    filename: 'bundle.js' // 配置输出的文件名
  }
}
```

在控制台，直接输入 `webpack` 命令执行的时候，`webpack` 做了以下几步：

1. 首先，`webpack` 发现，我们并没有通过命令的形式，给它指定入口和出口
2. `webpack` 就会去 项目的 根目录中，查找一个叫做 `webpack.config.js` 的配置文件
3. 当找到配置文件后，`webpack` 会去解析执行这个 配置文件，当解析执行完配置文件后，就得到了 配置文件中，导出的配置对象
4. 当 `webpack` 拿到 配置对象后，就拿到了 配置对象中，指定的 入口  和 出口，然后进行打包构建；

### 实现`webpack`的实时打包构建

1. 由于每次重新修改代码之后，都需要手动运行`webpack`打包的命令，比较麻烦，所以使用`webpack-dev-server`来实现代码实时打包编译，当修改代码之后，会自动进行打包构建。

2. 运行`npm i webpack-dev-server --save-dev`安装到开发依赖

   - 由于，我们是在项目中，本地安装的 `webpack-dev-server` ， 所以，无法把它当作 脚本命令，在`powershell` 终端中直接运行；（只有那些 安装到 全局 -g 的工具，才能在 终端中正常执行）

   - `webpack-dev-server` 这个工具，如果想要正常运行，要求，在本地项目中，必须安装 `webpack`

3. 安装完成之后，在命令行直接运行`webpack-dev-server`来进行打包，发现报错，此时需要借助于`package.json`文件中的指令，来进行运行`webpack-dev-server`命令，在`scripts`节点下新增`"dev": "webpack-dev-server"`指令，发现可以进行实时打包，但是`dist`目录下并没有生成`bundle.js`文件，这是因为`webpack-dev-server`将打包好的文件托管到了 电脑的内存中，并没有存放到 实际的 物理磁盘上，所以，我们在 项目根目录中，根本找不到 这个打包好的 `bundle.js`

   - 我们可以认为， `webpack-dev-server` 把打包好的 文件，以一种虚拟的形式，托管到了 咱们项目的 根目录中，虽然我们看不到它，但是，可以认为， 和 `dist`  `src`   `node_modules`  平级，有一个看不见的文件，叫做 `bundle.js`

 + 把`bundle.js`放在内存中的好处是：由于需要实时打包编译，所以放在内存中速度会非常快

 + 这个时候访问`webpack-dev-server`启动的`http://localhost:8080/`网站，发现是一个文件夹的面板，需要点击到`src`目录下，才能打开我们的index首页，此时引用不到`bundle.js`文件，需要修改`index.html`中`script`的`src`属性为:`<script src="/bundle.js"></script>`

 + 在 `package.json` 中设置 `scripts`节点下中的`"dev"` 

    + `--open` 运行直接打开浏览器
    + `--port 3000`设置启动时候的运行端口
    + `--contentBase src` 设置托管的根目录
    + `--hot` 减少不必要的代码更新，浏览器无刷新重载样式

   ```
   "dev": "webpack-dev-server --open --port 3000 --contentBase src --hot"
   ```

   也可以在 `webpack.config.js` 配置文件中配置

   ```js
   const webpack = require('webpack') // 启用热更新的 第1步
   module.exports = {
   	···
     devServer: { // 这是配置 dev-server 命令参数的第二种形式，相对来说，这种方式麻烦一些
       open: true, // 自动打开浏览器
       port: 3000, // 设置启动时候的运行端口
       contentBase: 'src', // 指定托管的根目录
       hot: true // 启用热更新的 第2步
     },
     plugins: [ // 配置插件的节点
       new webpack.HotModuleReplacementPlugin() 
     ] 																	// new 一个热更新的 模块对象，启用热更新的 第3步
     ···
   }
   ```

### 使用`html-webpack-plugin`插件配置启动页面

在内存中根据`index.html` 模板页面生成内存中的首页。

1. 运行`cnpm i html-webpack-plugin --save-dev`安装到开发依赖

2. 配置 `webpack.config.js`

   ```js
   const htmlWebpackPlugin = require('html-webpack-plugin')
   // 导入在内存中生成 HTML 页面的 插件
   // 只要是插件，都一定要 放到 plugins 节点中去
   // 这个插件的两个作用：
   //  1. 自动在内存中根据指定页面生成一个内存的页面
   //  2. 自动，把打包好的 bundle.js 追加到页面中去
   module.exports = {
   	···  
     plugins: [
       new htmlWebpackPlugin({ // 创建一个 在内存中 生成 HTML  页面的插件
         template: path.join(__dirname, './src/index.html'), // 指定 模板页面，将来会根据指定的页面路径，去生成内存中的 页面
         filename: 'index.html' // 指定生成的页面的名称
       })
     ]
     ···
   }
   ```

### 使用webpack打包css文件

注意：webpack, 默认只能打包处理 JS 类型的文件，无法处理 其它的非 JS 类型的文件

如果要处理 非JS类型的文件，我们需要手动安装一些 合适 第三方 loader 加载器；

1. 使用 import 语法，导入 CSS样式表 `import './css/index.css'`

2. 如果想要打包处理 `css` 文件，需要安装 `cnpm i style-loader css-loader -D`

3. 打开 `webpack.config.js` 这个配置文件，

   - 在 里面，新增一个 配置节点，叫做 `module`, 它是一个对象；
   - 在 这个 `module` 对象身上，有个 `rules` 属性，这个 `rules` 属性是个 数组；
   - 这个数组中，存放了，所有第三方文件的 匹配和 处理规则；
   - `use`表示使用哪些模块来处理`test`所匹配到的文件；
   - `use`中相关loader模块的调用顺序是从右向左调用的；

   ```js
   module: { // 这个节点，用于配置 所有 第三方模块 加载器 
     rules: [ // 所有第三方模块的 匹配规则
       { test: /\.css$/, use: ['style-loader', 'css-loader'] } 
       															//  配置处理 .css 文件的第三方loader 规则
     ]
   }
   ```

注意： `webpack` 处理第三方文件类型的过程：
1. 发现这个 要处理的文件不是`JS`文件，然后就去 配置文件中，查找有没有对应的第三方 `loader` 规则
2. 如果能找到对应的规则， 就会调用 对应的 `loader` 处理 这种文件类型；
3. 在调用`loader` 的时候，是从后往前调用的；
4. 当最后的一个 `loader` 调用完毕，会把 处理的结果，直接交给 `webpack` 进行 打包合并，最终输出到  `bundle.js` 中去

#### 使用webpack打包less文件

1. 运行`npm i less-loader less -D`
   - `less-loader`内部依赖`less`， 不需要显示定义配置文件中
2. 修改`webpack.config.js`这个配置文件：

```js
{ test: /\.less$/, use: ['style-loader', 'css-loader', 'less-loader'] },
```

#### 使用webpack打包sass文件

1. 运行`npm i sass-loader node-sass --save-dev`
2. 在`webpack.config.js`中添加处理sass文件的loader模块：

```js
{ test: /\.scss$/, use: ['style-loader', 'css-loader', 'sass-loader'] }
```

注意：Webpack 2X以上版本，加载器必须带 `-loader`，1X的版本不需要带。