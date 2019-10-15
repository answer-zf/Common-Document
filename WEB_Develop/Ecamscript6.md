# Ecamscript6



## 数组操作 



### find

#### 语法：

```js
arr.find(callback)
```

#### 参数：

callback

在数组每一项上执行的函数，接收 3 个参数：

- `element`  当前遍历到的元素。
- `index`（可选）当前遍历到的索引。
- `array`（可选）数组本身。

#### 返回值：

 数组中第一个满足所提供测试函数的元素的值，否则返回 `undefined`。 

#### 实例：

```js
var array = [5, 12, 8, 130, 44];

var found = array.find(function(item) {
  return item === 130;
});

console.log(found)  // 结果：130
```

 #### 底层原理

```js
// find 接收一个方法作为参数，方法内部返回一个条件
// find 会遍历所有的元素，执行你给定的带有条件返回值的函数
// 符合该条件的元素会作为 find 方法的返回值
// 如果遍历结束还没有符合该条件的元素，则返回 undefined
Array.prototype.myFind = function (conditionFunc) {
  for (var i = 0; i < this.length; i++) {
    if (conditionFunc(this[i], i)) {
      return this[i]
    }
  }
}

var ret = users.myFind(function (item, index) {
  return item.id === 2
})
```

