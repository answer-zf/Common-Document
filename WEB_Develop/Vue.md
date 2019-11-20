# Vue.js

## Node（后端）中的 MVC 与 前端中的 MVVM 之间的区别

 + MVC 是后端的分层开发概念，分为 Model ，View，Controllers
 + MVVM是前端视图层的概念，主要关注于 视图层分离，也就是说：MVVM把前端的视图层，分为了 三部分 Model, View , VM ViewModel

![01.MVC和MVVM的关系图解](media/Untitled. assets/01.MVC和MVVM的关系图解.png)

## Vue 基础

### 基本代码结构

- el  指定要控制的区域   
- data 是个对象，指定了控制的区域内要用到的数据    
- methods 虽然带个s后缀，但是是个对象，这里可以自定义了方法

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

#### `mustache` 、  `v-text` 、`v-html`

##### 插值表达式：(`mustache`) 

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
- 使用事件绑定机制，为元素指定事件处理函数时，如加`()`，就可以给函数传参。

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

####  `v-model`（双向数据绑定）

`v-bind:`只能实现数据的单向绑定，从 M 自动绑定到 V，无法实现数据的双向绑定

`v-model` 指令，可以实现表单元素和  Model 中数据的双向数据绑定（只能在表单元素中使用）

```vue
<input type="text" name="" v-model="msg" id="">
```

> 在Vue中，已经实现了数据的双向绑定，每当我们修改了 data 中的数据，Vue会默认监听到数据的改动，自动把最新的数据，应用到页面上

#### 样式操作

##### 使用class样式

1. 数组
```html
<h1 :class="['red', 'thin']">这是一个邪恶的H1</h1>
```

2. 数组中使用三元表达式
```html
<h1 :class="['red', 'thin', isactive?'active':'']">这是一个邪恶的H1</h1>
```

3. 数组中嵌套对象（代替三元表达式，提高代码的可读性）
```html
<h1 :class="['red', 'thin', {'active': isactive}]">这是一个邪恶的H1</h1>
```

4. 直接使用对象

```html
<h1 :class="{red:true, italic:true, active:true, thin:true}">这是一个邪恶的H1</h1>
```

- 在为 class 使用 v-bind 绑定 对象的时候，对象的属性是类名，由于 对象的属性可带引号，也可不带引号，所以 这里我没写引号；  属性的值 是一个标识符

```vue
<h1 :class="obj">这是一个邪恶的H1</h1>
<script>
...
data: {
  ...
  obj: {red:true, italic:true, active:true, thin:true}
  ...
}
...
</script>
```

##### 使用内联样式

1. 直接在元素上通过 `:style` 的形式，书写样式对象
```
<h1 :style="{color: 'red', 'font-size': '40px'}">这是一个善良的H1</h1>
```

2. 将样式对象，定义到 `data` 中，并直接引用到 `:style` 中
 + 在data上定义样式：
```
data: {
        h1StyleObj: { color: 'red', 'font-size': '40px', 'font-weight': '200' }
}
```
 + 在元素中，通过属性绑定的形式，将样式对象应用到元素中：
```
<h1 :style="h1StyleObj">这是一个善良的H1</h1>
```

3. 在 `:style` 中通过数组，引用多个 `data` 上的样式对象
 + 在data上定义样式：
```
data: {
        h1StyleObj: { color: 'red', 'font-size': '40px', 'font-weight': '200' },
        h1StyleObj2: { fontStyle: 'italic' }
}
```
 + 在元素中，通过属性绑定的形式，将样式对象应用到元素中：
```
<h1 :style="[h1StyleObj, h1StyleObj2]">这是一个善良的H1</h1>
```

#### `v-for`和`key`属性

1. 迭代数组

```vue
<ul>
  <li v-for="(item, i) in list">索引：{{i}} --- 姓名：{{item.name}} --- 年龄：{{item.age}}</li>
</ul>
```

