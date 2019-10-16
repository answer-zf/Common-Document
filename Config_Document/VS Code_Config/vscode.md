# VS Code 配置 



## 字体：[FiraCode](https://github.com/tonsky/FiraCode)



## json配置

```json

{
    "workbench.colorTheme": "SynthWave '84",
    "[html]": {
        "editor.defaultFormatter": "vscode.html-language-features"
    },
    "editor.mouseWheelZoom": true,
    "editor.wordWrap": "on",
    "prettier.arrowParens": "always",
    "[css]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "open-in-browser.default": "\"Chrome\"",
    "vsicons.dontShowNewVersionMessage": true,
    "workbench.iconTheme": "vscode-icons",
    "files.associations": {
        "*.wxml": "html"
    },
    "php.validate.executablePath": "C:/Develop/php/php.exe",
    "emmet.triggerExpansionOnTab": true,
    "fileheader.Author": "answer-zf",
    "fileheader.LastModifiedBy": "answer-zf",
    "editor.fontFamily": "Fira Code",
    "editor.fontLigatures": true,
    "files.autoGuessEncoding": true,
    "editor.selectionHighlight": false,
    "editor.renderWhitespace": "all",
    "emmet.includeLanguages": {
        "javascript": "javascriptreact",
        "vue-html": "html",
        "razor": "html",
        "plaintext": "jade"
    },
    "vscode_custom_css.imports": [
        "file:///C:/Users/Administrator/synthwave84.css"
    ],
    "prettier.jsxSingleQuote": true,
    "prettier.semi": false,
    "prettier.singleQuote": true,
    "prettier.eslintIntegration": true
}

```



## 插件

``` shell

$ Auto Close Tag
$ Auto Rename Tag
$ beautify
$ Bootstrap v4 Snippets
$ Bracket Pair Colorizer
$ Chinese (Simplified) Language Pack for Visual Studio Code
$ Code Runner
$ CSS Peek
$ Document This
$ Dracula Official
$ Git Blame
$ Git History
$ GitLens — Git supercharged
$ HTML CSS Support
$ HTML Snippets
$ npm Intellisense
$ open in browser
$ Path Intellisense
$ PHP intellisense for codeigniter
$ Prettier - Code formatter
$ Quokka.js
$ Sublime Text Keymap and Settings Importer
$ TODO Highlight
$ vscode-database
$ vscode-icons
$ PHP IntelliSense
$ PHP Intelephense
$ PHP DocBlocker
$ PHP Debug


$ Copy Relative Path
$ highlight-icemode
$ highlight-words
$ Rainbow Brackets ：突出显示成对的括号。
$ indent-rainbow：突出显示缩进。

格式化插件

$ Vetur
$ ESLint
$ Prettier - Code formatter

markdown
$ Markdown All in One
$ Markdown Shortcuts
$ Markdown Preview Enhanced
$ markdownlint

```



## 格式化插件配置



**.vscode/settings.json**

```json

{
  //.vue文件template格式化支持，并使用js-beautify-html插件
  "vetur.format.defaultFormatter.html": "js-beautify-html",
  //js-beautify-html格式化配置，属性强制换行
  "vetur.format.defaultFormatterOptions": {
    "js-beautify-html": {
      "wrap_attributes": "force-aligned"
    }
  },
  //根据文件后缀名定义vue文件类型
  "files.associations": {
    "*.vue": "vue"
  },
  //配置 ESLint 检查的文件类型
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    {
      "language": "vue",
      "autoFix": true
    }
  ],
  //保存时eslint自动修复错误
  "eslint.autoFixOnSave": true,
  //保存自动格式化
  "editor.formatOnSave": true
}

```



**.eslintrc.js**

```js

module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: ['plugin:vue/essential', 'eslint:recommended'],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    //强制使用单引号
    quotes: ['error', 'single'],
    //强制不使用分号结尾
    semi: ['error', 'never']
  },
  parserOptions: {
    parser: 'babel-eslint'
  }
}

```





##  快捷键



| Ctrl + W               |            关闭编辑器            |
| :--------------------- | :------------------------------: |
| Ctrl + Backspace       |      删除光标之前的一个单词      |
| Ctrl + delete          |      删除光标之后的一个单词      |
| Ctrl + Pagedown/Pageup |   在已经打开的文件之间进行切换   |
| Ctrl + Tab             |   在已经打开的文件之间进行跳转   |
| Ctrl + P               | 在当前的项目工程里，全局搜索文件 |

