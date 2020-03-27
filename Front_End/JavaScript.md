# JavaScript



## JS_Basic



### return    break    continue	

```js
return    break    continue					  
 
return      直接跳出函数       				程度最大    不执行后续

break       直接跳出循环						程度一般    不执行后续
											(若有循环嵌套，只能跳出一层，需要逐层break)      															 
continue    终止单次循环，不能跳出循环   		程度最小    执行后续循环
```



### 逻辑运算符优先级

```js
	!  >  &&   >   ||
```

#### 逻辑运算符说明：

​			  || 或的关系，如果前面的值等于false就会自动执行第二个值

​              && 且的关系，如果前面的值等于true就会自动执行第二个值

### 模板字符串（H5新增）

```js
// 支持解析变量 、 支持换行
// 可以用${}的方式引用变量

``		
ep      str=`a
		   	b`

`name=${name}&password=${password}`    // 模板字符串拼接变量

```



### 正则

```js
// 创建正则
var rec = /^[a-zA-Z]@\.$/		// //间书写正则

// 正则验证
rec.test('str')   				// 找到返回 boolean
rec.exec('str')					// 提取组 
								// 找到返回 数组 数组第一个成员是完整匹配值
								// 			   数组第二个成员是正则括号内容匹配值
								//             以此类推
								// 未找到返回null

```



## 常用API

```js

String.replace()  // 第一个参数，除了可写一个 字符串之外，还可以定义一个正则
array.indexOf()  
// 检索：某个指定的字符串值在str中首次出现的位置，找不到返回-1
// 第一个参数是指定的字符串 ，第二个参数是开始查找的位置（其默认值为0）
// es5 新增includes()

array.splice()
// 通过删除或替换现有元素或者原地添加新的元素来修改数组,并以数组形式返回   修改原数组
// 第一个参数 指定修改的开始位置（数组索引值） 第二个参数表示要移除的数组元素的个数

typeof operand
// operand 一个表示对象或原始值的表达式
// 返回 其类型 

toString() 
// 返回一个表示该对象的字符串
// 字符串拼接有其他类型数据默认用toString转义字符串
// 数组的toString方法   
// 返回：字符串：数组的元素用，拼接
// object的toString方法
// 返回：[object Object]

eval(String)
// 将传入的字符串当做 JavaScript 代码进行执行

some()
Array.some((item, i) => {
  if (item.id == id) {
    // 在 数组的 some 方法中，如果 return true，就会立即终止这个数组的后续循环
    return true;
  }
}) 

split()
Array.split('') // 一个字符串分割成字符串数组（以'',即每一个字符串为数组的每一项），与join()相反

reverse()
Array.reverse() // 用于颠倒数组中元素的顺序

charAt(0) // 返回指定位置的字符
```



## JQuery



### 入口函数

```js

// 入口函数 （jq ready()的简写）
$(function($){
	// 作用
	// 1. 单独作用域
	// 2. 确保页面加载过后执行   
})

// 即等价于（ jQuery的默认参数是：“document” ）
$().ready(function(){
	//do something
})

// 文档结构加载完成（不包含图片等非文字媒体文件）后，对DOM进行操作 
// 即 ：在“加载js和css”和“加载图片等其他信息”之间，就可以操作Dom

// 一个页面响应加载的顺序是：域名解析-加载html-加载js和css-加载图片等其他信息。
// onload    : 页面包含图片等文件在内的所有元素都加载完成。

```



### 动画相关

```js

// fadeIn() / fadeOut()有function（）参数
// 指的是在动画完成时执行的函数。
// fadeIn() / fadeOut 先检测样式，所以可以先设置display：flex属性，行内隐藏。 

// Example:
$('.avatar').fadeOut(function() {
  $(this).on('load', function () {
    $(this).fadeIn()
  }).attr('src', res)
})

// img的onload事件指的是图片完全加载完以后执行 （异步操作）先注册后设置 src

```

### contains

`$( ":contains(text)" )`

 **text:** 用来查找的一个文本字符串。这是区分大小写的。 

```html
<div>John Resig</div>
<div>George Martin</div>
<div>Malcom John Sinclair</div>
<div>J. Ohn</div>
<script>
  $("div:contains('John')").css("text-decoration", "underline")
</script>
```



## each or Foreach

### jQuery中的each

- $.each(数组, function)

- $('div').each(function) 一般用于遍历 jQuery 选择器选择到的伪数组实例对象

- 同时也是低版本浏览器中 forEach的替代品

- 但jQuery的实例对象不能用forEach方法，如果想要使用要转为数组

  `;[].slice.call($('div')).forEach(function (item) {console.log(item)})`

###  EcmaScript 5中的forEach

