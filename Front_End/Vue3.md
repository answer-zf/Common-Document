# Vue 3.0

## 回顾

### MVVM

-   M(数据模型) 通过响应的方式 进行数据绑定到 V(视图)中
-   在 V 中，用户通过事件反作用事件修改 M
-   通过 vue这个中间层(VM) 做桥梁，避免用户直接接触 DOM

### 生命周期

-   示例：异步获取列表数据

```js
    // 模拟异步数据调用
    function getCourses() {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve(['zf', 'zf'])
            }, 2000);
        })
    }
    const app = new Vue({
        // created钩子中调用接口
        async created() {
            // 组件实例已创建，由于为挂载，DOM 不存在
            const courses = await getCourses()
            this.courses = courses
        }
    })
```

-   生命周期演示

```html
<body>
    <div id="demo">
        <h1>初始化流程</h1>
        <p>{{foo}}</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12"></script>
    <script>
        // 创建实例
        const app = new Vue({
            el: '#demo',
            data: {
                foo: 'foo'
            },
            beforeCreate() { console.log('beforeCreate') },
            created() { console.log('created ' + this.$el) },
            beforeMount() { console.log('beforeMount') },
            mounted() {
                setTimeout(() => {
                    this.foo = 'foooooo'
                }, 2000);
                console.log('mounted ' + this.$el)
            },
            beforeUpdate() { console.log('beforeUpdate') },
            updated() { console.log('updated') },
        });
    </script>
</body>
```

-   场景分析

```javascript
{
    beforeCreate(){} // 执行时组件实例还未创建，通常用于插件开发中执行一些初始化任务
    created(){} // 组件初始化完毕，各种数据可以使用，常用于异步数据获取
    beforeMount(){} // 未执行渲染、更新，dom未创建
    mounted(){} // 初始化结束，dom已创建，可用于获取访问数据和dom元素
    beforeUpdate(){} // 更新前，可用于获取更新前各种状态
    updated(){} // 更新后，所有状态已是最新
    beforeDestroy(){} // 销毁前，可用于一些定时器或订阅的取消
    destroyed(){} // 组件已销毁，作用同上
}
```

### 组件

#### 父组件向子组件传参
    
    -   通过属性传参
    -   子组件通过props接收

```javascript
    // html: <course-list :courses="courses"></course-list>
    Vue.component('course-list', {
        data() {
            return {
                selectCourse: '',
            }
        },
        props: {
            courses: {
                type: Array,
                default: []
            }
        },
        template: `
        <div>
            <h2 v-bind:title="title">{{title}}</h2>
            <p v-if="courses.length == 0">none</p>
            <div v-for="c in courses" :key="c.id" :style="{backgroundColor: selectCourse === c ? '#ddd':'transparent'}">
                <div>{{ c }}</div>
            </div>
        </div>
        `
    })

    const app = new Vue({
        el: '#app',
        data() {
            return {
                title: 'value',
                course: '',
                courses: [],
                totalcount: 0
            }
        },
    })
```

#### 子组件向父组件传参(`$emit` 自定义事件)

    -   子组件 通过 $emit 自定义事件（第二个参数开始 传参） 并触发
    -   父组件 监听 $emit 自定义事件

> 当子组件需要和父级组件进行通信，可以派发并监听自定义事件。

```javascript
    // html: <course-add @add-course="addCourse"></course-add>
    Vue.component('course-add', {
        data() {
            return {
                course: ''
            }
        },
        template: `
        <div>
            <input type="text" @keydown.enter="addCourse" v-model="course">
        </div>
        `,
        methods: {
            addCourse() {
                // 派发事件 通知父组件做新增（事件命名使用 - 不使用 驼峰）
                this.$emit('add-course', this.course)
                this.course = ''
            },
        },
    })

    const app = new Vue({
        el: '#app',
        data() {
            return {
                courses: [],
            }
        },
        methods: {
            addCourse(course) {
                this.courses.push(course)
            }
        }
    })
```

#### 在组件上使用 v-model （双向绑定）

> 将数据存储在 父组件 内部 维护，子组件负责修改

##### 前提 v-model 的实现

> v-model 即 语法糖

v-model="value_"

1.  @input="value_=$event" $event 即用户输入的值
2.  :value="value_"

##### 组件实现

