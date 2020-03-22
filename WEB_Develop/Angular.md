# Angular

## 起步

### Step 0. 安装依赖环境

1. 安装 Node.js
2. 安装 npm
3. 安装 Python（ 使用 Python 2 ）
   - https://www.python.org/downloads/release/python-2717/
     - Windows x86-64 MSI installer
   - 确认 Python 环境 python --version
4. 安装 C++ 编译工具

- Angular CLi 在 Windows 上同时依赖 C++ 编译工具。
- 执行下面的命名安装 C++ 编译工具：
  - npm install --global --production windows-build-tools

### Step1. 安装脚手架工具 Angular CLI

#### 安装

```shell
  cnpm i -g @angular/cli
```

#### 确认

```shell
  ng --version
```

### Setp 2. 使用脚手架工具初始化项目

```shell
  ng new my-app
```

> 请特别注意：Angular CLI 在自动生成好项目骨架之后，会立即自动使用 npm 来安装所依赖的 Node 模块，自己手动 Ctrl + C 终止掉，然后进入初始化好的项目根目录使用 cnpm 来安装。

### Step 3. Serve the application

项目目录下：

```shell
  # 或者 npm start
  ng serve
```

> 该命令默认会开启一个服务占用 4200 端口，如果想要修改可以通过 --port 参数来指定，例如 ng serve --port 3000

## 简介

### 目录结构

> https://www.cnblogs.com/nightnight/p/11186387.html

### angular.json 部分配置

```json
{
  "projects": {
    "ng-text": {
      "projectType": "application",
      "schematics": {
        "@schematics/angular:component": {
          "style": "scss"
        }
      },
      "root": "", // 项目根目录
      "sourceRoot": "src", // 源码根目录
      "prefix": "app", // 使用脚手架工具创建组件的自动命名前缀
      "architect": {
        // 自动化命令配置
        "build": {
          // 项目默认生成的配置
          "builder": "@angular-devkit/build-angular:browser",
          "options": {
            "outputPath": "dist/ng-text", // 打包编译结果目录
            "index": "src/index.html", // 单页面
            "main": "src/main.ts", // 模块启动入口
            "polyfills": "src/polyfills.ts", // 用以兼容低版本浏览器不支持的 JavaScript 语法特性
            "tsConfig": "tsconfig.app.json",
            "aot": true,
            "assets": ["src/favicon.ico", "src/assets"], // 存放静态资源目录
            "styles": ["src/styles.scss"], // 全局样式文件
            "scripts": [] // 全局脚本文件
          }
        }
      }
    }
  },
  "defaultProject": "ng-text"
}
```

## TypeScript

### 环境

1. 在线测试编译环境 compiler
   - https://www.typescriptlang.org/play/index.html
2. 本地开发编译环境

```shell
  npm i -g typescript
  # 使用 tsc 文件路径 编译成 js
```

### 语法：

#### 数据类型：

```typescript
// 布尔类型
let isDone: boolean = false

// 数字
let amount: number = 6

// 字符串
let nickname: string = '张三'

// 模板字符串同样兼容
let nickname: string = `Gene`
let age: number = 37
let sentence: string = `Hello, my nickname is ${nickname}.I'll be ${age +
  1} years old next month.`

// 数组 在元素类型后面接上[]
let list: number[] = [1, 2, 3]
let list: string[] = ['z', 'f']
// 使用数组泛型，Array<元素类型>
let list: Array<number> = [1, 2, 3]

// 元组：有不同数据类型的数组
let arr: [number, string] = [1, 'zf'] // 一一对应的关系，不能多，不能少，不能交错

// 对象：
let obj: object = { name: 'zf' } // 一般使用这种方式

let user: {
  // 使用这种方式
  name: string
  age: number
} = {
  name: 'zf',
  age: 8
}
```

##### 特殊情况

**任意类型：**

```typescript
// Any: 任意类型 （少用）
let zfs: any = 'sadf'
zfs = 111
```

**函数中应用**

- 用于函数的形参

```typescript
function add(x: number, y: number): number {
  return x + y
}
let ret: number = add(10, 20)
// viod：表示没有任何类型 -> 空（ 只能用于函数的返回值 ）
function fn(): void {
  console.log('zf')
}
```

**Null 和 Undefined**

- 和 void 相似，它们的本身的类型用处不是很大：

```typescript
// 几乎不用
let u: undefined = undefined
let n: null = null
```

#### 接口

- 重用

```typescript
interface Person {
  name: string
  age: number
}
let xyz: Person = {
  name: 'zddf',
  age: 888
}
```

#### 解构赋值

**数组**

- 数组按照 顺序 解构

```typescript
let arr: number[] = [10, 20]
let [num1, num2, num3] = arr
```

**对象**

- 对象按照 键名 解构

```typescript
let obj: {
  name: string
  age: number
} = {
  name: 'zf',
  age: 18
}
let { name: zf, age } = obj
```

**剩余参数**

```typescript
function sum(...args: number[]): number {
  let ret = 0
  args.forEach(item => {
    ret += item
  })
  return ret
}
sum(1, 2, 3)
```

#### 展开操作符

```typescript
// 数组
let arr1 = [1, 2, 3]
let arr2 = [4, 5, 6]
let arr3 = [...arr1, ...arr2]

// 对象
let obj1 = {
  foo: 'bar'
}
let obj2 = {
  ...obj1,
  name: 'jack'
}
```

#### 类

```typescript
function Person(name: string, age: number) {
  this.name = name
  this.age = age
}
Person.prototype.sayHello = function(): void {
  console.log(this.name, this.age)
}
let p1 = new Person('zhans', 18)
p1.sayHello()
```

```typescript
class Person {
  // ts 要求声明类成员
  name: string
  age: number
  constructor(name: string, age: number) {
    this.name = name
    this.age = age
  }
  sayHello(): void {
    console.log(this.age, this.name)
  }
}
let p1 = new Person('zhans', 18)
p1.sayHello()

// 继承
class Student extends Person {
  constructor(name: string, age: number) {
    // super 就是 父类 构造函数
    super(name, age)
  }
}
```

##### 实例成员访问修饰符

- `public` 默认值 公开的
  - 类的成员默认是对外公开的
- `private` 私有的
  - 用来声明私有成员，只能在类的内部访问，外部访问不到
  - 私有成员 无法继承
- `protected` 受保护的
  - 与 private 类似 私有成员，外部无法直接访问，但可以被继承
- `readonly` 只读的，不允许修改，与 const 定义的常量类似

```typescript
// 类的成员默认是对外公开的
class Person {
  public name: string
  public age: number
  // 可以在声明类成员的同时赋值
  private readonly type: string = 'zf'
  protected foo: string = 'bar'
  public constructor(name: string, age: number) {
    this.name = name
    this.age = age
  }
  public getType() {
    // 在类的内部访问私有成员
    // 在外部无法访问
    return this.type
  }
}

// protected 的成员只能在子类内部访问，不能在子类外部访问
class Student extends Person {
  getFoo() {
    console.log(this.foo)
  }
}

new Student('z', 1).getFoo()
```

```typescript
class Person {
  constructor(public name: string, public age: number) {
    this.name = name
    this.age = age
  }
}
```
