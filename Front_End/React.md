# React

## 移动 App 开发环境配置

### 安装 Java jdk 1.8 (开发网站，客户端的环境)

**配置环境变量**

- 新建系统环境变量 `JAVA_HOME` , 值为：`C:\Program Files\Java\jdk1.8.0_121` (jdk 的根目录)

- 修改系统环境变量 `Path` , 新增：`%JAVA_HOME%\bin` 、 `%JAVA_HOME%\jre\bin`

- 新建系统环境变量 `CLASSPATH` , 值为：`.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;`

- 验证：命令行中输入 `javac`

### 安装 Node.js

### 安装 C++

### 安装 Git

### 安装 Python 2.7

> 注意勾选安装界面上的 Add Python to path , 验证：命令行中输入 `python`

### 配置安卓环境

1. 安装 SDK

   - 勾选：`Install for anyone using this computer`

   - 修改路径 `C:\Android`

2. 打开 `C:\Android\platforms` ，将 `android-23`(react-native 依赖) 、 `android-24` 、 `android-25` 解压后，放到该文件夹下

3. 打开 `C:\Android` , 将 `platform-tools` 解压后，放到该文件夹下

4. 配置 `build-tools`

   - 打开 `C:\Android` , 新建 `build-tools` 文件夹
   - 将
     - `build-tools_r23.0.1-windows.zip` (react-native 依赖) ,
     - `build-tools_r23.0.2-windows.zip` (weex 依赖) ,
     - `build-tools_r23.0.3-windows.zip` 分别解压后，
   - 分别改名为 `23.0.1` , `23.0.2` , `23.0.3` , 放到该文件夹下

5. 打开 `C:\Android` , 新建 `extras` 文件夹，在 `extras` 文件夹下新建 `android` 文件夹；解压 `m2responsitory` 文件夹和 `support` 文件夹，放到新建的 `C:\Android\platforms\extras\android` 下

6. 配置环境变量

   - 新建系统环境变量 `ANDROID_HOME` , 值为：`C:\Android` (SDK 的根目录)

   - 修改系统环境变量 `Path` , 新增：`%ANDROID_HOME%\tools` 、 `%ANDROID_HOME%\platform-tools`
