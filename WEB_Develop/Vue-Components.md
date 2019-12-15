## Vue 中的组件

### 定义：

什么是组件： 组件的出现，就是为了拆分Vue实例的代码量的，能够让我们以不同的组件，来划分不同的功能模块，将来我们需要什么样的功能，就可以去调用对应的组件即可；
组件化和模块化的不同：

 + 模块化： 是从代码逻辑的角度进行划分的；方便代码分层开发，保证每个功能模块的职能单一；
 + 组件化： 是从UI界面的角度进行划分的；前端的组件化，方便UI组件的重用；

### 全局组件定义的三种方式

定义组件的时候，如果要定义全局的组件， `Vue.component('组件的名称', {})`

1. 使用 `Vue.extend` 配合 `Vue.component` 方法：

   ```js
   // 使用 Vue.extend 来创建全局的Vue组件
   var com1 = Vue.extend({
     template: '<h3>Lorem ipsum dolor sit amet consectetur</h3>'
   })
   // 使用 Vue.component('组件的名称', 创建出来的组件模板对象)
   Vue.component('myCom1', com1)
   ```

   简写：

   ```js
   Vue.component('myCom1', Vue.extend({
     template: '<h3>Lorem ipsum dolor sit amet consectetur</h3>'
   }))
   ```

   -  第一个参数: 组件的名称, 将来在引用组件的时候, 就是一个标签形式 来引入 它的
   -  第二个参数:  `Vue.extend` 创建的组件  ,其中 `template`  就是组件将来要展示的HTML内容

   如果要使用组件，直接，把组件的名称，以 HTML 标签的形式，引入到页面中，即可

   ```html
   <div id="app">
     <my-com1></my-com1>
   </div>
   ```

   - 如果使用 Vue.component 定义全局组件的时候，组件名称使用了 驼峰命名，那么在使用组件的时候，只能在字符串模板中用驼峰的方式使用组件，但是在普通的标签模板中，需要把 大写的驼峰改为小写的字母，同时，两个单词之前，使用 - 链接
   - 如果不使用驼峰,则直接拿名称来使用即可

   ##### 组件注意事项

   - 组件参数的data值必须是函数同时这个函数要求返回一个对象 
     - 使用函数的作用：形成闭包的环境，使每个组件都拥有独立的数据
   - 组件模板必须是单个根元素
   - 组件模板的内容可以是模板字符串

2. 直接使用 Vue.component 方法：

   ```js
   Vue.component('myCom1', {
         template: '<h3>Lorem ipsum dolor sit amet consectetur</h3>'
       })
   ```

3. 将模板字符串，定义到 `template` 元素中：

   ```js
   Vue.component('myCom1', {
     template: '#tmpl'
   })
   ```

   在 被控制的 `#app` 外面,使用 `template` 元素,定义组件的HTML模板结构

   ```html
   <div id="app">
     <my-Com1></my-Com1>
   </div>
   <template id="tmpl">
     <div>
       <h3>Lorem ipsum dolor sit amet consectetur</h3>
     </div>
   </template>
   ```

`注意 : 不论是哪种方式创建出来的组件,组件的 template 属性指向的模板内容,必须有且只能有唯一的一个根元素`

### 私有组件定义

- 局部组件只能在注册他的父组件中使用

```js
var vm2 = new Vue({
  el: '#app2',
  components: {
    'myCom2': {
      template: '<h3>consectetur adipisicing elit. Commodi, nihil?</h3>'
    }
  }
})
```

`template: '#tmpl2'`同理全局定义方式。

### 组件中展示数据和响应事件

1. 组件可以有自己的 `data` 数据

   - 组件的 `data` 和 实例的 `data` 有点不一样,实例中的 `data` 可以为一个对象,但是 组件中的 data 必须是一个方法，而且这个方法内部必须返回一个对象
   - 组件中 的`data` 数据,使用方式,和实例中的 `data` 使用方式完全一样

   ```js
   Vue.component('vuecontent', {
     template: '<h2>this is h2,------data is {{msg}}</h2>',
     data() {
       return {
         msg: 'Lorem ipsum dolor sit amet'
       }
     }
   })
   ```

2. 组件可以有自己的 `methods` 响应时间。

   - 使用同 `vue` 实例

### 组件间切换

#### 使用`flag`标识符结合`v-if`和`v-else`切换组件

页面结构：

```html
<div id="app">
  <a href="#" @click.prevent="flag = true">login</a>
  <a href="#" @click.prevent="flag = false">register</a>
  <login v-if="flag"></login>
  <register v-else="flag"></register>
</div>
```

vue实例：

```js
Vue.component('login', {
  template: '<h3>login</h3>'
})
Vue.component('register', {
  template: '<h3>register</h3>'
})
```

#### 使用`components`属性定义局部子组件

Vue提供了 `component` ,来展示对应名称的组件

`component` 是一个占位符, `:is` 属性,可以用来指定要展示的组件的名称

页面结构：

```html
<div id="app">
  <a href="#" @click.prevent="comName = 'login'">login</a>
  <a href="#" @click.prevent="comName = 'register'">register</a>
  <component :is="comName"></component>
</div>
```

vue实例：

```js
var vm = new Vue({
  el: '#app',
  data: {
    comName: 'login' // 当前 component 中的 :is 绑定的组件的名称
  },
  methods: {}
})
```

#### 组件切换的动画应用：

使用 `transition`元素包裹 `component`元素，并设置样式即可

并且通过 `transition`元素中的 `mode` 属性,设置组件切换时候的 模式

页面结构：

```html
<transition mode="out-in">
  <component :is="comName"></component>
</transition>
```

css样式：

```css
.v-enter,
.v-leave-to {
  opacity: 0;
  transform: translateX(100px);
}
.v-enter-active,
.v-leave-active {
  transition: all .8s ease;
}
```

