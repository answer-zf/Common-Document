# React_App

## 环境安装

> 使用 create-react-app 安装 React app

1.  全局安装 `create-react-app`

    -   `npm install -g create-react-app`

2.  创建项⽬：

    -   `npx create-react-app my-app`

3.  打开项⽬：

    -   `cd my-app`

4.  启动项⽬：

    -   `npm start`

5.  初始化 git:

    -   `git add .`
    -   `git commit -m "init"`

6.  暴露配置项：

    -   `npm run eject`

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

-   已废除的三个生命周期
    -   componentWillMount
    -   componentWillReceiveProps
    -   componentWillUpdate
-   需要使用需要加 `UNSAFE_`前缀
-   做老项目兼容时，可使用命令批处理 `npx react-codemod rename-unsafe-lifecycles <path>`（path 批处理路径，不写则项目根目录下所有文件）
    -   使用命令前 git 需要提交一次
