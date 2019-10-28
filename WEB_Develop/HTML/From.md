# FORM 额外属性

```js

// 取消h5自动校验功能（form属性）因为浏览器自带的校验功能不友好而且与界面不兼容

novalidate

// 表单自动完成功能开启与禁止

autocomplete
		
	value:

		on(default)  
		off
        
// 文件域设置
   
	method='post'
	enctype='multipart/form-data'

```



## 文字颜色

```css
input::-webkit-input-placeholder {
  color: #182f62;
}
input::-moz-placeholder {
  color: #182f62;
}
input:-moz-placeholder {
  color: #182f62;
}
input:-ms-input-placeholder {
  color: #182f62;
}
```



## INPUT 额外属性

```js
	
// 页面加载即获取焦点

autofocus

// text属性带有file的标签的限制文件属性						

accept

					// 有两种值   1、 MIME Type     ex : audio/* ;

					//		    2、 文件扩展名	  ex : .lrc ;

// 让一个文件域多选。

multiple

```



# 表单提交



## CHECKBOX    


	默认提交   			‘on’;
	
	设置value提交 		value属性；
	
	多选提交的话是在name属性后加[]
	
		==>   name="funs[]"




## RADIO


	将多个radio的name属性设置成相同的  形成相同的组
	
	将value设置成不同的，在服务端辨别选则的是哪个




## SELECT


	如果option有value提交value 如果没value  提交innerhtml、innertext

