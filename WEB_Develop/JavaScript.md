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



## DOM



> 
>
> DOM 会将html元素进行封装，而且会抽象出来做一些额外功能
>
> 



#### attr   or   prop

```js

attr 获取的是html元素上的属性（即实际写在元素上的属性---elements所监视到的属性）

prop 获取的是DOM属性（获取的是DOM抽象出来的属性值，与attr的值部分有区别）

prop('search','?id=' + check_id)  //search的值是 href值中的 包含？之后的数据

```



#### DOM 操作

```js

document.createElement('str')  // 创建标签 str标签名 

document.body.appendChild('')  // 在目标元素中添加子元素

document.body.removeChild('')  // 在目标元素中删除子元素

```



#### 访问自定义属性 data-...

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

