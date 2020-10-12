# vim

## 模式切换

### 替换模式

-   进入替换模式：`R`
-   退出替换模式：`ESC`

### 粘贴模式

> 解决 Vim 缩进混乱

-   进入粘贴模式：`:set paste`
-   退出粘贴模式：`:set nopaste`

### 可视化模式（块）

-   v + 方向键 + c/y/d 
-   V + 方向键 + c/y/d 整行块

### 假死

-  Ctrl + s 禁止向终端输出（假死）
-  Ctrl + q 解除假死

## 基本操作


| 快捷键 | 作用       |
| :----- | :--------- |
| u      | 撤回       |
| CTRL R | 反撤回     |
| i      | 光标前输入 |
| a      | 光标后输入 |
| >>     | 缩进 >     |
| <<     | 缩进 <     |

## 光标

| 快捷键               | 作用                                                           |
| :------------------- | :------------------------------------------------------------- |
| h - j - k - l        | ← - ↓ - ↑ - →                                                  |
| 数字 + h - j - k - l | 光标快速移动到指定位置 ← - ↓ - ↑ - →                           |
| w                    | 光标跳到下个字的开头                                           |
| e                    | 光标跳到下个字的字尾                                           |
| b                    | 光标跳到上个字的开头                                           |
| 0 / ^                | 移动到行首                                                     |
| $                    | 移动到行末                                                     |
| +                    | 移动到下一行行首                                               |
| -                    | 移动到上一行行首                                               |
| : + 数字             | 跳转 .. 行                                                     |
| H - M - L            | 光标移动到这个屏幕的 最上方 - 中间 - 最下方 那一行的第一个字符 |
| gg                   | 跳转到文档最前                                                 |
| G                    | 跳转到文档最后                                                 |
| 数字 + gg / G        | 跳转到指定行号                                                 |
| %                    | 括号匹配跳转                                                   |
| { / }                | 跳转到代码块 开头/结尾                                         |

## 复制 、粘贴 、删除

| 快捷键         | 作用                               |
| :------------- | :--------------------------------- |
| y              | 复制（结合块使用）                 |
| yy             | 复制整行                           |
| y^             | 复制当前到行头的内容               |
| y$             | 复制当前到行尾的内容               |
| yw             | 复制一个 word                      |
| yG             | 复制到文档尾                       |
| 数字 + yy      | 复制光标及光标以下 xx 行           |
| d              | 剪切/删除                          |
| diw            | 删除光标所在的单词，不包括空白字符 |
| x / X          | 向后（向前）删除 字符              |
| p              | 粘贴                               |
| SHIFT + INSERT | 粘贴外部代码                       |
| J              | 合并行                             |

## 查询 、 替换

| 快捷键                | 作用                                                                        |
| :-------------------- | :-------------------------------------------------------------------------- |
| /word                 | 向光标向下寻找一个名称为word的字符串                                        |
| ?word                 | 向光标向上寻找一个名称为word的字符串                                        |
| n                     | 重复前一个查找                                                              |
| :n1,n2s/word1/word2/g | n1与n2为数字，在第n1与n2行之间查找word1 这个字符串，并将该字符串替换为word2 |
| :1,$s/word1/word2/g   | 从第一行到最后一行查找word1字符串，并将该字符串替换为word2                  |

## 折行

| 快捷键 | 作用     |
| :----- | :------- |
| zc     | 折行     |
| zo     | 打开折行 |

## 大小写转换

| 快捷键 | 作用     |
| :----- | :------- |
| gUw     | 大写     |
| guw     | 小写 |

## 自定义快捷键

-   ESC 设置为 CTRE I

    -   Linux 在 .vimrc 文件里设置
    -   Pycharm 在 .ideavimrc 文件里设置

    `:imap <C-I> <Esc>`

-   快捷键设置 规范如下

    -   <Esc>代表Escape键
    -   <CR>代表Enter键
    -   <D>代表Command键。
    -   Alt键可以使用<M-key>或<A-key>
    -   <C>代表Ctrl.
    -   对于组合键，可以用<C-Esc>代表Ctrl-Esc
    -   使用<S-F1>表示Shift-F1
    
    -   举例
        -   将 Ctrl-i 映射为 Esc : `:imap <C-I> <Esc>`
        -   配置F4为Ack快捷键 : `:map <F4> :Ack -i`
        -   在插入模式, 设置 ctrl + \ 为退出文件 : `:map! <C-\> <ESC>:q<CR>`
        
| Command命令 | 常规模式 | 可视化模式 | 运算符模式 | 插入模式 | 命令行模式 |
| :---------: | :------: | :--------: | :--------: | :------: | :--------: |
|    :map     |    √     |     √      |     √      |    -     |     -      |
|    :nmap    |    √     |     -      |     -      |    -     |     -      |
|    :vmap    |    -     |     √      |     -      |    -     |     -      |
|    :omap    |    -     |     -      |     √      |    -     |     -      |
|    :map!    |    -     |     -      |     -      |    √     |     √      |
|    :imap    |    -     |     -      |     -      |    √     |     -      |
|    :cmap    |    -     |     -      |     -      |    -     |     √      |