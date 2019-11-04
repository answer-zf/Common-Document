# AJAX



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



### AJAX 异步上传文件

```js

## 客户端操作

$('#avatar').on('change',function(){

   $this = $(this)

   var files = $this.prop('files')

   if(!files.length) return

   var file = files[0]

   // h5新增的 专门配合ajax操作，用于客户端服务端间传递二进制数据
   var data = new FormData()

   data.append('avatar', file)

   var xhr = new XMLHttpRequest()

   xhr.open('POST','/admin/api/upload.php')

   xhr.send(data) // 借助 formdata 传递文件

   xhr.onload = function(){
     $this.siblings('img').attr('src',this.responseText)
     $this.siblings('input').val(this.responseText) // 界面添加隐藏域提交文件
   }
})

```

```php

## 服务端  

if(empty($_FILES['avatar'])){
	exit();
}
$avatar = $_FILES['avatar'];
if($avatar['error'] !== UPLOAD_ERR_OK){
	exit();
}
$ext = pathinfo($avatar['name'], PATHINFO_EXTENSION);
$target = '../../static/uploads/img-' . uniqid() . '.' . $ext;
if( !move_uploaded_file($avatar['tmp_name'], $target)){
	exit();
}
echo substr($target,5);

```



### AJAX Template



#### artTemplate

- 创建 type =  type="text/x-art-template" 的script 标签 建立模板
- 使用代码引入模板引擎：var html = template('script 标签 id', {对象})

```html

<script type="text/x-art-template" id="tmpl">

	{{each comments}}

	<tr>
		<td>{{$value.author}}</td>
		<td>{{$value.content}}</td>
		<td>{{$value.created}}</td>
	</tr>
	
	{{/each}}

</script>

<script src="js/art-template.js"></script>

<script>
	
	xhr = new XMLHttpRequest()

	xhr.open('GET', '/php/text.php')

	xhr.send()

	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')

	xhr.onreadystatechange = function(){

		if(this.readyState !== 4) return
		var json = JSON.parse(this.responseText)
		var con = {comments: json.data}	  	//----------
		var html = template('tmpl', con)	//----------
		// console.log(html)
		var table = document.getElementById('table');
		table.innerHTML = html
		
	}

</script>

```



#### jsrender

```html

<script src="/static/assets/vendors/jsrender/jsrender.min.js"></script>
<script id="comments_tmpl" type="text/x-jsrender">
 {{for comments}}
  <tr{{if status === 'approved'}} class="warning"{{else status === 'rejected'}} class="danger"{{/if}}>
   <td class="text-center"><input type="checkbox"></td>
   <td>{{:author}}</td>
   <td>{{:content}}</td>
   <td>《{{:title_name}}》</td>
   <td>{{:created}}</td>
   <td>{{if status === 'approved'}}批准{{else status === 'rejected'}}未批准{{else status === 'held'}}待审批{{/if}}</td>
   <td class="text-center">
    {{if status === 'held'}}
     <a href="post-add.html" class="btn btn-info btn-xs">批准</a>
     <a href="post-add.html" class="btn btn-warning btn-xs">驳回</a>
    {{/if}}
     <a href="javascript:;" class="btn btn-danger btn-xs">删除</a>
    </td>
   </tr>
 {{/for}}
</script>
<script>
 $.get('/admin/api/comments_select.php',function(res){
   var html = $('#comments_tmpl').render({ comments: res})
   $('#comments_tbody').html(html)
 })    
</script>

```



### AJAX动态添加文件的事件绑定

```js

// 利用冒泡，在父元素上绑定点击事件，判断子元素是否点击来判断事件
$('#comments_tbody').on('click','.btn-delete',function(){
  console.log(11);
})
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







