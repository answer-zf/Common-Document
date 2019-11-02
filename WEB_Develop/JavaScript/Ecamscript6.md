# Ecamscript6

## 前言

- ECMAScript 6.0（以下简称ES6）是JavaScript语言的下一代标准，已经在2015年6月正式发布了。
- Ecmascript 是 JavaScript 语言的标注规范
- JavaScript 是 Ecmascript 规范的具体实现
  + 具体实现取决于各大浏览器厂商的支持进度
- Ecmascript 6 也被称作 Ecmascript 2015
- 各大浏览器厂商对于最新的 Ecmascript 6 标准支持可以参照：
  + http://kangax.github.io/compat-table/es6/
- 对于不支持 ES6 的环境，可以使用一些编译转码工具做转换处理再使用
  + 例如 babel

## let 和 const

let：

- let 类似于 var，用来声明变量
- 通过 let 声明的变量不同于 var，只在 let 命令所在的代码块内有效（块级作用域）
- let 声明的变量不存在变量提升
- let不允许在相同作用域内，重复声明同一个变量

const：

- const声明一个只读的常量。一旦声明，常量的值就不能改变
- const 声明必须初始化
- const的作用域与let命令相同：只在声明所在的块级作用域内有效
- const命令声明的常量也是不提升，必须先声明后使用
- const声明的常量，也与let一样不可重复声明

## 解构赋值

ES6 允许按照一定模式，从数组和对象中提取值，对变量进行赋值，这被称为解构（Destructuring）。

数组解构：

```js
let [a, b, c] = [123, 456, 789]
console.log(a, b, c) 123 456 789
```

对象解构：

```js
let { name, age } = { name: 'Jack', age: 18 }
console.log(name, age) Jack 18
```

函数参数解构：

```js
function f (p1, { p2 = 'aa', p3 = 'bb' }) {
  console.log(p1, p2, p3)
}

f('p1', { p2: 'p2' }) p1 p2 bb
```

字符串解构：

```js
let [a, b, c, d, e] = 'hello'
console.log(a, b, c, d, e) h e l l o
```



## 字符串

实用方法：

```js
includes(String)：返回布尔值，表示是否找到了参数字符串。
startsWith(String)：返回布尔值，表示参数字符串是否在源字符串的头部。
endsWith(String)：返回布尔值，表示参数字符串是否在源字符串的尾部。
repeat(Number)：repeat方法需要指定一个数值，然后返回一个新字符串，表示将原字符串重复Number次。
```

模板字符串：

```js
let basket = { count: 5, onSale: true }
$('#result').append(`
  There are <b>${basket.count}</b> items
   in your basket, <em>${basket.onSale}</em>
  are on sale!
`);
```

- 模板字符串（template string）是增强版的字符串，用反引号（`）标识
- 它可以当作普通字符串使用，也可以用来定义多行字符串，或者在字符串中嵌入变量
- 如果使用模板字符串表示多行字符串，所有的空格和缩进都会被保留在输出之中
- 模板字符串中嵌入变量，需要将变量名写在 `${}` 之中
  + 大括号内部可以放入任意的JavaScript表达式，可以进行运算，以及引用对象属性
  + 大括号内部还可以调用函数

## 数组

方法：

```js
Array.from() 将一个伪数组转为一个真正的数组
              实际应用中，常见的类似数组的对象是DOM操作返回的NodeList集合，
              以及函数内部的arguments对象。Array.from都可以将它们转为真正的数组。
Array.of() Array.of方法用于将一组值，转换为数组
           这个方法的主要目的，是弥补数组构造函数Array()的不足。
           因为参数个数的不同，会导致Array()的行为有差异。
find() 查找数组中某个元素
findIndex() 查找数组中某个元素的索引下标
includes() 返回一个布尔值，表示某个数组是否包含给定的值，与字符串的includes方法类似
```

实例方法：

ES6提供三个新的方法——entries()，keys()和values()——用于遍历数组.
可以用 `for...of` 循环进行遍历，唯一的区别是 `keys()` 是对键名的遍历、
`values()` 是对键值的遍历，`entries()` 是对键值对的遍历。

```js
let arr = ['a', 'b', 'c']
console.log(arr.keys())
for (let index of arr.keys()) {
  console.log(index)
}
// 0
// 1
// 2