2. 迭代对象中的属性

```vue
<!-- 循环遍历对象身上的属性 -->
<!-- 注意：在遍历对象身上的键值对的时候， 除了有 val key ,在第三个位置还有 一个 索引  -->
<p v-for="(val, key, i) in list">值是： {{ val }} --- 键是： {{key}} -- 索引： {{i}}</p>
```

3. 迭代数字

```vue
<!-- 注意：如果使用 v-for 迭代数字的话，前面的 count 值从 1 开始 -->
<p v-for="i in 10">这是第 {{i}} 个P标签</p>
```



> 2.2.0+ 的版本里，**当在组件中使用** v-for 时，key 现在是必须的。

当 Vue.js 用 v-for 正在更新已渲染过的元素列表时，它默认用 “**就地复用**” 策略。如果数据项的顺序被改变，Vue将**不是移动 DOM 元素来匹配数据项的顺序**， 而是**简单复用此处每个元素**，并且确保它在特定索引下显示已被渲染过的每个元素。

为了给 Vue 一个提示，**以便它能跟踪每个节点的身份，从而重用和重新排序现有元素**，你需要为每项提供一个唯一 key 属性。

```vue
<div id="app">

  <div>
    <label>Id:
      <input type="text" v-model="id">
    </label>
    <label>Name:
      <input type="text" v-model="name">
    </label>
    <input type="button" value="添加" @click="add">
  </div>
  <!-- 注意： v-for 循环的时候，key 属性只能使用 number或string -->
  <!-- 注意： key 在使用的时候，必须使用 v-bind 属性绑定的形式，指定 key 的值 -->
  <!-- 在组件中，使用v-for循环的时候，或者在一些特殊情况中，如果 v-for 有问题，必须 在使用 v-for 的同时，指定 唯一的 字符串/数字 类型 :key 值 -->
  <p v-for="item in list" :key="item.id">
    <input type="checkbox">{{item.id}} --- {{item.name}}
  </p>
</div>
<script>
  // 创建 Vue 实例，得到 ViewModel
  var vm = new Vue({
    el: '#app',
    data: {
      id: '',
      name: '',
      list: [
        { id: 1, name: '李斯' },
        { id: 2, name: '嬴政' },
        { id: 3, name: '赵高' },
        { id: 4, name: '韩非' },
        { id: 5, name: '荀子' }
      ]
    },
    methods: {
      add() { // 添加方法
        this.list.unshift({ id: this.id, name: this.name })
      }
    }
  });
</script>
```

#### `v-if` 和 `v-show`

##### `v-if` 

- 每次都会重新删除或创建元素
- 有较高的切换性能消耗

##### `v-show`

- 每次不会重新进行DOM的删除和创建操作，只是切换了元素的 display:none 样式
- 有较高的初始渲染消耗

```vue
<input type="submit" value="切换" @click="flag=!flag">
    <h3 v-if="flag">v-if--------Lorem ipsum dolor, sit amet consectetur adipisicing elit.</h3>
    <h3 v-show="flag">v-show--------Lorem ipsum dolor, sit amet consectetur adipisicing elit.</h3>
```

如果元素涉及到频繁的切换，最好不要使用 v-if, 而是推荐使用 v-show

如果元素可能永远也不会被显示出来被用户看到，则推荐使用 v-if

### 过滤器

- 概念：Vue.js 允许你自定义过滤器，**可被用作一些常见的文本格式化**。
- 过滤器可以用在两个地方：**mustache 插值和 v-bind 表达式**。
- 过滤器应该被添加在 JavaScript 表达式的尾部，由“管道”符指示。
  - 调用：
    - `{{ name | '过滤器名称' }}`

#### 全局过滤器

`Vue.filter('过滤器名称', function () { })`

其中的 function ，第一个参数，已经被规定死了，永远都是 过滤器 管道符前面 传递过来的数据

#### 私有过滤器

在Vue 实例中，增加一个属性值：`filters：{}`

