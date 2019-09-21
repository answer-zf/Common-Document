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



## 标签

```

link标签

	真正定义： 链入一个文档，通过rel 属性申明链入的文档与当前文档之间的关系

script标签

	1. innerHTML 永远不会显示在界面上
	2. 如果type 不等于 text/javascript 的话，内部的内容不会作为 Javascript执行
	
```


## 模板字符串

```js

// 支持解析变量 、 支持换行

``		
ep      str=`a
		   	b`

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

