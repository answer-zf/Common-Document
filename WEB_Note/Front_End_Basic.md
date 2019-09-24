# JAVASCRIPT



## return    break    continue	

```js

return    break    continue					  
 
return      直接跳出函数       				程度最大    不执行后续

break       直接跳出循环						程度一般    不执行后续
											(若有循环嵌套，只能跳出一层，需要逐层break)      															 
continue    终止单次循环，不能跳出循环   		程度最小    执行后续循环
```



## 逻辑运算符优先级

```js
	!  >  &&   >   ||
```



## 模板字符串

```js

// 支持解析变量 、 支持换行

``		
ep      str=`a
		   	b`

```



## 正则

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

// Example:
$('.avatar').fadeOut(function() {
  $(this).on('load', function () {
    $(this).fadeIn()
  }).attr('src', res)
})

// img的onload事件指的是图片完全加载完以后执行 （异步操作）先注册后设置 src

```



## JSON

```js

es5中有JSON对象（内置对象）

	JSON.parse(str)    		==>  将json字符串转为数组
		
	JSON.stringify(arr)		==>  将数组转换为json格式的字符串

```



# HTML



## 显示代码原有格式

```html
<pre></pre>
```



## 标签

```
link标签

	真正定义： 链入一个文档，通过rel 属性申明链入的文档与当前文档之间的关系

script标签

	1. innerHTML 永远不会显示在界面上
	2. 如果type 不等于 text/javascript 的话，内部的内容不会作为 Javascript执行
	
```

