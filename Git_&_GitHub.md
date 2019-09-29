# Git



## 初始化Git仓库

```shell

## 找到目标文件夹并进入

## 右键  选择 Git Bash Here

$ git init

```



## 配置个人信息

```shell

## 方便每次备份将使用者信息备份起来，方便操作

## 配置用户名
 
$ git config --global user.name "answer-zf"

## 配置邮箱
$ git config --global user.email "feng18255163789@gmail"

```



## 将文件备份到Git仓库中

```shell

## 先存放置暂存区
$ git add ./readme.md

## 再提交到版本库
$ git commit -m "complete the first function！"    ## -m : 说明信息（便于查看）
 
----------------------
 	## 不输入 -m 会进去vim编辑器环境输说明信息。
 	## 在vim里输入说明信息后 Esc键 + :Wp 即可    ## w：保存 p：退出
 	## 强制退出：Esc键 + :p
 	
##**************************************************************************
 	
## 把所有的文件存放到暂存区
$ git add ./	## 当前文件夹所有文件

## 一次性把所有修改后的文件直接放到版本库中
$ git commit --all -m "这是一次性操作"        ## --all : 把所有修改后的文件直接放到版本库中
```



## 查看状态

```shell

$ git status

## Changes not staged for commit
## modified （红色）  =>  文件已修改，但未放入暂存区

## Changes to be committed
## modified （绿色）  =>  文件已经放入暂存区

## nothing to commit, working tree clean  ==> 文件已经在工作区

```



## 查看提交日志

``` shell

## 查看历史日志
$ git log   ## 如果出现显示bug 输入q 即可。

## 查看精简日志，单行显示
$ git log --oneline

## **************************************************
## 查看每次切换版本记录
$ git reflog

```



## 回退指定版本

```shell

## git log 只能显示当前版本以及之前的版本

$ git reset --hard Head~0    ## Head~0   回退到上一次提交代码时的状态
							 ## Head~1   回退到上上一次提交代码时的状态
							 
							 ## hard     允许工作区代码被以前的代码覆盖
							 
## 可以通过版本号精确回退到某一次提交的状态
$ git reset --hard b0750f9   ## b0750f9 ：版本号
```



## 分支（ 默认有一个主分支 master）



### 创建、查看、切换分支

```shell

## 创建分支
$ git branch dev     ## 创建指定分支（dev）
					 ## 在刚刚创建时，dev分支里的文件和master分支里的东西是相同的

## 查看分支
$ git branch		 ## 有*和绿色高亮的部分是当前所处在的分支

## 切换分支
$ git checkout dev

## 删除分支
$ git branch -d dev  ## 删除指定分支（dev）
```



### 合并分支

```shell

## 切换到master分支（主分支）
$ git checkout master

## 将dev分支合并到主分支中
$ git merge dev

			## git merge：把当前分支与指定分支，进行合并

```



### 合并分支冲突

```shell

## 在dev分支提交了代码以后
## 又在主分支master提交了代码
## 合并分支以后，需要手动处理，在提交到主分支中

```



# GitHub



## GitHub上传

### Https上传

```shell

## 格式 git push + url地址 + master    master指的是 将本地master分支提交到服务器master分支
$ git push https://github.com/answerooo3/Common-Document.git master

```

### SSH上传

```shell

## 优势：不需要输入用户名密码，依旧可以进行身份验证 

## 公钥（GitHub存放），私钥（个人存放）
## 生成公钥，私钥
$ ssh-keygen -t rsa -C "feng18255163789@gmail.com"

## 找到C:\Users\answer_zf\.ssh内的
## id_rsa	    私钥
## id_rsa.pub   公钥

## 复制 id_rsa.pub 内代码
## 进去GitHub => 点击我的头像 => Settings => SSh and GPG keys => NEW SSH key
## 添加已复制的代码 起个名字（Title内填写） => Add SSH key
## 再用push上传即可 （传参为SSH地址）

## 换主机：
## 在路径  C:\Users\ + 主机用户名  的目录下找到 .ssh文件
## 在目标主机更换.ssh 文件

```



## GitHub下载

### Pull

```shell

## 开发优先推荐

## 新建文件并初始化 git仓储

## 从服务器下载 git
$ git pull https://github.com/asnwer-zf/Common-Document.git master

```

### Clone

```shell

## 不用初始化git仓储，会在本地新建根文件夹
## 如果多次执行会覆盖本地内容
$ git clone https://github.com/asnwer-zf/Common-Document.git

```



## GitHub多人开发的冲突问题

```shell

## 修改同一个文件的冲突
## 先pull到本地手动修改冲突后 ，再push到GitHub

## 修改不同文件的冲突
## 先pull到本地进入vim填写说明系统自行合并 ，再push到GitHub

```



## Push 与 Pull简化操作

```shell

## 对于经常输入的url地址，可以做类似变量命名的操作简化，但是作用只在本地当前目录
## 类似修改变量的操作用set-url name url
## 不是全局
$ git remote add origin git@github.com:asnwer-zf/Common-Document.git
$ git remote set-url origin https://github.com/asnwer-zf/ProJect_DaMiJun.git
$ git push origin master

## origin 类似变量命名的操作

##*********************************
## -u 参数关联
$ git push origin -u master
## 后面的提交简化：
$ git push
## 仍然提交上去了
## -u：把当前分支与远程的指定分支进行关联，即：记住操作
## 关联以后 git pull 同样可以

## -u 关联在push中进行

```



## GitHub 创建个人站点

```shell

## 访问
https://answer-zf.github.io

## 创建
## 1. 新建仓库   注：用户名必须为  answer-zf.github.io
## 2. 仓库内必须有.html文件

```



## GitHub 创建项目站点

```shell

## 访问
https://answer-zf.github.io

## 创建
## 1. 进入项目主页，点击 settings
## 2. 在settings页面，点击 Launch automatic page generator 来自动生成主题页面
## 3. 新建站点基础信息设置
## 4. 选择主题
## 5. 生成网页

```

