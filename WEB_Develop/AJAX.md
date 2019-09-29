## JAVASCRIPT与服务端进行交互

``` js

var xhr = new XMLHttpRequest();

xhr.open('GET','http://answer05.zf/time.php');	// 设置请求行

xhr.setRequestHeader('Foo', 'Bar');				// 设置请求头

// POST请求必须设置
// xhr.setRequestHeader('Contetn-Type', 'application/x-www-from-urlencord'); 
xhr.send(null);

// 一般不建议用on 注册事件容易出现覆盖
// xhr.onreadystatechange = function(){
xhr.addEventListener('readystatechange', function() {
	if (this.readyState !== 4) return;
    var data = JSON.parse(this.responseText)
	// console.log(this.responseText)             	获取响应体内容
	// console.log(this.getAllResponseHeaders());	获取响应头内容	
});

```



## AJAX



### AJAX_Basic

```js

$.ajax({
    url: '/php/test.php',
    type: 'post',
    data: { id: 1, name: '小明' },  // 传参
    dataType: 'json',    		   // 设置服务器返回的数据类型
    success: function(res) {
        console.log(res)
    }
});

$.ajax({
	url: '/php/test.php',
	type: 'get',
	// data: { 'id': 666666, 'name': 'shangjing'},
	// dataType: 'json',		
	beforeSend: function(xhr){
		console.log(xhr)
	},
	// 请求成功
	success: function(res){
		console.log(res)
	},
	// 请求失败
	error: function(xhr){
		console.log(xhr)
	},
	// 请求完成（ include（ success & error ））
	complete: function(xhr){
		console.log(xhr)
	}
})
```



### AJAX_Advance

```js

// 快捷方法
$.get( url [, data ] [, success(data, textStatus, jqXHR) ] [, dataType ] )

$.post()

$.getJSON()

// 全局 Ajax 事件处理器
$(document).ajaxStart(function(){   
})
$(document).ajaxStop(function(){
})

```



#### Example

```html
<!-- 前提载入 -->
<link rel="stylesheet" type="text/css" href="/css/nprogress.css">
<script src="/js/nprogress.js"></script>
<!-- 独立作用域确保页面加载完成执行 -->
<script>
	$(function($){       
	  // 全局事件处理函数
	  $(document)
	    .ajaxStart(function(){
	      NProgress.start()
	    })
	    .ajaxStop(function(){
	      NProgress.done()        
	  })
	  // 局部页面响应以及渲染
	  $('.list-group-item').on('click', function() {
	      var href = $(this).attr('href')
	      $('#main').load(href + ' #main > *')
	      return false
	  });      
	})
</script>
```



## JSONP（跨域）



### JSONP 跨域请求底层源码

```js

## 客户端

//JSONP 封装
function jsonp (url, params, callback) {
  var funcName = 'jsonp_' + Date.now() + Math.random().toString().substr(2, 5)

  if (typeof params === 'object') {
    var tempArr = []
    for (var key in params) {
      var value = params[key]
      tempArr.push(key + '=' + value)
    }
    params = tempArr.join('&')
  }

  var script = document.createElement('script')
  script.src = url + '?' + params + '&callback=' + funcName
  document.body.appendChild(script)

  window[funcName] = function (data) {
    callback(data)

    delete window[funcName]
    document.body.removeChild(script)
  }
}

```

```php

## 服务端

$conn = mysqli_connect('localhost', 'root', '123456', 'demo');

$query = mysqli_query($conn, 'select * from users');

while ($row = mysqli_fetch_assoc($query)) {
  $data[] = $row;
}

if (empty($_GET['callback'])) {
  header('Content-Type: application/json');
  echo json_encode($data);
  exit();
}

// 如果客户端采用的是 script 标记对我发送的请求
// 一定要返回一段 JavaScript
header('Content-Type: application/javascript');
$result = json_encode($data);

$callback_name = $_GET['callback'];
echo "typeof {$callback_name} === 'function' && {$callback_name}({$result})";

```



### AJAX发送JSONP请求

```js

$.ajax({
  url: 'http://localhost/jsonp/server.php',
  dataType: 'jsonp',
  success: function (res) {
    console.log(res)
  }
})

// 即 dataType 参数设置为 jsonp 即可
// 只能发GET请求
```



### 服务端解决跨域问题

```php

## 服务端加响应头即可 （存在兼容问题）
header('Access-Control-Allow-Origin: *');   // * 通配所有源 也可以指定源 加网址即可

```



## HTTP 补充 -----

请求报文当中的请求头的Content-Type应该跟随着请求体的格式的变化而变化

ajax中response 和responseText

	区别
	
		response     	获取的结果会根据 this.responseType的变化而变化
		responseText    永远获取的是字符串的响应体

