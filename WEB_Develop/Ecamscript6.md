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