for (let item of arr.values()) {
  console.log(item)
}
// 'a'
// 'b'
// 'c'

for (let [index, item] of arr.entries()) {
  console.log(index, item)
}
// 0 'a'
// 1 'b'
// 2 'c'
```

扩展运算符：

```js
console.log(...[1, 2, 3]) 1 2 3
console.log(1, ...[2, 3, 4], 5) 1 2 3 4 5

// 合并数组
let arr1 = [123, 456]
let arr2 = [789, 890]
console.log([...arr1, ...arr2])   // [ 123, 456, 789, 890 ]
```



### find 详解

方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 undefined

#### 语法：

```js
arr.find(callback)
```

#### 参数：

callback

在数组每一项上执行的函数，接收 3 个参数：

- `element`  当前遍历到的元素。
- `index`（可选）当前遍历到的索引。
- `array`（可选）数组本身。

#### 返回值：

 数组中第一个满足所提供测试函数的元素的值，否则返回 `undefined`。 

#### 实例：

```js
var array = [5, 12, 8, 130, 44];

var found = array.find(function(item) {
  return item === 130;
});

console.log(found)  // 结果：130
```

 #### 底层原理

```js
// find 接收一个方法作为参数，方法内部返回一个条件
// find 会遍历所有的元素，执行你给定的带有条件返回值的函数
// 符合该条件的元素会作为 find 方法的返回值
// 如果遍历结束还没有符合该条件的元素，则返回 undefined
Array.prototype.myFind = function (conditionFunc) {
  for (var i = 0; i < this.length; i++) {
    if (conditionFunc(this[i], i)) {
      return this[i]
    }
  }
}

var ret = users.myFind(function (item, index) {
  return item.id === 2
})
```

every  -- 方法测试一个数组内的所有元素是否都能通过某个指定函数的测试。它返回一个布尔值。 

some  --  方法测试数组中是不是有元素通过了被提供的函数测试。它返回的是一个Boolean类型的值。 

findIndex--  方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 [`undefined`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/undefined)。

includes  --   方法返回数组中满足提供的测试函数的第一个元素的索引。否则返回-1。 

map --  方法创建一个新数组，其结果是该数组中的每个元素都调用一个提供的函数后返回的结果。 

reduce --  方法对数组中的每个元素执行一个由您提供的**reducer**函数(升序执行)，将其结果汇总为单个返回值 



## 函数的扩展

### 函数参数的默认值：

```js
ES6 允许为函数的参数设置默认值，即直接写在参数定义的后面。

function log(x, y = 'World') {
  console.log(x, y);
}

log('Hello') Hello World
log('Hello', 'China') Hello China
log('Hello', '') Hello
```

- 通常情况下，定义了默认值的参数，应该是函数的尾参数
  + 因为这样比较容易看出来，到底省略了哪些参数
  + 如果非尾部的参数设置默认值，实际上这个参数是没法省略的。
- 指定了默认值以后，函数的length属性，将返回没有指定默认值的参数个数
  + 也就是说，指定了默认值后，length属性将失真

### rest 参数：

```js

f(1, 2, 3) 

function f(x, y, z) {
  console.log(Array.from(arguments)) // [ 1, 2, 3 ]
}
// ...args 叫做 rest 参数
// ...args 是一种语法，...不能省略，args 是随便起的一个名字
// ...args 可以将用户传递进来的参数包装到一个数组中
function f(...args) {
  console.log(args) // [ 1, 2, 3 ]
}

// ...args 是把用户传递参数的没有对应到具体形参的变量解析到一个数组中
function f(a, ...args) {
  console.log(args)  // [2, 3]
}

function add(...values) {
  let sum = 0;

  for (var val of values) {
    sum += val;
  }

  return sum;
}

add(2, 5, 3) 10
```

### 箭头函数：

```js
var f = v => v

上面的箭头函数等同于：

var f = function(v) {
  return v
}

let foo = (x, y) => {
  console.log(x, y)
  return x + y
}
```

- 箭头函数体内的this对象，就是定义时所在的对象，而不是使用时所在的对象
- 箭头函数不可以当作构造函数，也就是说，不可以使用new命令，否则会抛出一个错误
- 箭头函数内部不可以使用arguments对象，该对象在函数体内不存在
  + 如果要用，可以用Rest参数代替

使用场景：

- 箭头函数最好都用在匿名函数的地方