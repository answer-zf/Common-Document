# Ecamscript6



## 数组操作 



### find

方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 undefined

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

every  -- 方法测试一个数组内的所有元素是否都能通过某个指定函数的测试。它返回一个布尔值。 

some  --  方法测试数组中是不是有元素通过了被提供的函数测试。它返回的是一个Boolean类型的值。 

findIndex--  方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 [`undefined`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/undefined)。

includes  --   方法返回数组中满足提供的测试函数的第一个元素的索引。否则返回-1。 

map --  方法创建一个新数组，其结果是该数组中的每个元素都调用一个提供的函数后返回的结果。 

reduce --  方法对数组中的每个元素执行一个由您提供的**reducer**函数(升序执行)，将其结果汇总为单个返回值 