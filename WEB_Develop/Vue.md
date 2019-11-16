# Vue.js

## Node（后端）中的 MVC 与 前端中的 MVVM 之间的区别

 + MVC 是后端的分层开发概念，分为 Model ，View，Controllers
 + MVVM是前端视图层的概念，主要关注于 视图层分离，也就是说：MVVM把前端的视图层，分为了 三部分 Model, View , VM ViewModel

![01.MVC和MVVM的关系图解](media/Untitled. assets/01.MVC和MVVM的关系图解.png)

## Vue 基础

### 基本代码结构

```vue
...
<!-- 1. 导入Vue的包 -->
<script src="./lib/vue-2.4.0.js"></script>
<!-- 将来 new 的Vue实例，会控制这个 元素中的所有内容 -->
<!-- Vue 实例所控制的这个元素区域，就是我们的 V  -->
<div id="app">
  <p>{{ msg }}</p>
</div>
<script>
  // 2. 创建一个Vue的实例
  // 当我们导入包之后，在浏览器的内存中，就多了一个 Vue 构造函数
  //  注意：我们 new 出来的这个 vm 对象，就是我们 MVVM中的 VM调度者
  var vm = new Vue({
    el: '#app',  // 表示，当前我们 new 的这个 Vue 实例，要控制页面上的哪个区域
    // 这里的 data 就是 MVVM中的 M，专门用来保存 每个页面的数据的
    data: { // data 属性中，存放的是 el 中要用到的数据
      msg: '欢迎学习Vue' // 通过 Vue 提供的指令，很方便的就能把数据渲染到页面上，程序员不再手动操作DOM元素了【前端的Vue之类的框架，不提倡我们去手动操作DOM元素了】
    }
  })
</script>
```

### 基础数据操作

#### 插值表达式 、  `v-text` 、`v-html`

##### 插值表达式： 

```vue
<style>
  [v-cloak] {
     display: none; 
  }
</style>
<div v-cloak>{{ msg }}</div>
```

- 会由于`script` 标签位置的不确定性，会出现闪烁问题

- 相较于 `v-text`  ,插值表达式只会替换自己的这个占位符，不会把 整个元素的内容清空

- 可以使用 `v-cloak` 解决 闪烁问题

##### `v-text`

```vue
<div v-text="msg"></div>
```

- 默认 `v-text` 是没有闪烁问题的
- `v-text`会覆盖元素中原本的内容

##### `v-html`

```vue
<div v-html="msg2">1212112</div>
```

- 能够解析 `html` 标签 并 渲染 前面两个只能把标签当作字符串输出
- 默认 `v-html` 是没有闪烁问题的
- `v-html`会覆盖元素中原本的内容

#### `v-bind`

`v-bind`: 是 Vue中，提供的用于绑定属性的指令

```vue
<input type="button" value="按钮" v-bind:title="msg + '123'">
```

- `v-bind:` 指令可以被简写为 `:`要绑定的属性
  - `<input type="button" value="按钮" :title="msg + '123'">`
- `v-bind` 中，可以写合法的JS表达式

#### `v-on` 与 事件修饰符

##### `v-on`

Vue 中提供了 `v-on:` 事件绑定机制

```vue
<input type="button" value="按钮" v-on:click="show" id="app">
<script>
    var vm = new Vue({
      el: '#app',
      methods: { // 这个 methods属性中定义了当前Vue实例所有可用的方法
        show: function () {
          alert('Hello')
        }
      }
    })
</script>
```

- `v-on:` 指令可以被简写为 `@`要绑定的属性
  - `<input type="button" value="按钮" @click="show">`

##### 事件修饰符

+ .stop       阻止冒泡

+ .prevent    阻止默认事件

+ .capture    添加事件侦听器时使用事件捕获模式

+ .self       只当事件在该元素本身（比如不是子元素）触发时触发回调

+ .once       事件只触发一次

###### 实例结构

```vue
<style>
  .inner {
    height: 150px;
    background-color: darkcyan;
  }

  .outer {
    padding: 40px;
    background-color: red;
  }
</style>
<div id="app">
  
</div>
<script>
  // 创建 Vue 实例，得到 ViewModel
  var vm = new Vue({
    el: '#app',
    data: {},
    methods: {
      div1Handler() {
        console.log('这是触发了 inner div 的点击事件')
      },
      btnHandler() {
        console.log('这是触发了 btn 按钮 的点击事件')
      },
      linkClick() {
        console.log('触发了连接的点击事件')
      },
      div2Handler() {
        console.log('这是触发了 outer div 的点击事件')
      }
    }
  });
</script>
```

###### 使用`.stop` 阻止冒泡 （里 -> 外）

```vue
<div class="inner" @click="div1Handler">
  <input type="button" value="戳他" @click.stop="btnHandler">
</div>
```

###### 使用 `.prevent` 阻止默认行为

```vue
<a href="http://www.baidu.com" @click.prevent="linkClick">有问题，先去百度</a>
```

###### 使用  .capture 实现捕获触发事件的机制 （外 -> 里）

```vue
<div class="inner" @click.capture="div1Handler">
  <input type="button" value="戳他" @click="btnHandler">
</div>
```

###### 使用 .self 实现只有点击当前元素时候，才会触发事件处理函数

```vue
<div class="inner" @click="div1Handler">
  <input type="button" value="戳他" @click="btnHandler">
</div>
```

- 相较于`.self` 只会阻止自己身上冒泡行为的触发，并不会真正阻止 冒泡的行为

  ```vue
  <div class="outer" @click="div2Handler">
    <div class="inner" @click.self="div1Handler">
      <input type="button" value="戳他" @click="btnHandler">
    </div>
  </div>
  ```

###### 使用 .once 只触发一次事件处理函数

```vue
<a href="http://www.baidu.com" @click.prevent.once="linkClick">有问题，先去百度</a>
```

- 事件修饰符可以串联
- `.prevent` 与 `.once` 前后关系

#### 双向数据绑定 `v-model`

`v-bind:`只能实现数据的单向绑定，从 M 自动绑定到 V，无法实现数据的双向绑定

`v-model` 指令，可以实现表单元素和  Model 中数据的双向数据绑定（只能在表单元素中使用）

```vue
<input type="text" name="" v-model="msg" id="">
```

