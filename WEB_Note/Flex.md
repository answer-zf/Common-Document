# 弹性布局（display:flex）

```js

// 方向：

	flex-direction

		默认值：  row		水平向左

		常用值：	 column		垂直向下

		其他值：  row-reverse			水平向左

			     column-reverse         垂直向下

// 换行：

	flex-wrap

		默认值：  nowrap		不换行，若超出则等比缩小（ flex-shrink=1 ）

		常用值：	 wrap		换行，第一行在上方。

		其他值：  wrap-reverse			换行，第一行在下方。

// 对齐：

	justify-content

		默认值：  flex-start			左对齐

		常用值：  flex-end			右对齐
		 		 center				居中
  				 space-between  	两端对齐
                 
		其他值：  space-around   	两侧等距
        
	align-items

		默认值：  flex-start			上对齐

		常用值：  flex-end			下对齐
		 		 center				居中

		其他值：  baseline			文字基线对其
		  		 stretch   			占满容器
                 
// 复合写法：

flex: 0 1 auto;		==>		flex-grow	flex-shrink		flex-basis（比width优先级高）

								拉			缩			   类比宽
                                
                                
```

