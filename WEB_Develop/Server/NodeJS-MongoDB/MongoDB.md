# mongoDB

 https://www.runoob.com/mongodb/mongodb-tutorial.html 

## 关系型数据库和非关系型数据库

### 关系型数据库

表就是关系，或者说表与表之间存在关系

- 所有的关系型数据库都需要通过 `sql` 语言来操作
- 所有的关系型数据库在操作前都需要设计表结构
- 数据表还支持约束
  - 唯一的
  - 主键
  - 默认值
  - 非空

### 非关系型数据库

非常灵活

- 有的非关系型数据库就是key-value 对
- 在MongoDB是长得最像关系型数据库的非关系型数据库
  - 数据库  - > 数据库
  - 数据表  - > 集合（数组）
  - 表记录  - > (文档对象)
- MongoDB 不需要设计表结构
- 可以任意往里面存数据，没有结构性这么一说

## MongoDB数据库基本概念

- 数据库 : 可以有多个数据库
- 集合 : 一个数据库可以有多个集合（表）
- 文档：一个集合中可以有多个文档（表记录）
- 文档结构非常灵活，没有任何限制
- MongoDB非常灵活，不需要想MySQL一样先创建数据库、表、设计表结构
  - 这里只需要，当你需要插入数据的时候，只需要指定往哪个数据库的哪个集合操作就可以
  - 一切都有 MongoDB 来帮你自动完成建库建表的事

```js
{
  qq:{   // 数据库
    users: [   // 集合
      {name: 'zhangsan', age: 16},   // 文档
      {name: 'zhangsan', age: 16},
      {name: 'zhangsan', age: 16},
      {name: 'zhangsan', age: 16},
      ...
    ],
    products: {
      
    }
    ...
  },
  taobao:{
    
  },
  baidu{
    
  }
}
```



## 安装

- 下载
- 安装
- 配置环境变量
- `mongod --version` 测试是否安装成功

## 启动和关闭数据库

启动:

```shell
# mongodb  默认使用执行 mongod 命令所处盘符根目录下 /data/db 作为自己的数据存储目录
# 在第一次执行该命令之前先自己手动新建一个 /data/db
mongod
```

如果需要修改默认数据存储目录，可以

```shell
mongod --dbpath=数据存储目录路径
```

停止：

```shell
在开启服务的控制台，直接 Ctrl+c 即可停止
或者直接关1闭开启服务的控制台
```

## 连接和退出数据库

连接：

```shell
# 该命令默认连接本机的 MongoDB 服务
mongo
```

退出：

```shell
# 在连接状态输入 exit 退出连接
exit
```

## 基本命令

- `show dbs`

  - 查看显示书友数据库

- `db`

  - 查看当前操作的数据库

- `use 数据库名称`

  - 切换到指定数据库（如果没用会新建）

- 插入数据

  ![插入数据](../../../mackdown_UsePic/MongoDB_cmd.png)

## 在 Node 中操作 MongoDB 数据库

### MongoDB

- 使用官方 `MongoDB` 包来操作

  > https://github.com/mongodb/node-mongodb-native

### mongoose

- 使用第三方 mongoose 来操作 MongoDB 数据库

- 第三方包：`mongoose` 基于 MongoDB 官方的 `mongodb` 包再一次做了封装。

  > https://mongoosejs.com/ 



#### 起步：

安装：

```shell
npm i mongoose
```

hello world:

```js
var mongoose = require('mongoose')

// 连接 MongoDB 数据库
mongoose.connect('mongodb://localhost/test', { useMongoClient: true})

// 创建一个模型
// 就是在设计数据库
// MongoDB 是动态的，非常灵活，只需要在代码中设计数据库就可以了
// mongoose 这个包就可以让你的设计编写过程变得非常简单
var Cat = mongoose.model('Cat', { name: String })

// 实例化一个Cat
var kitty = new Cat({ name: 'Zildjian' })

// 持久化保存 Kitty 实例 
kitty.save(function (err) {
  if (err) {
    console.log(err)
  } else {
    console.log('meow')
  }
})
```

