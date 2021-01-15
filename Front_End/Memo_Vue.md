# Vue 相关 备忘

## Vue

### Vuex

-   mapState,mapMutations... (vuex 映射)

    -   `...mapMutations('user', ['updateIsAdmin']),`
    -   'user': modules/user.js
    -   'updateIsAdmin': 模块中 mutations项中的方法名
    -   mapState 同理

### dialog

-   resetField 的坑

    -   问题：重置到最近一次提交，快速连续提交会出问题(连点)

    -   解决：在 dialog 上加 `destroy-on-close` 属性，用于重置验证信息，或者使用 v-if

    -   `destroy-on-close` 关闭时销毁 Dialog 中的元素

### table

-   表头与内容错位

```css
body .el-table th.gutter{
  display: table-cell!important;
}

body .el-table colgroup.gutter{
  display: table-cell!important;
}
```

## JS

### 判断类型

`Object.prototype.toString.call(value)`

### 数组

#### ES 5

-   filter()

    -   创建一个新数组，新数组中的元素是通过检查指定数组中符合条件的所有元素(过滤)

-   map()

    -   创建一个新数组，新数组中的元素是调用一次提供的函数后的返回（对每个元素的操作后的返回）

-   判断 数组的所有成员是否满足指定的条件

    -   some() 只要其中一个为true，就会返回true `一真即真`
    -   every() 必须所有都返回true才会返回true `一假即假`

#### 数组扁平化(ES10)

> 将嵌套的数组变成一维数组的过程

-   `arr.flat()`

### 字符串

#### ES 7

-   padStart(len,str)

    -   向左填充 str 字符串，使操作字符串长度等于 len

    -   应用 补 0

        -   str1.padStart(2,'0')  // str1 = '5' => '05'

-   padEnd(len,str)

    -   反之，向右

### 异步相关

#### async、await(ES7)

-   提交成功后，立即渲染页面时，不要分在两个函数中写，有异步的问题

## CSS

### 溢出省略隐藏

```css
div{
  /* 单行 */
  text-overflow: ellipsis !important;
  white-space: nowrap !important;
  overflow: hidden !important;

  /* 两行 */
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
}
```

## 项目优化

### 生产阶段 移除 console

-   使用 `babel-plugin-transform-remove-console` babel插件解决

```js
// 项目发布阶段需要用到的 插件数组
const prodPlugins = []
if (process.env.NODE_ENV === 'production') {
  // 在 babel.config.js 按需移除 console
  prodPlugins.push('transform-remove-console')
}

module.exports = {
  presets: ['@vue/cli-plugin-babel/preset'],
  plugins: [
    [
      'component',
      {
        libraryName: 'element-ui',
        styleLibraryName: 'theme-chalk'
      }
    ],
    // 发布产品时候的插件数组
    ...prodPlugins,
    // 路由懒加载
    '@babel/plugin-syntax-dynamic-import'
  ]
}
```

### 配置 生产 开发的入口文件

```js
// vue.config.js
module.exports = {
  chainWebpack: config => {

    // 发布模式
    config.when(process.env.NODE_ENV === 'production', config => {

      config
        .entry('app')
        .clear()
        .add('./src/main-prod.js')

      // 将 import 引入的第三方包，改为 cdn
      config.set('externals', {
        vue: 'Vue',
        'vue-router': 'VueRouter',
        axios: 'axios',
        echarts: 'echarts',
        nprogress: 'NProgress',
        'element-ui': 'ELEMENT'
      })

      // index.html 添加 cdn
      // main-prod.js 注释 import 引入的第三方包（只注释导入的 css）
      // <!-- css -->
      // <!-- nprogress-->
      // <link rel="stylesheet" href="https://cdn.staticfile.org/nprogress/0.2.0/nprogress.min.css">
      //
      // <!-- element-ui -->
      // <link rel="stylesheet" href="https://cdn.staticfile.org/element-ui/2.14.0/theme-chalk/index.min.css">
      //
      // <!-- js -->
      // <script src="https://cdn.staticfile.org/vue/2.6.11/vue.min.js"></script>
      // <script src="https://cdn.staticfile.org/vue-router/3.2.0/vue-router.min.js"></script>
      // <script src="https://cdn.staticfile.org/axios/0.20.0/axios.min.js"></script>
      // <script src="https://cdn.staticfile.org/echarts/4.9.0-rc.1/echarts.min.js"></script>
      // <script src="https://cdn.staticfile.org/nprogress/0.2.0/nprogress.min.js"></script>
      // <script src="https://cdn.staticfile.org/element-ui/2.14.0/index.min.js"></script>

      config.plugin('html').tap(args => {
        // 使用 htmlWebpackPlugin.options.xxx 在 html 调用
        args[0].isProd = true
        args[0].title = '后台管理系统'
        return args
      })

    })

    // 开发模式
    config.when(process.env.NODE_ENV === 'development', config => {
      config
        .entry('app')
        .clear()
        .add('./src/main-dev.js')

      config.plugin('html').tap(args => {
        args[0].isProd = false
        args[0].title = '后台管理系统'
        return args
      })
    })
  }
}
```
