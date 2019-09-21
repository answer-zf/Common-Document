# 设置cookie



## PHP 设置

```php

header('Set-Cookie: foo=bar');   // 只能设置一次cookie，多次会覆盖

setcookie						 // 能多次设置cookie

setcookie('key');				 // 传一个参数是‘删除’， 即将过期时间设置为过去时间；

setcookie('key', 'value');		 // 传两个参数是设置 cookie

setcookie('key', 'value', time() + 1 * 24 *60 *60);

	// 传第三个参数是设置过期时间，若不传递则是会话级别的cookie（关闭浏览器，自动删除）

```




## JAVASCRIPT 设置

``` js

var a = new Date;

a.setYear(2029);

document.cookie = "app-installed=1; expire =" + a.toGMTString();

```



## 打开浏览器 到关闭浏览器之间的过程叫一次会话（session）