### 组件传值：

#### 父组件向子组件传值：

- 本质：父组件向子组件传递数据 `data`

子组件中，默认无法访问到 父组件中的 `data` 上的数据 和 `methods` 中的方法

父组件，可以在引用子组件的时候， 通过 属性绑定`(v-bind:)` 的形式, 把 需要传递给 子组件的数据，以属性绑定的形式，传递到子组件内部，供子组件使用

```html
<div id="app">
  <com1 :parentmsg="msg"></com1>
</div>
<script>
  var vm = new Vue({
    el: '#app',
    data: {
      msg: '132'
    },
    components: {
      com1: {
        template: '<h1>9-----{{parentmsg}}</h1>',
        props: [ // 把父组件传递过来的 parentmsg 属性，
          			 // 先在 props 数组中，定义一下，这样，才能使用这个数据
          'parentmsg'
        ]
      }
    }
  })
</script>
```

- 与 组建中的 `data`的 区别：
  - 子组件中的 `data` 数据，并不是通过 父组件传递过来的，而是子组件自身私有的，比如： 子组件通过 Ajax ，请求回来的数据，都可以放到 `data` 身上；且 `data` 上的数据，都是可读可写的
  - 组件中的 所有 `props` 中的数据，都是通过 父组件传递给子组件的；且`props` 中的数据，都是只读的，无法重新赋值
- 父组件发送的形式是以属性的形式绑定值到子组件身上。
- 然后子组件用属性props接收
- props传递数据原则：单向数据流，只允许父组件向自组建传递数据，不允许子组件直接操作，props中的数据
- 在props中使用驼峰形式，模板中需要使用短横线的形式字符串形式的模板中没有这个限制

#### 子组件向父组件传值：

- 父组件向子组件传递方法 `methods`

父组件向子组件 传递 方法，使用的是 事件绑定机制； `v-on`, 当我们自定义了 一个 事件属性之后，那么，子组件就能够，通过某些方式，来调用 传递进去的 这个 方法

```html
<div id="app">
  <com1 @func="show"></com1> // 切记 show 不能加（），不能传参，表示的是方法而不是调用！
  <com1 @func="show($event)"></com1>
</div>
<template id="tmpl">
  <div>
    <h1>this is component for son </h1>
    <input type="button" value="touch" @click="touch">
  </div>
</template>
<script>
  var com1 = { // 定义了一个字面量类型的 组件模板对象
    template: '#tmpl', // 通过指定了一个 Id, 表示要去加载这个指定Id的 template 元素中的内容，当作组件的HTML结构
    data() {
      return {
        sonmsg: {
          name: 'zf',
          age: 18
        }
      }
    },
    methods: {
      touch() { // 当点击子组件按钮的时候，通过 this.$emit 拿到父组件传递过来的 func 方法，并调用
        this.$emit('func', this.sonmsg)
      }
    }
  }
  var vm = new Vue({
    el: '#app',
    data: {
      datamsgFromSon: null
    },
    methods: {
      show(data) {
        this.datamsgFromSon = data
      }
    },
    components: {
      com1
    }
  })
</script>
```

#### 利用传值原理，在`localStorage`存储数据：

 将数据存放在内存中使用 h5 的新特性 `localStorage`

- `localStorage` 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去删除。

- `localStorage` 中的键值对总是以字符串的形式存储 ，而且是只读的 
- 保存数据：`localStorage.setItem('myCat', 'Tom')` 
- 读取数据：`localStorage.getItem('myCat')`

页面结构：

```html
<div id="app">
  <comment-box @load="loadComments"></comment-box>
  <ul class="list-group">
    <li class="list-group-item" v-for="item in list" :key="item.id">
      <span class="badge">person: {{item.name}}</span>
      <div>{{item.content}}</div>
    </li>
  </ul>
</div>
<template id="tmpl">
  <div>
    <div class="form-group">
      <label for="">person:</label>
      <input type="text" class="form-control" v-model="name">
    </div>
    <div class="form-group">
      <label for="">content:</label>
      <textarea class="form-control" v-model="content"></textarea>
    </div>
    <div class="form-group">
      <input type="button" value="add" class="btn btn-primary" @click="add">
    </div>
  </div>
</template>
```

vue实例：

```js
var commentBox = {
  data() {
    return {
      name: '',
      content: ''
    }
  },
  template: '#tmpl',
  methods: {
    add() {
      var tmpl = {
        id: Date.now(),
        name: this.name,
        content: this.content
      }
      var list = JSON.parse(localStorage.getItem('cmts') || '[]')
      console.log(list);
      list.unshift(tmpl)
      localStorage.setItem('cmts', JSON.stringify(list))
      this.name = this.content = ''
      this.$emit('load')
    }
  },
}
var vm = new Vue({
  el: '#app',
  data: {
    list: null
  },
  methods: {
    loadComments() {
      var list = JSON.parse(localStorage.getItem('cmts') || '[]')
      this.list = list
    }
  },
  components: {
    commentBox
  },
  created() {
    this.loadComments()
  }
})
```

### 使用 `this.$refs` 来获取元素和组件

获取DOM节点： 

1. 目标标签中添加 `ref` 属性，自定义名称

   ```html
   <div id="app">
     <input type="button" value="getDOM" @click="getDOM">
     <h3 ref="content">Lorem ipsum dolor sit amet consectetur adipisicing elit.</h3>
   </div>
   ```

2. 在vue 实例中使用 `this.$refs.自定义名称.innerText`

   ```js
   methods: {
     getDOM() {
       console.log(this.$refs.content.innerText);
     }
   }
   ```

获取组件的数据和方法：
`this.$refs.自定义名称.数据名 / 方法名()`