```javascript
    // <course-add @add-course="addCourse" v-model="course"></course-add>
    Vue.component('course-add', {
        // 接收父组件传递value，不需要额外维护course
        props: ['value'],
        template: `
        <div>
            <input type="text" @keydown.enter="addCourse" :value='value' @input="onInput">
        </div>
        `,
        methods: {
            addCourse() {
                // 派发事件 通知父组件做新增
                // 派发事件不再需要传递数据
                this.$emit('add-course')
            },
            onInput(e) {
                this.$emit('input', e.target.value)
            }
        },
    })

    const app = new Vue({
    el: '#app',
    data() {
        return {
            course: '',
            courses: []
        }
    }
    methods: {
        addCourse() {
            this.courses.push(this.course)
            this.course = ''
        }
    }
})
```

#### 内容分发 （插槽）

> 通过使用vue提供的 <slot> 元素可以给组件传递内容

```javascript
// 方法1. <message :show="show" @close="show=$event">xxxxxxxxxxx</message>
// 方法2. 使用 sync 修饰符，默认自定义事件 @update:value_="value_ = $event" 简化操作，没有特殊操作省略
//    <message :show.sync="show">xxxxxxxxxxx</message>

Vue.component('message', {
    props: ['show'],
    template: `
        <div class="message-box" v-if="show">
            <!-- 通过 slot 插槽获取 传入内容 -->
            <slot></slot>
            // 方法1 
            <span class="message-box-close" @click="$emit('close',false)">x</span>
            // 方法2 
            <span class="message-box-close" @click="$emit('update:show',false)">x</span>
        </div>
    `
})

const app = new Vue({
    el: '#app',
    data() {
        return {
            course: '',
            courses: [],
            show: false,
        }
    },
    methods: {
        addCourse() {
            this.courses.push(this.course)
            this.course = ''
            this.show = true
        }
    }
})

```

##### 具名插槽

```html
<message :show.sync="show">
    <!-- 命名为 title 插槽内容 -->
    <template v-slot:title>
        <h2>。。。。。。。。</h2>
    </template>
    <!-- 默认插槽内容 v-slot:default 可省略 -->
    <template v-slot:default>
        default slot content
    </template>
</message>

<script>
    Vue.component('message', {
        props: ['show'],
        template: `
            <div class="message-box" v-if="show">
                <!-- 具名插槽 没有提供内容显示 默认内容-->
                <slot name="title"> 默认内容 </slot>
                <!-- 通过 slot 插槽获取 传入内容 -->
                <slot></slot>
                <span class="message-box-close" @click="$emit('update:show',false)">x</span>
            </div>
        `
    })
    //...
</script>
```

##### 作用域插槽

> 插槽内容 都是由 父组件 提供 ，想要在插槽使用子组件的内容

```html
    <message :show.sync="show">
        <!-- 命名为 title 插槽内容 -->
        <template v-slot:title="slotProps">
            <h2>{{ slotProps.title }}</h2>
        </template>
        <!-- 默认插槽内容 v-slot:default 可省略 -->
        <template v-slot:default>
            default slot content
        </template>
    </message>
    <script>
        Vue.component('message', {
            props: ['show'],
            template: `
                <div class="message-box" v-if="show">
                    <!-- 具名插槽 -->
                    <slot name="title" title="from message component content"> 默认内容 </slot>
                    <!-- 通过 slot 插槽获取 传入内容 -->
                    <slot></slot>
                    <span class="message-box-close" @click="$emit('update:show',false)">x</span>
                </div>
            `
        })
    </script>
```

#### 组件化

> 组件是可复用的 Vue 实例，组件是VueComponent的实例，继承自Vue
> 软件工程中原则的践行，高内聚，低耦合，增强程序的复用性、可维护性和可测试性

-   使用场景

    -   通用组件：实现最基本的功能，具有通用性、复用性，例如按钮组件、输入框组件、布局组件等
    -   业务组件：它们完成具体业务，具有一定的复用性，例如登录组件、轮播图组件。
    -   页面组件：组织应用各部分独立内容，需要时在不同页面组件间切换，例如列表页、详情页组件


-   本质
    -   vue中的组件经历如下过程
        -   组件配置 => VueComponent实例 => render() => Virtual DOM=> DOM
    -   组件的本质是产生虚拟DOM

### API

#### 数据相关API

##### Vue.set / Vue.delete

> 向响应式对象中 添加/删除 一个属性，并确保这个新属性同样是响应式的，且触发视图更新。

