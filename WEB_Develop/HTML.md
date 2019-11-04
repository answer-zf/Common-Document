

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



## 自定义radio CheckBox  file...

```html

<style>
	#checkbox{
		display:none;
	}
	i::after{
		content:'☆';
	}
	#checkbox:checked+i::after{
		content:'★';
	}
</style>
<body>
	<label>
		<input type="checkbox" name="checkbox" id="checkbox">
		<i style="font-size: normal"></i>		
	</label>
</body>
```



## 兄弟选择器的灵活运用

### 以及display:inline-block 出现空格的问题解决

```html

<style>
	ul{
		list-style: none;
		font-size: 0;
	}
	ul li{
		display:inline-block;
		font-size: 14px;
	}
	ul > li + li:before{
		content:'|';
	}
</style>
<body>
	<ul>
		<li>item</li>
		<li>item</li>
		<li>item</li>
		<li>item</li>
		<li>item</li>
		<li>item</li>
		<li>item</li>
		<li>item</li>
		<li>item</li>
		<li>item</li>
	</ul>
</body>

```



