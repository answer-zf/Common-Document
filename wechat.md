# 基础

## 类似 vue 
1. 小程序不是运行在浏览器中，没有 BOM DOM 对象
2. 小程序的 JS 有额外的成员
   - App 方法：用于定义应用程序实例对象 （类似 vue）
   - Page 方法：用于定义页面对象 （类似 router）
   - getApp 方法: 用于获取全局应用程序对象
   - getCurrentPages 方法：用于获取当前页面的调用栈(数组， 最后一个就是当前页面)
   - wx 对象： 用来提供核心API
3. 小程序支持 commonJS规范
   - 不支持 exports.xxx 导出
   - 只支持 module.exports

## 事件
### 事件绑定
1. bindtap catchtap
   - bindtap 绑定事件，事件冒泡
   - catchtap 绑定事件，阻止事件冒泡

### 事件传参
1. 使用 data- 属性， 通过调用 e.target.dataset 的方式获取 （类似H5）

## 数据绑定
- 小程序不支持双向数据绑定
> 可以使用 bindinput 监听，this.setData() 方法同步
```js
  data: {
    message: 'initial'
  },
  inputHandle: function(e) {
    this.setData({
      message: e.detail.value
    })
  }
```
```html
  <input value="{{ message }}" bindinput="inputHandle"></input>
  <text>
    {{ message }}
  </text>
```

## API :交互相关

https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html

```js
Page({
  btnToDo: function() {
    // 交互操作组件 必须通过调用API方式使用
    wx.showActionSheet({
      // 显示出来的项目列表
      itemList: ['zf', 'zzz', 'fff', 'ccc'],
      // 点击其中任一项的回调
      success: function(res) {
        // res.cancel 指的是是否点击了取消
        if (!res.cancel) {
          // tapIndex指的是点击的下标
          console.log(res.tapIndex)
        }
      }
    })

    wx.showModal({
      title: '提示',
      content: '这是一个模态弹窗',
      success: function(res) {
        if (res.confirm) {
          console.log('用户点击确定')
        }
      }
    })

    wx.showToast({
      title: '成功',
      // 只支持 success 和 loading
      icon: 'loading',
      duration: 2000
    })
  }
})
```