> 注意：当有局部和全局两个名称相同的过滤器时候，会以就近原则进行调用，即：局部过滤器优先于全局过滤器被调用！

#### 实例演示

```vue
<div id="app">
  <div class="panel panel-primary">
    <div class="panel-heading">
      <div class="panel-title">brand management</div>
    </div>
    <div class="panel-body form-inline">
      <label for="">
        Id:
        <input type="text" name="" id="" class="form-control" v-model="id">
      </label>
      <label for="">
        NAME:
        <input type="text" name="" id="" class="form-control" v-model="name">
      </label>
      <input type="button" value="add" class="btn btn-primary" @click="add">
      <label for="">
        搜索:
        <input type="text" name="" id="" class="form-control" v-model="keywords" >
      </label>
    </div>
  </div>
  <table class="table table-bordered table-hover progress-striped">
    <thead>
      <tr>
        <th>Id</th>
        <th>NAME</th>
        <th>Ctime</th>
        <th>Operation</th>
      </tr>
    </thead>
    <tbody>
<!-- 之前， v-for 中的数据，都是直接从 data 上的list中直接渲染过来的 -->
<!-- 现在：自定义一个 search 方法，同时，把所有的关键字，通过传参的形式，传递给了 search 方法 -->
<!-- 在 search 方法内部，通过执行 for 循环，把所有符合 搜索关键字的数据，保存到一个新数组中，返回-->
      <tr v-for="item in search(keywords)" :key="item.id">
        <td>{{item.id}}</td>
        <td>{{item.name}}</td>
        <td>{{ item.Ctime | dateFormat }}</td>
        <td>
          <a href="" @click.prevent="deleteFrom(item.id)">Delete</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
<script>
  Vue.filter('dateFormat', function (dateStr, pattern = '') {  // 全局过滤器
    // 根据给定的时间字符串，得到特定的时间
    var dt = new Date(dateStr)
    var y = dt.getFullYear()
    var m = (dt.getMonth() + 1).toString().padStart(2, '0')
    var d = dt.getDate().toString().padStart(2, '0')
    if (pattern.toLowerCase === 'yyyy-mm-dd') {
      return `${y}-${m}-${d}`
    }
    var hh = dt.getHours().toString().padStart(2, '0')
    var mm = dt.getMinutes().toString().padStart(2, '0')
    var ss = dt.getSeconds().toString().padStart(2, '0')
    return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
  })
  var vm = new Vue({
    el: '#app',
    data: {
      id: '',
      name: '',
      keywords: '',
      list: [
        { id: 1, name: 'BMW', Ctime: new Date() },
        { id: 2, name: 'BZ', Ctime: new Date() },
      ]
    },
    methods: {
      add() {
        var obj = {
          id: this.id,
          name: this.name,
          Ctime: new Date()
        }
        this.list.push(obj)
        this.id = this.name = ''
      },
      deleteFrom(id) {
        var index = this.list.findIndex(item => item == id)
        this.list.splice(index, 1)
      },
      search(keywords) {
        return this.list.filter(item => {
          if (item.name.includes(keywords)) {
            return true
          }
        })
      }
    },
    filters: { // 私有过滤器
      dateFormat(dateStr, pattern = '') {
        var dt = new Date(dateStr)
        var y = dt.getFullYear()
        var m = (dt.getMonth() + 1).toString().padStart(2, '0')
        var d = dt.getDate().toString().padStart(2, '0')
        if (pattern.toLowerCase === 'yyyy-mm-dd') {
          return `${y}-${m}-${d}`
        }
        var hh = dt.getHours().toString().padStart(2, '0')
        var mm = dt.getMinutes().toString().padStart(2, '0')
        var ss = dt.getSeconds().toString().padStart(2, '0')
        return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
      }
    }
  })
</script>
```

### 键盘修饰符以及自定义键盘修饰符

#### 1.x中自定义键盘修饰符【了解即可】