- forEach 是 EcmaScript 5 中的一个数组遍历函数，是 JavaScript 原生支持的遍历方法 可以遍历任何可以被遍历的成员
- jQuery 的 each 方法和 forEach 几乎一致
- 由于 forEach 是 EcmaScript 5 中的，故不兼容 **IE8**

```javascript

// IE 8 不支持
;['abc', 'd', 'efg'].forEach(function (item, index) {
  console.log(item)
})

// 遍历 jQuery 元素
$.each(['abc', 'd', 'efg'], function (index, item) {
  console.log(item)
})

// $('#id') => 伪数组  是对象
// 对象的原型链中没有 forEach
// 对象的原型链是 Object.prototype
// 这个 each 是 jQuery 提供的
// 这个 each 在 jQuery 的原型链中
// $('div').each(function (index, item) {
//   console.log(item)
// })

// jQuery 不是专门用来遍历 jQuery 元素的
// 1. 方便的遍历 jQuery 元素
// 2. 可以在不兼容 forEach 的低版本浏览器中使用 jQuery 的 each 方法

 ;[].slice.call($('div')).forEach(function (item) {console.log(item)})

```

```js
Array.prototype.mySlice = function () {
  var start = 0
  var end = this.length
  if (arguments.length === 1) {
    start = arguments[0]
  } else if (arguments.length === 2) {
    start = arguments[0]
    end = arguments[1]
  }
  var tmp = []
  for (var i = start; i < end; i++) {
    tmp.push(this[i])
  }
  return tmp
}

var fakeArr = {
  0: 'abc',
  1: 'efg',
  2: 'haha',
  length: 3
}

// 所以你就得到了真正的数组。 
[].mySlice.call(fakeArr)
```



## 网页中的跳转方式：

1. 使用 `a` 标签的形式进行跳转 --- **标签跳转**
2. 使用 `window.location.href` 的形式跳转 --- **编程式导航**

## DOM



> DOM 会将html元素进行封装，而且会抽象出来做一些额外功能
>



### attr   or   prop

```js

attr 获取的是html元素上的属性（即实际写在元素上的属性---elements所监视到的属性）

prop 获取的是DOM属性（获取的是DOM抽象出来的属性值，与attr的值部分有区别）

prop('search','?id=' + check_id)  //search的值是 href值中的 包含？之后的数据

```



### DOM 操作

```js

document.createElement('str')  // 创建标签 str标签名 

document.body.appendChild('')  // 在目标元素中添加子元素

document.body.removeChild('')  // 在目标元素中删除子元素

```



### 访问自定义属性 data-...

```js

.dataset['id']		 // DOM
.attr('data-id')     // jQuery
.data('id')		     // jQuery

```



## JSON

```js
es5中有JSON对象（内置对象）

	JSON.parse(str)    		==>  将json字符串转为数组
		
	JSON.stringify(arr)		==>  将数组转换为json格式的字符串

```



## JavaScript 模块化

+ PHP 中为什么就可以直接 `require`、`include` 因为 PHP 当初在设计的时候就加入了这个功能
+ PHP 这门语言天生就支持
+ 模块作用域
+ 可以使用 API 来进行文件与文件之间的依赖加载
+ 在 Node 这个环境中对 JavaScript 进行了特殊的模块化支持 CommonJS
+ JavaScript 天生不支持模块化
  * require
  * exports
  * Node.js 才有的
+ 在浏览器中也可以像在 Node 中的模块一样来进行编程
  * `<script>` 标签来引用加载，而且你还必须考虑加载的顺序问题
  * require.js 第三方库 AMD
  * sea.js     第三方库 CMD
+ 无论是 CommonJS、AMD、CMD、UMD、EcmaScript 6 Modules 官方规范
  * 都是为了解决 JavaScript 的模块化问题
  * CommonJS、AMD、CMD 都是民间搞出来的
  * EcmaScript 是官方规范定义
  * 官方看民间都在乱搞，开发人员为了在不同的环境使用不同的 JavaScript 模块化解决方案
  * 所以 EcmaScript 在 2015 年发布了 EcmaScript 2016 官方标准
  * 其中就包含了官方对 JavaScript 模块化的支持
  * 也就是说语言天生就支持了
  * 但是虽然标准已经发布了，但是很多 JavaScript 运行换将还不支持
  * Node 也是只在 8.5 版本之后才对 EcmaScript 6 module 进行了支持
  * 后面学 Vue 的时候会去学习
  * less 编译器 > css
  * EcmaScript 6 -> 编译器 -> EcmaScript 5
  * 目前的前端情况都是使用很多新技术，然后利用编译器工具打包可以在低版本浏览器运行。
  * 使用新技术的目的就是为了提高效率，增加可维护性