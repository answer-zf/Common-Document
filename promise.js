var fs = require('fs')

var p1 = new Promise(function(resolve, reject) {
  fs.readFile('./data/a.txt', 'utf8', function(err, data) {
    if (err) {
      reject(err)
    } else {
      resolve(data)
    }
  })
})
var p2 = new Promise(function(resolve, reject) {
  fs.readFile('./data/b.txt', 'utf8', function(err, data) {
    if (err) {
      reject(err)
    } else {
      resolve(data)
    }
  })
})
var p3 = new Promise(function(resolve, reject) {
  fs.readFile('./data/c.txt', 'utf8', function(err, data) {
    if (err) {
      reject(err)
    } else {
      resolve(data)
    }
  })
})
p1.then(
  function(data) {
    console.log(data)
    // 当 p1 读取成功的时候
    // 当前函数中 return 的结果就可以在后面的 then 中 function 接收到，故：
    // 当 return 123 后面就接收到 123
    // 没有 return 后面就接收的是 undefined
    // 同理可以 return 一个 Promise 对象
    // 当 return 一个Promise 对象的时候，后续的then中的 方法的第一个参数会作为p2 的 resolve
    return p2
  },
  function(err) {
    console.log(err)
  }
)
  .then(function(data) {
    console.log(data)
    return p3
  })
  .then(function(data) {
    console.log(data)
  })
