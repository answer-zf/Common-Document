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

-   父组件向子组件传参
    -   props

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

-   子组件向父组件传参
    -   `$emit` 自定义事件

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