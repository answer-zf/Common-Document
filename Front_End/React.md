# React

## 移动 App 开发环境配置

### 安装 Java jdk 1.8 (开发网站，客户端的环境)

**配置环境变量**

-   新建系统环境变量 `JAVA_HOME` , 值为：`C:\Program Files\Java\jdk1.8.0_121` (jdk 的根目录)

-   修改系统环境变量 `Path` , 新增：`%JAVA_HOME%\bin` 、 `%JAVA_HOME%\jre\bin`

-   新建系统环境变量 `CLASSPATH` , 值为：`.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;`

-   验证：命令行中输入 `javac`

### 安装 Node.js

### 安装 C++

### 安装 Git

### 安装 Python 2.7

> 注意勾选安装界面上的 Add Python to path , 验证：命令行中输入 `python`

### 配置安卓环境

1.  安装 SDK

    -   勾选：`Install for anyone using this computer`

    -   修改路径 `C:\Android`

2.  打开 `C:\Android\platforms` ，将 `android-23`(react-native 依赖) 、 `android-24` 、 `android-25` 解压后，放到该文件夹下

3.  打开 `C:\Android` , 将 `platform-tools` 解压后，放到该文件夹下

4.  配置 `build-tools`

    -   打开 `C:\Android` , 新建 `build-tools` 文件夹
    -   将
        -   `build-tools_r23.0.1-windows.zip` (react-native 依赖) ,
        -   `build-tools_r23.0.2-windows.zip` (weex 依赖) ,
        -   `build-tools_r23.0.3-windows.zip` 分别解压后，
    -   分别改名为 `23.0.1` , `23.0.2` , `23.0.3` , 放到该文件夹下

5.  打开 `C:\Android` , 新建 `extras` 文件夹，在 `extras` 文件夹下新建 `android` 文件夹；解压 `m2responsitory` 文件夹和 `support` 文件夹，放到新建的 `C:\Android\platforms\extras\android` 下

6.  配置环境变量

    -   新建系统环境变量 `ANDROID_HOME` , 值为：`C:\Android` (SDK 的根目录)

    -   修改系统环境变量 `Path` , 新增：`%ANDROID_HOME%\tools` 、 `%ANDROID_HOME%\platform-tools`

### 安装 yarn react-native-cli

-   `npm install -g yarn react-native-cli`

-   设置 yarn 淘宝镜像：
    -   `yarn config set registry https://registry.npm.taobao.org -g`
    -   `yarn config set disturl https://npm.taobao.org/dist --global`

### react native 快速打包

1.  初始化项目 ：`react-native init projectname`

2.  **切换到项目目录**, 将手机连接电脑, 运行 `adb devices` , 确认手机是否连接

3.  `react-native run-android` , 设备上安装并启动应用

[Weex 快速打包](http://weex.apache.org/cn/guide/tools/toolkit.html)

1.  安装依赖:Weex 官方提供了 weex-toolkit 的脚手架工具来辅助开发和调试。首先，你需要最新稳定版的 Node.js 和 Weex CLi。
2.  运行`npm install -g weex-toolkit`安装 Weex 官方提供的 `weex-toolkit` 脚手架工具到全局环境中
3.  运行`weex create project-name`初始化 Weex 项目
4.  进入到项目的根目录中，打开 cmd 窗口，运行`weex platform add android`安装 android 模板，首次安装模板时，等待时间较长，建议 fq 安装模板
5.  打开`android studio`中的`安卓模拟器`，或者将`启用USB调试的真机`连接到电脑上，运行`weex run android`，打包部署 weex 项目
6.  部署完成，查看项目效果

## ReactJs

### React 基础

#### 安装：

```bash
npm install react react-dom -S
```

#### 起步

```js
import React from 'react'
import ReactDOM from 'react-dom'
// 参数1：创建元素的类型 => string
// 参数2：元素上的属性 => Object
// 参数3 + ：当前元素的子节点
const div = React.createElement('div',{id: 'zf', className: 'zf', title: 'title'}, 'this.is.div')
// 使用 ReactDOM 把元素渲染到页面指定的容器中：
// 参数1：要渲染的虚拟DOM元素
// 参数2：要渲染到页面上的哪个位置中
ReactDOM.render(div, document.getElementById('app'))
```

#### JSX (语法糖)

1.  安装：

    -   `npm i babel-preset-react -D`

2.  配置：

    -   在 .babelrc 文件 presets 的值添加 "react"

3.  使用：

    ```js
    const div = React.createElement('div',{id: 'zf', className: 'zf', title: 'title'}, 'this.is.div')
    // 可替换为：
    const div = (
      <div className="zf" id="zf" title="title">
        this.is.div
      </div>
    )
    ```

4.  语法：

    -   变量的使用，用 `{}` 包含使用

        ```js
        const title = 'this.is.variable'
        const div = (
          <div className="zf" id="zf" title={title}>
            this.is.div
          </div>
        )
        ```

        > 当 编译引擎，在编译JSX代码的时候，如果遇到了&lt; 那么就把它当作 HTML 代码去编译，如果遇到了 {} 就把 花括号内部的代码当作 普通JS代码去编译；

    -   在 `{}` 内部，可以写任何符合 JS 规范的代码
    -   在 JSX 中，如果要为元素添加 class 属性了，必须写成 className , 避免与 ES6 中的 class 冲突
    -   label标签的 for 属性需要替换为 htmlFor
    -   在 JSX 创建 DOM 的时候，所有的节点，必须用**唯一**的根元素进行包裹
    -   注释必须放到 {} 内部 => `{/* 注释 */}`

    ```js
    // 综合事例
    const arr = []
      for (let i = 0; i < 10; i++) {
        const p = <p key={i}>this.is.p</p>
        arr.push(p)
      }
      const title = 'this.is.variable'
      const div = (
        <div className="zf" id="zf" title={title}>
          this.is.div
          {arr}
          {/* 注释 */}
        </div>
      )
    ReactDOM.render(div, document.getElementById('app'))
    ```

5.  创建组件：

    -   在 react 中，构造函数就是一个组件。
    -   如果想要把组件放到页面中，只需把 构造函数的名称 当做 组件名称，以 HTML 标签形式引入页面中即可。
    -   构造函数首字母必须大写，否则会按普通 HTML 标签渲染

    ```js
    function MyDiv() {
      return (
        <div>
          <h1>this.is.component</h1>
        </div>
      )
    }
    ReactDOM.render(
      <div>
        <MyDiv></MyDiv>
      </div>,
      document.getElementById('app')
    )
    ```

6.  组件传值：

    -   父组件向子组件传递数据

        -   传值：

            -   非对象的值的传递：使用属性向子组件传值
            -   对象的传递：...obj 使用 es6 中的属性扩散, 即:简化属性的方式的操作

        -   获取：
            -   非对象的值，直接通过属性名获取
            -   对象：通过向构造函数传递形参（props）,通过 props 接收
                -   通过 props 获取的值是只读的,不能重新赋值

    ```js
    const username = 'z...f'
    const person = {
      age: 30,
      name: 'zf',
      address: 'anhui'
    }
    function MyDiv(props) {
      return (
        <div>
          <h1>
            this.is.component
            {username}
            {props.name}
            {props.address}
          </h1>
        </div>
      )
    }
    ReactDOM.render(
      <div>
        <MyDiv {...person}></MyDiv>
      </div>,
      document.getElementById('app')
    )
    ```
