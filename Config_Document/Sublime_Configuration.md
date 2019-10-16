# 插件

``` shell

## 汉化插件
$ Localization

## 格式化代码插件
$ JSFormat							## js  格式化代码    shift+alt+j
$ HTML-CSS-JS Prettify				## html格式化代码	shift+alt+h
$ CodeFormatter						## 通用格式化代码	   shift+alt+f 
			   ---------------------
									## sublime 只支持php5.6-php7.2的php版本
									## 更改配置信息：
									## "php_path": "C:/Develop/php-7.1.31/php.exe",
									
## 侧边栏优化插件
$ SideBarEnhancements				## 具体配置见注释

## 最牛逼的插件：
$ Emmet                             ## 牛逼到不用解释！

## 代码颜色插件：
$ Color Highlighter

## 最棒的注释插件：
$ DocBlockr                         ## 快捷键：/** + enter

## 括号匹配插件：
$ Bracket Highlighter

## 快捷文件名输入插件：
$ AutoFileName

## 等号对其插件：
$ Alignment							## 快捷键：alt+shift+e

## 转码插件：
$ ConvertToUTF8

## 头部注释插件：
$ FILE HEADER                       ## 自定义创建头部注释（详情配置见备注）

## 语法错误检测插件
$ sublimelinter 					## 错误日志视图快捷键： ctrl+k,ctrl+e

$ sublimelinter-php 				## 具体见备注
$ SublimeLinter-jshint
$ SublimeLinter-csslint

## PHP调试插件
$ Xdebug Client

## 主题预览插件
$ colorsublime
```



# 主题

``` shell

## 配色:			Dracula
## 主题:			Materialize

```



# 首选项配置

``` json

## 状态栏编码显示
$ "show_encoding":true

```



## 备注



**SUBLIMELINTER配置** 	==> 	基于node插件

``` shell

------js/css检测	## 安装环境

## 1.安装node.js

## 2.命令行输入 
##   2.1 js  检测
$ npm install -g jshint            ##	SublimeLinter-jshint
$ jshint -v						   ##   命令行输出："jshint v2.10.2"

##   2.2 css 检测
$ npm install -g csslint           ##	SublimeLinter-csslint
$ csslint --version				   ##   命令行输出："v1.0.4"


------php检测  	 ## 配置环境

​```json

    "lint_mode": "save only",

    "paths": {
        "linux": [],
        "osx": [],
        "windows": ["C:/Develop/php"]
    }	
    
```



**FILE HEADER配置** 

```json

## 1.设置配置文件
        
{
    "Default":
   {
       "email": "657829956@qq.com",
       "last_modified_by": "answer-zf",
       "author": "answe-zf"
   }
｝

## 2.自定义注释

## 	2.1找到文件夹

	C:\Users\Administrator\AppData\Roaming\Sublime Text 3\
    Packages\FileHeader\template\header
    
## 	2.2在文件夹里找到需要修改的文件，并修改（以html文件为例）

    <!--
    * @Author: {{author}}
    * @Date:   {{create_time}}
    * @Last Modified by:   {{last_modified_by}}
    * @Last Modified time: {{last_modified_time}}
    * @E-mail: {{email}}
    -->

```



## 快捷键配置

``` json

[
    //格式化快捷键配置
    //--codeformatter快捷键配置
    {
        "keys": ["shift+alt+f"],
        "command": "code_formatter"
    },
    //--htmlprettify快捷键配置
    {
        "keys": ["alt+shift+h"],
        "command": "htmlprettify"
    },
    //--jsFormat快捷键设置
    {
        "keys": ["shift+alt+j"],
        "command": "js_format",
        "context": [{
            "key": "selector",
            "operator": "equal",
            "operand": "source.js,source.json"
        }]
    },
    //chorme 浏览器打开快捷键(浏览器地址需适配本机电脑)    
    {
        "keys": ["f2"],
        "command": "side_bar_files_open_with",
        "args": {
            "paths": [],
            "application": "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",
            "extensions": ".*"
        }
    },
    //SublimeLinter快捷键配置
    //--Lint this view
    {
        "keys": ["ctrl+k", "ctrl+l"],
        "command": "sublime_linter_lint"
    },
    //--Show all errors
    {
        "keys": ["ctrl+k", "ctrl+e"],
        "command": "sublime_linter_panel_toggle"
    },
    //Alignment快捷键配置
    {
        "keys": ["alt+shift+e"],
        "command": "alignment"
    }
]

```



## 设置配置



## 连体字

```json

//连体字符设置
"font_face": "Fira Code"

## 常用编程字体：
-- Consolas
-- Fira Code
-- Source Code Pro
```

