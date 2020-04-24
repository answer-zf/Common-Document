# VS Code

## Setting Sync：远程配置同步插件的 token：

**sync.gist.id：42cafa1971c8eabf28258d9dd154f762**

## 字体：[FiraCode](https://github.com/tonsky/FiraCode)

## vue 代码时使用 eslint

```shell
# 安装
cnpm i eslint
cnpm i eslint-plugin-vue
cnpm i -g eslint
cnpm i -g eslint-plugin-vue
npm init -y

# 配置
eslint --init
```

[选项配置信息](https://blog.csdn.net/Gabriel_wei/article/details/90269165)

## shortcut

### 代码操作

#### 光标

| 快捷键                 | 作用                  |
| :------------------ | :------------------ |
| Home / End          | 将光标定位到当前行的最 左 / 右 侧 |
| Shift + Alt + ↑ / ↓ | 向 上 / 下 添加光标        |
| Shift + Alt + i     | （所选区域）每一行的末尾都创建一个光标 |
| Esc                 | 取消多选光标              |

#### 删除

| 快捷键                       | 作用                |
| :------------------------ | :---------------- |
| Ctrl + Backspace / Delete | 删除光标之 前 / 后 的一个单词 |
| Ctrl + Shift + K          | 删除整行              |

#### 编辑

| 快捷键                  | 作用          |
| :------------------- | :---------- |
| Ctrl + Enter         | 在当前行下插入新的一行 |
| Ctrl + Shift + Enter | 在当前行上插入新的一行 |
| Alt + ↑ / ↓          | 将代码向上 / 下移动 |
| Shift + Alt + ↑ / ↓  | 将代码向上 / 下复制 |
| Ctrl + J             | 合并行         |

#### 折叠代码

| 快捷键                  | 作用              |
| :------------------- | :-------------- |
| Ctrl + Shift + [ / ] | 折叠 / 展开 所有子区域代码 |
| Ctrl + K Ctrl + 3    | 折叠所有 （html）     |
| Ctrl + K Ctrl + J    | 展开 所有           |

#### F 键

| 快捷键 | 作用          |
| --- | ----------- |
| F4  | 匹配下一个       |
| F12 | html 跳转 css |

#### 终端

| 快捷键               | 作用  |
| ----------------- | --- |
| Ctrl + \` \| 打开终端 |     |

### 编辑器

#### 基本操作

| 快捷键                              | 作用               |
| -------------------------------- | ---------------- |
| Ctrl + Pagedown/Pageup           | 在已经打开的文件之间进行切换   |
| Ctrl + + Shift + Pagedown/Pageup | 切换标签页的位置         |
| Ctrl + P                         | 在当前的项目工程里，全局搜索文件 |
| Ctrl + G                         | 跳转到指定行           |
| Ctrl + shift + O                 | 在当前文件的各种方法之间进行跳转 |

#### 分屏

| 快捷键                         | 作用    |
| --------------------------- | ----- |
| Shift + Alt + 2 / Ctrl + \| | 分屏    |
| Shift + Alt + 1             | 合并    |
| Ctrl + 1 / 2                | 切换分屏  |
| Ctrl + W                    | 关闭编辑器 |

### 插件

#### quokka （ JS TS 辅助 ）

| 快捷键        | 作用                           |
| ---------- | ---------------------------- |
| Ctrl + K Q | 打开新的 quokka 文件 => JavaScript |
| Ctrl + K J | 打开新的 quokka 文件 => TypeScript |
| Ctrl + K T | 在现有文件重新启动                    |

#### Settings Sync（ 配置同步 ）

| 快捷键             | 作用   |
| --------------- | ---- |
| Shift + Alt + U | 上传配置 |
| Shift + Alt + D | 下载配置 |

## VS Code settings.json 的配置备份

```js
{
  "files.associations": {
    "*.wxml": "wxml",
    "*.vue": "vue",
    "*.cjson": "jsonc",
    "*.wxss": "css",
    "*.wxs": "javascript"
  },
  "open-in-browser.default": "\"Chrome\"", // 打开浏览器 默认 Chrome
  // "terminal.integrated.shell.windows": "E:\\soft\\cmder\\Cmder.exe", // 主题设置
  "workbench.iconTheme": "vscode-icons", // 主题图标设置
  "vsicons.dontShowNewVersionMessage": true, // 关闭版本消息显示
  "editor.detectIndentation": false, // vscode默认启用了根据文件类型自动设置tabsize的选项
  "editor.tabSize": 2, // 重新设定tabsize
  "editor.mouseWheelZoom": true, // Ctrl 滚动缩放
  "editor.wordWrap": "on", // 自动换行
  "editor.formatOnSave": true, // 保存自动格式化
  "breadcrumbs.enabled": true, // 启用导航路径
  "javascript.updateImportsOnFileMove.enabled": "always", // 文件重命名时更新导入路径
  "editor.selectionHighlight": false, // 关闭自带高亮效果
  "editor.renderWhitespace": "all", // 显示空格
  "editor.fontFamily": "'Fira Code','Source Code Pro', 'STZhongsong'", // 字体设置
  "editor.fontLigatures": true, // 配置连体字
  "emmet.triggerExpansionOnTab": true, // emmet 语法
  "emmet.includeLanguages": {
    "javascript": "javascriptreact",
    "vue-html": "html",
    "razor": "html",
    "plaintext": "jade",
    "wxml": "html"
  },
  "git.enableSmartCommit": true,
  "git.autofetch": true,
  "fileheader.Author": "answer-zf", // 注释头部信息
  "fileheader.LastModifiedBy": "answer-zf", // 注释头部信息
  "[html]": {
    "editor.defaultFormatter": "vscode.html-language-features"
  },
  "[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "eslint.validate": [
    // 添加 vue 支持
    "javascript",
    "javascriptreact",
    {
      "language": "html",
      "autoFix": true
    },
    {
      "language": "vue",
      "autoFix": true
    }
  ],
  "eslint.autoFixOnSave": true, // 每次保存的时候将代码按eslint格式进行修复
  "files.autoGuessEncoding": true, // 打开文件自检字符集编码
  "prettier.semi": false, // 去掉代码结尾的分号
  "prettier.singleQuote": true, // 使用单引号替代双引号
  "vetur.format.defaultFormatter.stylus": "stylus-supremacy", // 使用单引号替代双引号
  "vetur.format.defaultFormatter.html": "js-beautify-html", // 让vue中的js按编辑器自带的ts格式进行格式化
  "vetur.format.defaultFormatterOptions": {
    // vue组件中html代码格式化样式
    "js-beautify-html": {
      "wrap_attributes": "force-aligned" //属性强制折行对齐
    }
  },
  "typescript.format.insertSpaceBeforeFunctionParenthesis": true, //让函数(名)和后面的括号之间加个空格
  "javascript.format.insertSpaceBeforeFunctionParenthesis": true,
  "editor.fontWeight": "500",
  "workbench.startupEditor": "newUntitledFile",
  "workbench.colorTheme": "Material",
  "editor.lineHeight": 26,
  "workbench.statusBar.visible": true,
  "[vue]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "window.zoomLevel": 0,
  "editor.cursorStyle": "block",
  "minapp-vscode.disableAutoConfig": true, // 微信小程序设置
  "minapp-vscode.showSuggestionOnEnter": true,
  "html.format.wrapAttributes": "force-aligned",
  "search.followSymlinks": false,
  "[markdown]": {
    "editor.defaultFormatter": "yzhang.markdown-all-in-one",
    // 自定义 md 代码段
    "editor.formatOnSave": true,
    "editor.renderWhitespace": "all",
    "editor.quickSuggestions": {
      "other": true,
      "comments": true,
      "strings": true
    },
    "editor.acceptSuggestionOnEnter": "on"
  },
  "[json]": {
    "editor.defaultFormatter": "vscode.json-language-features"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "terminal.integrated.shell.windows": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
  "typescript.validate.enable": false,
  "[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "sync.gist": "42cafa1971c8eabf28258d9dd154f762"
}
```
