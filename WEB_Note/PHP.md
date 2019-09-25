

# PHP操作数据库

## curd

```php

// 查询（读取[r]）

function zf_fetch_all($sql){

	$connect = mysqli_connect('host','username','password','DB_name');

	if (!$connect) exit('<h1>数据库连接失败</h1>');

	$query = mysqli_query($connect, $sql); // 结果集
	if (!$query){		
		return false;
	}

	while ($row = mysqli_fetch_assoc($query)) {
		$data[] = $row;
	}

	mysqli_free_result($query);
	mysqli_close($connect);

	return $data;
}

// 增 删 改 (create delete update)
	mysqli_affected_rows()     // 查询 XX链接最后一次的受影响行数
        
        

```

## SQL 注入

```php

## 在浏览器输入框输入http://../../xxx.php?id=1or1=1;
## 执行的是删除php页面 被用户恶意传参即执行
delete from categories where id = 1 or 1 = 1
## 清空数据库

## 解决方法
## 对传参进行强转   
$id = (int)$_GET['id'];

```





# 重点笔记



## PHP 传参区别

```php

PHP  -  API   			// 如需要传地址参数，必须是绝对路径 or 物理路径  （require、include）
						// 只有html有相对路径一说（a,link,script,img...）
    
```



## 随笔

```php
 
function_exists('count')// 判断函数知否被定义 typeof fn === 'function'
    
0     					// UPLOAD_ERR_OK

@						// 如果需要在调用函数时忽略错误或者警告可以在函数名前加上 @

(int)$str    			// 数字字符串 强行转 数字

implode(",", $array)	// 数组转字符串

dirname(__FILE__)		// 获取文件路径
    
```



# PHP _ API

## 时间API

```php

date('Y-m-d H:i:s', time());

	// 对已有时间做格式化

		$str = '2017-10-22 15:18:58';

		strtotime // 可以用来将一个有格式的时间字符串 转换为一个 时间戳

		$timestamp = strtotime($str);

					// 注意单引号字符串问题

		echo date('Y年m月d日<b\r>H:i:s', $timestamp);

```



## 非空判断API

```php

isset();
		
	// 判断变量是否存在		
	// 也可判断数组中是否有指定的键
	isset($array['key']);
	isset 会吞掉 Undefined index 的警告

empty();
		
	// 检查一个变量是否为空
	empty($array['key']) 相当于 !isset($array['key']) || $array['key'] == false


		// 底层代码：empty 的实现

			function empty ($input) {
			  return !isset($input) || $input == false
			}

```



## 载入脚本API

```php

require 'url';
	
	// 可以用于在当前脚本中载入一个别的脚本文件并且执行他
	// 在每一次调用时都会载入对应的文件

require_once 'url';

	// 如果之前载入过，不再执行（只执行一次）
	// 类似于 定义常量 定义函数 一般用	require_once载入
		
----------------------------

require 'url';
require_once 'url';

// 特点：
	// 一旦被载入的文件不存在就会报一个致命错误，当前文件不再往下执行 （适合：引用配置，预定义函数）

include 'url';
include_once 'url';

// 特点：
	// 载入文件不存在不会报错误（会有警告，警告不用管），当前文件继续执行（适合：部分html）

```

