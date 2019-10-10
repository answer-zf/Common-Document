# Node_Advance



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

语法：

```js
var custom = require('module')
```

作用：

1. 执行被加载模块中代码
2. 得到被加载模块中的  `exports`  导出接口对象

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

