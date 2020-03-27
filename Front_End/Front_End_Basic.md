# Front_End

## HTML

1. 显示代码原有格式 类似模板字符串功能

   - 使用 `<pre></pre>` 标签

2. link 与 script 的区别

   - link 标签：链入一个文档，通过 rel 属性申明链入的文档与当前文档之间的关系
   - script 标签:
     1. `innerHTML` 永远不会显示在界面上
     2. 如果 `type` 不等于 `text/javascript` 的话，内部的内容不会作为 `Javascript` 执行

3. 自定义 radio CheckBox file...

```html
<style>
  #checkbox {
    display: none;
  }
  i::after {
    content: '☆';
  }
  #checkbox:checked + i::after {
    content: '★';
  }
</style>
<body>
  <label>
    <input type="checkbox" name="checkbox" id="checkbox" />
    <i style="font-size: normal"></i>
  </label>
</body>
```

4. 行内块级元素出现空格问题的解决 `font-size: 0`

## FLEX

### 方向：

- flex-direction

  - 默认值： row 水平向左

  - 常用值： column 垂直向下

  - 其他值：
    - row-reverse 水平向左
    - column-reverse 垂直向下

### 宽度均分

- flex: 1;

### 换行：

- flex-wrap

  - 默认值： nowrap 不换行，若超出则等比缩小（ flex-shrink=1 ）
  - 常用值： wrap 换行，第一行在上方。
  - 其他值： wrap-reverse 换行，第一行在下方。

### 对齐：

- justify-content

  - 默认值： flex-start 左对齐

  - 常用值：

    - flex-end 右对齐
    - center 居中
    - space-between 两端对齐

  - 其他值： space-around 两侧等距

- align-items

  - 默认值： flex-start 上对齐

  - 常用值：

    - flex-end 下对齐
    - center 居中

  - 其他值：
    - baseline 文字基线对其
    - stretch 占满容器

## JavaScript

### JS Basic

1. `return` or `break` or `continue`

   - `return`: 直接跳出函数 => 程度最大, 不执行后续

   - `break`: 直接跳出循环 => 程度一般, 不执行后续(若有循环嵌套，只能跳出一层，需要逐层 break)

   - `continue`: 终止单次循环，不能跳出循环 => 程度最小, 执行后续循环

2. `attr` or `prop`

   - `attr`: 获取的是 html 元素上的属性（即实际写在元素上的属性---elements 所监视到的属性）

   - `prop`: 获取的是 DOM 属性（获取的是 DOM 抽象出来的属性值，与 attr 的值部分有区别）

> DOM 会将 html 元素进行封装，而且会抽象出来做一些额外功能

3. 访问自定义属性 `data-...`

   - DOM: `.dataset['id']`

   - jQuery:
     - `.attr('data-id')`
     - `.data('id')`

4. 逻辑运算符优先级： `! > && > ||`

5. 逻辑运算符说明：

   - `||` 或的关系，如果前面的值等于 false 就会自动执行第二个值

   - `&&` 且的关系，如果前面的值等于 true 就会自动执行第二个值

6. 正则

   - 创建

     - `var rec = /^[a-zA-Z]@\.$/`

   - 验证

     - rec.test('str') => 找到返回 `boolean`

### API
