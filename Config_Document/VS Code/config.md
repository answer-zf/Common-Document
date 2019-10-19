# VS Code 配置 



## 字体：[FiraCode](https://github.com/tonsky/FiraCode)



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
字体图标
Icon Fonts
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


