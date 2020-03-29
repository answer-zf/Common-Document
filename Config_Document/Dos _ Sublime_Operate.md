## Dos 常用命令

### CMD 操作类

```shell

# 切盘
$ D:

# 删除文件
$ del

# 退出dos
$ exit

# 清空命令行
$ cls

# &&   同时执行两个操作 用 && 衔接
```

### 目录操作类

```shell

#显示目录
$ dir   ## 详细

#创建目录
$ md 目录名

#删除目录
$ rd 目录名
$ rd /s/q 目录名   ## 强制删除文件文件夹和文件夹内所有文件

#进入指定目录
$ cd 目录名

#树形图显示目录结构
$ tree

```

### 文件操作类

```shell

# 重名名文件
$ ren

######	进阶操作  ==>  批量重命名(指定字符串替换)
$ ren *.html *.php

# 替换文件
$ replace

# 删除文件
$ replace
$ del 文件名

# 创建文件
$ echo on > a.txt



# 向文件添加内容 （覆盖）
$ echo 内容 > a.txt

# 向文件添加内容 （向后追加）
$ echo 追加 >> a.txt

```

### 服务操作类

```shell

# 查询服务
$ sc query MySQL

# 启动服务
$ net start MySQL

# 停止服务
$ net stop MySQL

# 删除服务
$ sc delete MySQL

# 查询端口情况
$ netstat -ano

```

## Linux

Git Bash / Cmder 可以模拟 Linux 环境，在 Windows 操作

```bash

# 清屏
clear

# 显示文件夹列表 （显示不隐藏的文件与文件夹）
ls
ls -a  # (显示当前目录下的所有文件及文件夹包括隐藏的.和..等)

# 显示工作目录
pwd

# 删除一个文件或者目录
rm 文件名
# 删除非空目录，以及一些比较顽固的文件或者目录
rm -rf 目录名

# 创建目录
touch 文件名

# 查看文件（完整输出）
cat 文件名
# 向文件添加内容 （覆盖）
cat > a.txt （回车后 添加内容）
# 向文件添加内容 （向后追加）
cat >> a.txt （回车后 添加内容）

# 查看文件（分页输出）-- 适用于查看大文本文件
less 文件名 		# b 向上翻一页    空格 向下翻一页    鼠标滚轮翻页

# visual interface 编辑文本
vi 文件名		# 进去vi编辑模式
Esc         # 退出到命令模式
i 					# 进入插入模式
:q 					# 退出vi
:w 					# 保存编辑
:wq 				# 保存并退出
:q! 				# 强制退出不保存修改

```

## Window

```shell

sysdm.cpl  cmd 开启服务

# 强制删除  =>  SHFIT + delete

# 显示桌面			==>   win + D

# 最小化所有窗口	  ==>   win + M

# 最小化除当前窗口以外所有窗口	==>   win + HOME

# 打开资源管理器	  ==>   win + E

# 打开设置	        ==>   win + I

# 截图			 ==>   win + PrintScreen

# 放大缩小视口	  ==>   WIN + +/-

# 切换输入法    	   ==>   WIN + space

# 自定义截图		   ==>   WIN + SHFIT +S
```

```
win + Ctrl + D       新建桌面
win + Ctrl + 方向键   切换桌面
win + tab						 列表
```

## Sublime

```shell
# 命令行 用 sublime 打开当前目录 .表示当前目录
subl .

# 命令行 用 vscode 打开当前目录
code .

# 删除整行  		==>    CTRL + SHIFT + K

# 括号内部选中  	   ==>    CTRL + SHIFT + M

# 直接跳下一行  	   ==>    CTRL + ENTER

# 直接跳上一行  	   ==>    CTRL + SHIFT + ENTER

# 查找选择器		    ==>	   CTRL + R

# 替换同一个目录下所有文件公共部分
# ==>侧边栏目录下子文件右键选项   Find Advanced  >  In Parent Folder

# 打开所在目录		==>    右击文件选  Reveal

```

## Browser

### Chrome

```shell

# console 命令行截图    ==>     Capture node screenshot

```

### 搜索栏技巧

```shell
# 搜索关键词如有空格，可用  ""  包含，视为一个词

# 搜索限定

$ 关键词 + site:cnblogs.com

# 限定在 cnblogs.com 搜索

```

## 右键菜单分栏设置地址

> HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\
