# 使用 VMware 安装 Linux

## VMware 安装重点：

-   稍后安装操作系统
-   点选将虚拟磁盘存储为单个文件(O)
-   点击“编辑虚拟机设置”
    -   点选“使用ISO映像文件(M)”，并添加 iso 镜像
-   VM Ware 网络配置
    1.  网络适配器：桥接模式
    2.  编辑 => 虚拟网络编辑器 => 更改设置 => Vmnet0 桥接到：自动
    3.  虚拟机 => 设置 => 勾选 启动时连接 和 复制物理网络连接状态
-   使用 VM Ware 虚拟机，安装 Ubuntu 系统，（切换中英文输入法 win + space）

## Linux7 安装

-   配置时区 (DATE & TIME)
    -   时区设置为 Region：Asia    City：Shanghai
    -   Network Time ：
-   设置软件选择 (SOFTWARE SELECTION)
    -   选择：Minimal install or Gnome Desktop
-   设置安装位置 (INSTALLATION DESTINATION)
    -   I will configuire parttioning => down
    -   添加 /boot 分区 => 存放启动文件，例如内核kernel
    -   添加 swap 分区 => 交换分区，虚拟内存，当内存耗尽时，把硬盘当内存用(8G/16G)
    -   最后 添加 根分区(`\`, 不填大小即剩余空间都给根)
-   KDUMP: 关闭
-   NETWORK & HOSTNAME:
    -   配置：常规第一个选项勾选