-   `Vue.set(target, propertyName/index, value)`

    -   target: 需要修改的对象
    -   propertyName/index : 对象的key
    -   value: 值

-   `Vue.delete(target, propertyName/index)`

```javascript
// <input type="text" v-model.number="price" @keydown.enter="batchUpdate">
const app = new Vue({
    el: '#app',
    data() {
        return {
            course: '',
            courses: [{ name: 'zf' }, { name: 'zf' }],
            price: 0
        }
    },
    methods: {
        batchUpdate() {
            this.courses.forEach(c => {
                // c.price = this.price  数据已改，界面没有响应式更新。
                // Vue.set(c, 'price', this.price) 
                this.$set(c, 'price', this.price) // 也可以使用 同名实例方法  Vue.delete 也同理 this.$delete()
            });
        }
    }
});
```

#### 事件相关API

##### vm.$on 

> 监听当前实例上的自定义事件。事件可以由 vm.$emit 触发。回调函数会接收所有传入事件触发函数的额外参数。

```javascript
// 即 模板中的 @click ... 的 编程写法
vm.$on('test', function (msg) { // @test=" .. "
    console.log(msg) 
})
```

##### vm.$emit

> 触发当前实例上的事件。附加参数都会传给监听器回调。

##### 事件总线

> 通过在Vue原型上添加一个Vue实例作为事件总线，实现组件间相互通信，而且不受组件间关系的影响

`Vue.prototype.$bus = new Vue()`

> 这样做可以在任意组件中使用 this.$bus 访问到该Vue实例

```html
<!--给之前新增成功消息添加.success-->
<message :show.sync="show" class="success">...</message>
<!--新增警告提示窗-->
<message :show.sync="showWarn" class="warning">...</message>
```

```javascript
const app = new Vue({
    data() {
        return {
            // 控制警告信息显示状态
            showWarn: false,
        }       
    },
    methods: {
        addCourse() {
            // 增加输入校验
            if (this.course) {
                // ...  
                this.show = true
            } else {
            // 提示警告信息
                this.showWarn = true
            }
        }
    },
})
```

**功能实现**

```javascript
// 弹窗组件
Vue.component('message', {
    // ...
    // 监听关闭事件
    props: ['show'],
    template: `
        <div class="message-box" v-if="show">
            <!-- 具名插槽 -->
            <slot name="title" title="from message component content"> 默认内容 </slot>
            <!-- 通过 slot 插槽获取 传入内容 -->
            <slot></slot>
            <span class="message-box-close" @click="$emit('update:show',false)">x</span>
        </div>
    `,
    mounted () {
        this.$bus.$on('message-close', () => {
            this.$emit('update:show', false)  // 等价于 批处理 click 事件
        });
    },
})
```

```html
<!-- 派发关闭事件 -->
<div class="toolbar">
    <button @click="$bus.$emit('message-close')">清空提示框</button>
</div>
```

##### vm.$once

> 监听一个自定义事件，但是只触发一次。一旦触发之后，监听器就会被移除。 -> 与 $on 唯一的区别

##### vm.$off

-   移除自定义事件监听器。
    -   如果没有提供参数，则移除所有的事件监听器；
    -   如果只提供了事件，则移除该事件所有的监听器；
    -   如果同时提供了事件与回调，则只移除这个回调的监听器。

#### 组件或元素引用

##### ref和vm.$refs（操作 DOM）

-   ref 被用来给元素或子组件注册引用信息。
-   引用信息将会注册在父组件的 $refs 对象上。
-   如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素（直接操作 DOM）
-   如果用在子组件上，引用就指向组件实例

```html
<input type="text" ... ref="inp">
<script>
    mounted(){
        // 设置输入框焦点
        this.$refs.inp.focus()
    }
</script>
```

**注意：**

-   ref 是作为渲染结果被创建的，在初始渲染时不能访问它们
-   $refs 不是响应式的，不要试图用它在模板中做数据绑定
-   当 v-for 用于元素或组件时，引用信息将是包含 DOM 节点或组件实例的数组。

### 动画

> transition组件会为嵌套元素 自动添加class，可用于做css过度动画

```html
<style>
/* 定义过度动画 */
.fade-enter-active,
.fade-leave-active {
    transition: opacity .5s;
}
.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
<script>
Vue.component('message', {
    // 使用transition组件应用过度动画
    template: `
    <transition name="fade">
    ...
    </transition>
    `,
})
</script>
```