```js
Vue.directive('on').keyCodes.f2 = 113;
```

#### 2.x中自定义键盘修饰符

1. 通过`Vue.config.keyCodes.名称 = 按键值`来自定义案件修饰符的别名：

```js
Vue.config.keyCodes.f2 = 113;
```

2. 使用自定义的按键修饰符：

```html
<input type="text" v-model="name" @keyup.f2="add">
```

3. 相关文档：

> js 里面的键盘事件对应的键码：http://www.cnblogs.com/wuhua1/p/6686237.html
> vue 2.x 键盘修饰符文档：https://cn.vuejs.org/v2/guide/events.html#键值修饰符

###  自定义指令

#### 全局自定义指令：

使用  `Vue.directive('自定义属性名', { })` 定义全局的自定义指令

- 参数1 ： 指令的名称，注意: 在定义的时候，指令的名称前面，不需要加 v- 前缀
  - 在调用的时候，必须 在指令名称前 加上 v- 前缀来进行调用

- 参数2： 是一个对象，这个对象身上，有一些指令相关的函数，这些函数可以在特定的阶段，执行相关的操作

  >  vue 2.x 自定义指令文档：https://cn.vuejs.org/v2/guide/custom-directive.html

  ```js
  ···
  <input type="text" class="form-control" v-model="keywords" id="search" v-focus v-color="'blue'">// 'blue'不加单引号会当成变量在，data 中找。
  ···
  
  Vue.directive('focus', {
    bind: function (el) { // 每当指令绑定到元素上的时候，会立即执行这个 bind 函数，只执行一次
      // 注意： 在每个 函数中，第一个参数，永远是 el ，表示 被绑定了指令的那个元素，这个 el 参数，是一个原生的JS对象
      // 在元素 刚绑定了指令的时候，还没有 插入到 DOM中去，这时候，调用 focus 方法没有作用
      // 因为，一个元素，只有插入DOM之后，才能获取焦点
      // el.focus()
    },// inserted 表示元素 插入到DOM中的时候，会执行 inserted 函数【触发1次】
    inserted: function (el) {  
      el.focus()
      // 和JS行为有关的操作，最好在 inserted 中去执行，防止 JS行为不生效
    },
    update: function (el) {  // 当VNode更新的时候，会执行 updated， 可能会触发多次
    }
  })
  
  Vue.directive('color', {
  // 样式，只要通过指令绑定给了元素，不管这个元素有没有被插入到页面中去，这个元素肯定有了一个内联的样式
  // 将来元素肯定会显示到页面中，这时候，浏览器的渲染引擎必然会解析样式，应用给这个元素
    bind: function (el, binding) {
      // 和样式相关的操作，一般都可以在 bind 执行
      // console.log(binding.value)      指令的绑定值  				clg: blue
      // console.log(binding.expression) 字符串形式的指令表达式 clg: 'blue'
      el.style.color = binding.value
    }
  })
  ```

  总结 ： 与样式有关的操作，设置到 `bind` 中，与行为有关的操作，设置到 `inserted`  中。

  ​			  `bind` 的执行时机，早与 `inserted` 。

#### 局部自定义指令：

在Vue 实例中，增加一个属性值：`directives：{}`

```html
<input type="text" class="form-control" v-model="keywords" v-fontweight="200">
···
directives: {
  'fontweight': {
    bind(el, binding) {
      el.style.fontWeight = binding.value
    }
  }
}
···
```

#### 自定义属性中函数简写：

若只使用 `bind` 和  `update`  触发相同行为，而不关心其它的钩子。 可简写：

```html
<input type="text" class="form-control" v-model="keywords" v-fontweight="200">
···
directives: {
  // 注意：这个 function 等同于 把 代码写到了 bind 和 update 中去
  'fontsize': function (el, binding) { 
    el.style.fontSize = parseInt(binding.value) + 'px'
  }
}
···
```

