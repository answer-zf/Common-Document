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





# PHP CURD实例

## add

```php

function add()
{
    if (empty($_POST['name'])) {
        $GLOBALS['error_message'] = '请输入用户名';
        return;
    }
    if (!(isset($_POST['gender']) && $_POST['gender'] !== '-1')) {
        $GLOBALS['error_message'] = '选择性别';
        return;
    }
    if (empty($_POST['birthday'])) {
        $GLOBALS['error_message'] = '请选择日期';
        return;
    }

   	$name = $_POST['name']; 

   	$gender = $_POST['gender']; 
   	
   	$birthday = $_POST['birthday']; 

    if (empty($_FILES['avatar'])) {
        $GLOBALS['error_message'] = '请选择文件';
        return;
    }

    $address = $_FILES['avatar'];

    //var_dump($address);

    if ($address['error'] !== UPLOAD_ERR_OK){
    	$GLOBALS['error_message'] = '文件上传失败';
        return;
    }

    if($address['size'] > 1 * 1024 *1024){
    	$GLOBALS['error_message'] = '文件上传过大';
        return;
    }
    if(strpos($address['type'],'image/') !== 0){
    	$GLOBALS['error_message'] = '文件格式不符';
        return;
    };
    $suffix = '../upload/avatar-' . uniqid() . '.' . pathinfo($address['name'], PATHINFO_EXTENSION);
    if(!move_uploaded_file($address['tmp_name'],$suffix)){
    	$GLOBALS['error_message'] = '文件上传失败';
        return;
    };
    
    $avatar = substr($suffix, 2);

    $conn = mysqli_connect('127.0.0.1', 'root' ,'123456' ,'test');
    if (!$conn) {
    	$GLOBALS['error_message'] = '服务器连接失败';
        return;
    }
    
  	$query = mysqli_query($conn, "insert into users values (null, '{$name}', {$gender}, '{$birthday}', '{$avatar}');");
    var_dump($query);
    if (!$query) {
    	$GLOBALS['error_message'] = '数据查询失败';
        return;
    }

    if(mysqli_affected_rows($conn) !== 1){
    	$GLOBALS['error_message'] = '添加信息失败';
        return;
    }

	header('Location: index.php');

}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    add();
}

```

## delete

```php

if (empty($_GET["id"])) {
    exit('<h1>必须传入指定参数</h1>');
}

$conn = mysqli_connect('127.0.0.1', 'root', '123456', 'test');

if (!$conn) {
    exit('<h1>连接数据库失败</h1>');
}

$query = mysqli_query($conn, 'delete from users where id = ' . $_GET["id"] . ';');

if (!$query) {
    exit('<h1>查询数据失败</h1>');
}

$affect = mysqli_affected_rows($conn);

if ($affect <= 0) {
    exit('<h1>删除失败</h1>');
}

header('Location: index.php');

```



## edit

```php

if (empty($_GET['id'])) {
    exit('<h1>必须传入指定参数</h1>');
}
$id   = $_GET['id'];
$conn = mysqli_connect('127.0.0.1', 'root', '123456', 'test');

if (!$conn) {
    exit('<h1>数据库连接失败</h1>');
}

$query = mysqli_query($conn, "select * from users where id = {$id} limit 1;");

if (!$query) {
    exit('<h1>数据查询失败</h1>');
}

$base = mysqli_fetch_assoc($query);

if (!$base) {
    exit('<h1>查询数据失败</h1>');
}

function edit()
{

    if (empty($_POST['name'])) {
        $GLOBALS['error_message'] = "请输入姓名";
        return;
    }
    if (empty($_POST['birthday'])) {
        $GLOBALS['error_message'] = "请选择生日";
        return;
    }
    if (!(isset($_POST['gender']) && $_POST['gender'] !== '-1')) {
        $GLOBALS['error_message'] = "请输入姓名";
        return;
    }

    global $base;

    $base['name'] = $_POST['name'];

    $base['gender'] = $_POST['gender'];

    $base['birthday'] = $_POST['birthday'];

    $p_id = $_GET['id'];

    if (isset($_FILES['avatar']) && $_FILES['avatar']['error'] === UPLOAD_ERR_OK) {
        $suffix = '../upload/avatar-' . uniqid() . '.' . pathinfo($_FILES['avatar']['name'], PATHINFO_EXTENSION);
        if (!move_uploaded_file($_FILES['avatar']['tmp_name'], $suffix)) {
            $GLOBALS['error_message'] = '文件上传失败';
            return;
        }

        $base['avatar'] = substr($suffix, 2);

    }

    $conn = mysqli_connect('127.0.0.1', 'root', '123456', 'test');
    if (!$conn) {
        $GLOBALS['error_message'] = '服务器连接失败';
        return;
    }

    $query = mysqli_query($conn, "update users set name = '{$base['name']}', gender = {$base['gender']}, birthday = '{$base['birthday']}', avatar = '{$base['avatar']}' where id = {$p_id};");

    if (!$query) {
        $GLOBALS['error_message'] = '数据查询失败';
        return;
    }

    header('Location: index.php');
    
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



## 常用API

```php

// 字符串

strpos($str,'a')
// 查找指定字符串中某些字符首次出现位置     $str:指定字符串   'a': 泛指查找的字符
// 返回：若有返回位置索引，若无返回false
    
// 转数字
(int)$str
intval($str)
    
// 判断是不是数字
is_numeric($str)   // 返回boolean值
    
// 获取文件拓展名
pathinfo(string $path,PATHINFO_EXTENSION)
```



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



# PHP 应用实例

## 日期年龄转换

``` php

$both = strtotime($row['birthday'] . '0:0:0');
$bY = date('Y', $both);
$bm = date('m', $both);
$bd = date('d', $both);
$nm = date('m');
$nd = date('d');
$age = date('Y') - $bY;
if( $bm > $nm || $bm == $nm && $bd > $nd){
	$age--;
}

```