1.  v-enter ：定义进入过渡的开始状态。在元素被插入之前生效，在元素被插入之后的下一帧移除。
2.  v-enter-active ：定义进入过渡生效时的状态。在元素被插入之前生效，在过渡/动画完成之后移除.
3.  v-enter-to : 定义进入过渡的结束状态。在元素被插入之后下一帧生效 (与此同时 v-enter 被移除)，在过渡/动画完成之后移除。
    -   `.fade-enter-to { opacity: 1; }`
4.  v-leave : 定义离开过渡的开始状态。在离开过渡被触发时立刻生效，下一帧被移除。
    -   `.fade-leave { opacity: 1; }`
5.  v-leave-active ：定义离开过渡生效时的状态。在整个离开过渡的阶段中应用，在离开过渡被触发时立刻生效，在过渡/动画完成之后移除。这个类可以被用来定义离开过渡的过程时间，延迟和曲线函数。
6.  v-leave-to : 定义离开过渡的结束状态。在离开过渡被触发之后下一帧生效 (与此同时 v-leave 被删除)，在过渡/动画完成之后移除。

#### 使用CSS动画库

> 通过自定义过度类名可以有效结合Animate.css这类动画库制作更精美的动画效果。

[自定义过度](https://cn.vuejs.org/v2/guide/transitions.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E8%BF%87%E6%B8%A1%E7%9A%84%E7%B1%BB%E5%90%8D)

-   引用
    -   `<link href="https://cdn.jsdelivr.net/npm/animate.css@3.5.1" rel="stylesheet" type="text/css">`

-   使用
    -   `<transition enter-active-class="animated bounceIn" leave-active-class="animated bounceOut">`

#### JavaScript 钩子

-   可以在<transition>属性中声明 JavaScript 钩子，使用JS实现动画。

```html
<script
src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.2.3/velocity.min.js">
</script>
<script>
    Vue.component('message', {
        template: `
        <transition name="fade"
            :css="false" // 禁用css
            @before-enter="beforeEnter"
            @enter="enter"
            @before-leave="beforeLeave"
            @leave="leave">
        </transition>
        `,
        methods: {
            beforeEnter(el) {
                el.style.opacity = 0
            },
            enter(el, done) {
                Velocity(el, { opacity: 1 }, { duration: 500, complete: done })
            },
            beforeLeave(el) {
                el.style.opacity = 1
            },
            leave(el, done) {
                Velocity(el, { opacity: 0 }, { duration: 500, complete: done })
            }
        },
    })
</script>
```

### 可复用

#### 过滤器

> Vue.js 允许你自定义过滤器，可被用于一些常见的文本格式化。过滤器可以用在两个地方：双花括号插 值和 v-bind 表达式 (后者从 2.1.0+ 开始支持)。过滤器应该被添加在 JavaScript 表达式的尾部，由“管 道”符号指示

```javascript
// {{ c.price | currency('RMB') }}
// 全局过滤器
Vue.filter('currency',function (value) {
    return value
})
// 局部过滤器
filters: {
    currency(value, symbol = '￥') {
        return symbol + value;
    }
}
```

#### 自定义指令

> 对普通 DOM 元素进行底层操作，用 自定义指令

-  按钮权限控制
```javascript
// <button v-permission="'admin'"></button>
const role = 'user'
Vue.directive('permission', {
    inserted(el, binding) {
        if (role !== binding.value) {
            el.parentElement.removeChild(el)
        }
    }
})
```

#### 渲染函数

> Vue 推荐使用模板创建 HTML。然而需要 JavaScript 的 完成编程的能力，用渲染函数

```javascript
render: function (createElement) {
    // createElement函数返回结果是VNode
    return createElement(
        tag, // 标签名称
        data, // 传递数据
        children // 子节点数组
    )
}
```

-   使用实例

```html
<heading level="1" :title="title">
    {{title}}
</heading>
```

```javascript
Vue.component('heading', {
    props: {
        level: {
            type: String,
            required: true
        }
    },
    // 返回 createElement 的 VNODE
    render(h) {
        console.log(this.$slots.default);
        return h(
            'h' + this.level, // tagname 即标签名
            // 动态添加的属性，不处理，vue默认行为添加到根节点上
            this.$slots.default
        )
    }
})
```

##### 虚拟DOM

> Vue 通过建立一个虚拟 DOM 来追踪自己要如何改变真实 DOM。

```javascript
const vnode = h(
    'h' + level,
    { attrs: { title: this.title } }, // 之前省略了title的处理
    this.$slots.default
)
console.log(vnode);
```

##### createElement 参数

[createElement-参数](https://cn.vuejs.org/v2/guide/render-function.html#createElement-%E5%8F%82%E6%95%B0)

[深入数据对象](https://cn.vuejs.org/v2/guide/render-function.html#%E6%B7%B1%E5%85%A5%E6%95%B0%E6%8D%AE%E5%AF%B9%E8%B1%A1)


-   示例

```html
<!-- 渲染的目标结果 <h2> <svg>
        <use xlink:href="#icon-CART"></use>
    </svg> </h2> -->
<heading :title="title" level="1" icon="CART">
    {{title}}
</heading>
```

```javascript
Vue.component('heading', {
    props: {
        level: { type: String, required: true },
        title: { type: String, default: '' },
        icon: { type: String }
    },
    render(h) {
        // 子节点数组
        let children = []
        if (this.icon) {
            children.push(h(
                // 标签
                'svg',
                // 数据
                { class: 'icon' },
                // 子节点
                [h( 'use', { attrs: { 'xlink:href': '#icon-' + this.icon } } )]
            ))
        }
        children = children.concat(this.$slots.default)
        const vnode = h(
            'h' + this.level, // tagname 即标签名
            // 动态添加的属性，不处理，vue默认行为添加到根节点上
            { attrs: { title: this.title } },
            children
        )
        return vnode
    }
})
```

##### 函数式组件

> 组件没有管理任何状态，也没有监听任何传递给它的状态，也没有生命周期方法时，可以将组件标记为 functional ，这意味它无状态 (没有响应式数据)，也没有实例 (没有 this 上下文)。

-   优化上述示例

```javascript
Vue.component('heading', {
    functional: true, // 函数式组件
    props: { level: { type: String, required: true }, title: { type: String, default: '' }, icon: { type: String } },
    render(h, context) {
        // 子节点数组
        let children = []
        // 属性获取
        const { icon, title, level } = context.props
        if (icon) {
            children.push(h(
                // 标签
                'svg',
                // 数据
                { class: 'icon' },
                // 子节点
                [h( 'use', { attrs: { 'xlink:href': '#icon-' + icon } } )]
            ))
        }

        children = children.concat(context.children)

        const vnode = h(
            'h' + level, // tagname 即标签名
            // 动态添加的属性，不处理，vue默认行为添加到根节点上
            { attrs: { title: title } },
            children
        )
        return vnode
    }
})
```

#### 混入

**组件逻辑复用**

[混入](https://cn.vuejs.org/v2/guide/mixins.html#ad)

#### 插件

[插件](https://cn.vuejs.org/v2/guide/plugins.html#ad)

-   示例：重构 heading 使其变成插件

```javascript
// 在使用的地方引入即可
// <script src="plugins/heading.js"></script>
// 声明插件（创建） /plugins/heading.js
const myPlugin = {
    install(Vue, options) {
        Vue.component('heading', {
            functional: true, // 函数式组件
            props: {
                level: {
                    type: String,
                    required: true,
                },
                title: {
                    type: String,
                    default: '',
                },
                icon: {
                    type: String,
                },
            },
            render(h, context) {
                // 子节点数组
                console.log(context)

                let children = []
                // 属性获取
                const { icon, title, level } = context.props
                if (icon) {
                    children.push(
                        h(
                            // 标签
                            'svg',
                            // 数据
                            { class: 'icon' },
                            // 子节点
                            [
                                h('use', {
                                    attrs: {
                                        'xlink:href': '#icon-' + icon,
                                    },
                                }),
                            ]
                        )
                    )
                }

                children = children.concat(context.children)

                const vnode = h(
                    'h' + level, // tagname 即标签名
                    // 动态添加的属性，不处理，vue默认行为添加到根节点上
                    { attrs: { title: title } },
                    children
                )
                return vnode
            },
        })
    },
}
if (typeof window !== 'undefined' && window.Vue) {
    // 使用插件
    window.Vue.use
}

```

### vue-cli

#### 快速原型开发

-   安装：`npm install -g @vue/cli-service-global`
-   使用：vue serve filename.vue

```bash
# 1. ~/.vuerc
{
  "useTaobaoRegistry": true,
  "packageManager": "npm"
}

```

#### 创建项目

-   vue create project_name

#### 添加插件

-   vue add router

#### 资源路径

> 当你在 JavaScript、CSS 或 *.vue 文件中使用相对路径 (必须以 . 开头) 引用一个静态资源时，该资源将被webpack处理。

##### 转换规则

-   如果 URL 是一个绝对路径 ，它将会被保留不变(存放在 pulic 文件夹下，webpack 不会处理)
    
    -   文件存放在 public 下，webpack 不会处理，即 public 就是根目录
    -   `<img alt="Vue logo" src="/assets/logo.png">`

-   如果 URL 以 @ 开头, Vue CLI 默认会设置一个指向 src 的别名 @ 。即根目录是 src
    -   `import CourseList from '@/components/CourseList.vue'`

##### 何时使用 public 文件夹

-   通过 webpack 的处理的好处（使用相对路径）：
    1.  脚本和样式表会被压缩且打包在一起，从而避免额外的网络请求。
    2.  文件丢失会直接在编译时报错，而不是到了用户端才产生 404 错误。
    3.  最终生成的文件名包含了内容哈希，因此你不必担心浏览器会缓存它们的老版本。

-   使用 public 文件夹的好处（使用绝对路径）
    1.  需要在构建输出中指定一个固定的文件名字。
    2.  有上千个图片，需要动态引用它们的路径。
    3.  有些库可能和 webpack 不兼容，除了将其用一个独立的 `<script>` 标签引入没有别的选择。


##### 使用public文件夹的注意事项

-   如果应用没有部署在域名的根部时，需要为 URL 配置 publicPath 前缀

```javascript
// vue.config.js
module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
        ? '/cart/'
        : '/'
}
```

-   在 public/index.html 等通过 html-webpack-plugin 用作模板的 HTML 文件中，需要通过 <%= BASE_URL %> 设置链接前缀：

    -   `<link rel="icon" href="<%= BASE_URL %>favicon.ico">`

-   在模板中，先向组件传入BASE_URL：

```javascript
data () {
    return {
        publicPath: process.env.BASE_URL
    }
}
```

-   然后在 组件模板（template）中使用：

```html
<img :src="`${publicPath}my-image.png`">
```

#### css

-   如果创建项目时没有选择需要的预处理器（Sass/Less/Stylus），则需手动安装相应loader

```bash
# Sass
npm install -D sass-loader node-sass
# Less
npm install -D less-loader less
# Stylus
npm install -D stylus-loader stylus
```

```html
<style scoped lang="scss">
    $color: #42b983;
    a {
        color: $color;
    }
</style>
```

#### 自动化导入样式

> 自动化导入样式文件 (用于颜色、变量、mixin等)，可以使用 style-resources-loader。

-   安装

```bash
npm i -D style-resources-loader
```

-   配置

```javascript
// 1.  创建 @styles/imports.scss 文件，在该文件 预定义需要导入的内容
// 2.  配置 vue.config.js 文件
//       即 在使用之初，先将imports.scss 文件载入，故在所有文件中可以直接使用预定义的变量、定义..
const path = require('path')
function addStyleResource(rule) {
    rule.use('style-resource')
        .loader('style-resources-loader')
        .options({
            patterns: [path.resolve(__dirname, './src/styles/imports.scss')],
        })
}
module.exports = {
    chainWebpack: (config) => {
        const types = ['vue-modules', 'vue', 'normal-modules', 'normal']
        types.forEach((type) =>
            addStyleResource(config.module.rule('scss').oneOf(type))
        )
    },
}
```

#### Scoped CSS

> 当 `<style>` 标签有 scoped 属性时，它的 CSS 只作用于当前组件中的元素。

-   原理

```html
<style scoped>
    .red {
        color: red;
    }
</style>

<!-- 原理如下: 通过使用 PostCSS 来实现转换-->

<template>
    <div class="red" data-v-f3f3eg9>hi</div>
</template>
<style>
    .red[data-v-f3f3eg9] {
        color: red;
    }
</style>
```

-   深度作用选择器：使用 >>> 操作符可以使 scoped 样式中的一个选择器能够作用得“更深”，例如影响子组件

-   Sass 之类的预处理器无法正确解析 >>> 。这种情况下你可以使用 /deep/ 或 ::v-deep 操作符取而代之

#### 
