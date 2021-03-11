# React_App

## 环境安装

> 使用 create-react-app 安装 React app

1. 创建项⽬：

    - `npx create-react-app my-app`

2. 打开项⽬：

    - `cd my-app`

3. 启动项⽬：

    - `npm start`

4. 初始化 git:

    - `git add .`
    - `git commit -m "init"`

5. 暴露配置项：

    - `npm run eject`

## JSX

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
// import './index.css';
import styles from './index.module.css'; // .app .logo { width: 100px; }  (css模块化)
import logo from './logo192.png';

const name = 'this.is zf';

const obj = {
  foo: 'bar',
  foz: 'baz',
};

const formatName = (name) => {
  return name.foo + ',' + name.foz;
};

const greet = <div>zf</div>;

const show = true; // 条件示例

const a = [1, 2, 3]; // 循环示例

const jsx = (
  <div className={styles.app}>
    hello {name}
    <div>{formatName(obj)}</div>
    {greet}
    {show ? greet : 'login'}
    {show && greet}
    <ul>
   {a.map((item) => (
    <li key={item}>{item}</li>
   ))}
  </ul>
  <img
      src={logo}
      alt="logo"
      // className="logo"
      className={styles.logo} // css模块化
      // style={{ width: '50px', height: '50px' }} 内联写法，使用对象表示
  />
 </div>
);

ReactDOM.render(jsx, document.getElementById('root'));
```

## 生命周期

- 已废除的三个生命周期
  - componentWillMount
  - componentWillReceiveProps
  - componentWillUpdate
- 需要使用需要加 `UNSAFE_`前缀
- 做老项目兼容时，可使用命令批处理 `npx react-codemod rename-unsafe-lifecycles <path>`（path 批处理路径，不写则项目根目录下所有文件）
  - 使用命令前 git 需要提交一次

## umi

### 安装

1. 创建项目文件夹
2. `yarn create umi`

   1. `ant-design-pro`
   2. `pro v4`
   3. `js`
   4. `simple`(精简版)

### 基本使用

1. 创建页面

   - `umi g page about/index --less`

     - 在 pages 目录下创建 `index.js` `index.less` 两个文件

2. 配置 基础路由

   - 在 `/config/routes.js` 文件中
   - `[0].routes.[1].routes` 中添加路由
     - `{path: '/about',component: './about/index'}`

3. 配置 侧边栏

   - 在上一步添加的路由配置中，再添加 `name`,`icon` 两个字段即可
   - 即：`{ name: 'more', icon: 'table', path: '/about', component: './about/index' }`
     - `name` 字段需要达到国际化响应的效果
     - 在 `/locales/zh-CN/menu.js` 中 添加 `menu. + 自定义的name值`即可
     - 即 `'menu.about': '关于',`

### 约定式路由

1. 配置

   - 动态传参：
     - `umi g page product/[id] --less`
     - `umi g page product/index --less`
       - `/config/routes.js` 添加
         - `{ path: '/product/:id', component: './product/[id]' },` (必须传参)
         - `{ path: '/product/:id', component: './product/index' },`

   - 可选动态传参：
     - `umi g page productDetail/[id$] --less`
     - `umi g page productDetail/index --less`
       - `/config/routes.js` 添加
         - `{ path: '/productDetail/:id?', component: './productDetail/[id$]' },` (可传可不传)
         - `{ path: '/productDetail/:id?', component: './productDetail/index' },`

2. 使用传参

```jsx
export default function Page(props) {
  // 动态路由 props 上有 context（框架进行的传值）
  console.log(props);
  const { id } = props.match.params;
  return (
    <div>
      <h1 className={styles.title}>Page product/index</h1>
      <p>{id}</p>
    </div>
  );
}
```

_ps. 由于 umi3 最新的版本将 routes 单独抽离出来一个文件，_
命令行动态生成 路由 的功能 已经失效
约定式路由也同样不会在配置文件自动生成
故. 上面所做的按约定式的方式生成的页面，可以按普通方式生成，只要 路由配置合法即可。

### 嵌套路由

1. 创建

   - `umi g page ofLayout/_layout`
   - `umi g page ofLayout/index`

2. 路由配置

    ```js
      {
        path: '/ofLayout',
        component: './ofLayout/_layout',
        routes: [
          {
            path: '/ofLayout/index',
            component: './ofLayout/index',
          },
        ],
      },
    ```

3. _layout 文件配置

    ```jsx
      export default function Page(props) {
        return (
          <div>
            <h1 className={styles.title}>Page ofLayout/_layout</h1>
            {props.children}
          </div>
        );
      }
    ```

### 页面跳转

```jsx
import { Button } from 'antd';
import { history, Link } from 'umi';
import React from 'react';

export default function Page() {
  return (
    <div>
      <h1 className={styles.title}>Page about/index</h1>

      {/* 命令式 */}
      <Button
        type="primary"
        onClick={() => {
          history.push('/more');
        }}
      >
        go more
      </Button>

      {/* 声明式 */}
      <Link to="/productDetail">to productDetail</Link>
    </div>
  );
}
```

_ps. 在 umi 3.x 中_，使用 history 取代 router，Link 的导入方式也发生的变化.

## antd 修改默认样式

> 使用 :global() 的方式修改 antd 默认样式，类似在 vue 中使用 /deep/

```less
.moreForm { // className 自定义类名
  display: flex;

  :global(.ant-form-item) { // antd 封装后的类名
    margin-right: 10px;
  }
}
```

_ps. 同样可以在 global.less 中_ 直接使用 antd 封装后的类名 修改默认样式，由于该样式挂载至全局，可能造成局部样式的紊乱，除非全局样式，一般不在 global.less 修改antd 默认样式
