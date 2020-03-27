# 弹性布局（display:flex）

## 方向：

- flex-direction
   - 默认值：  row		水平向左
   - 常用值：	 column		垂直向下
   - 其他值：  
     - row-reverse			水平向左
     - column-reverse         垂直向下

## 宽度均分

- flex: 1;

## 换行：

- flex-wrap
   - 默认值：  nowrap		不换行，若超出则等比缩小（ flex-shrink=1 ）
   - 常用值：	 wrap		换行，第一行在上方。
   - 其他值：  wrap-reverse			换行，第一行在下方。

## 对齐：

- justify-content
  - 默认值：  flex-start			左对齐
  - 常用值：  
    - flex-end			右对齐
    - center				居中
    - space-between  	两端对齐
  - 其他值：  space-around   	两侧等距
        
- align-items
  - 默认值：  flex-start			上对齐
  - 常用值：  
    - flex-end			下对齐
    - center				居中
  - 其他值：
    - baseline			文字基线对其
    - stretch   			占满容器

