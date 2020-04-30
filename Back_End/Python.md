# 常用命令

```bash
$ pwd # 所在工作目录的绝对路径
$ touch ['文件名'] # 创建文件
```

# python 基础

## 基础语法

### 变量

1.  定义：关联一个对象的标识
2.  命名：
    -   必须为字母数或下划线，后面跟着字母，数字，下划线。
    -   不能使用保留关键字
3.  语法：
    -   变量名1 = 变量名2 = 表达式
    -   变量名1，变量名2  =表达式1，表达式2
        -   交换值（Python独有）
        -   变量名1，变量名2  =变量名2，变量名1

#### 数据类型

-   变量没有类型，关联的对象有类型。
-   可以通过 type 方法，判断对象的类型。
-   语法：变量 = type(数据)

1.  None

    -   表示不存在的特殊对象
    -   变量解除绑定

2.  整形 int

    -   整数. 包含正数，负数，0.
    -   字面值：
        -   默认十进制
        -   二进制（0,1）：0b0,0b1,0b10,0b11, 0b100 （使用二进制在前面加0b）
        -   八进制(0-7)：0o0,0o7,0o10（使用八进制在前面加0o）
        -   十六进制(0-9,a(10)-f(15))：0x0,0xa（使用十六进制在前面加0x）
            -   9, a, b, c ,d ,e ,f, 10 (9, 10, 11, 12, 13, 14, 15)
    -   小整数对象池：CPython 中整数-5 到 256，永远存在小整数对象池中，不会释放
        -   对象池：缓存的机制。
        -   使用 `id()`(返回变量存储的对象地址)，在交互式中可以体现，文件式中进行了优化

3.  浮点数 float

    -   小数 (包含正数，负数，0.0)
    -   科学计数法：e/E => 10 的 x 幂
        -   123.2e2

4.  字符串 str

    -   用于记录文本信息, `""` 双引号包裹。

5.  复数 complex

    -   虚部以j或J结尾
        -   5 + 3j

6.  布尔 bool
    -   True / False

#### 数据类型转换

-   int() / float() / str() / complex()
-   bool()
    -   False: 0, 0.0, "", None
-   混合类型自动升级
-   1 + 2.14 => 3.14

### 运算符

-   `+`  `-`  `*`
-   除
    -   小数除: `/`   (结果为float类型)
    -   底板除：`//`  (向下取整)
    -   取余数: `%`
-   幂运算:  `**`

-   优先级

    -   `**`
    -   `()`
    -   `*` `/` `%` `//`
    -   `+` `-`

-   round()  => (数据，精度)：四舍五入，精度如果省略，则默认为0.

#### 增强运算符

`x += 1 => x = x + 1`

-   `-=`
-   `*=`
-   `/=`
-   `//=`
-   `%=`
-   `**=`

#### 比较运算符

`>`
`<`
`==`
`>=`
`<=`
`!=`

#### 逻辑运算符

-   与 `and` => 一假皆假
-   或 `or` => 一真俱真
-   非 `not`

#### 短路逻辑

-   如果ａｎｄ前面的表达式结果为false，后面的表达式不再执行
    -   建议：将耗时的判断尽量放在后面
-   如果or前面的表达式结果为True，后面的表达式不再执行
    -   建议：将耗时的判断尽量放在后面

#### 身份运算符

-   判断两个对象是不是同一个对象
-   x is y => id(x) == id(y)
-   x is not y => id(x) != id(y)

#### 优先级

-   从高到低：
-   算数运算符
-   比较运算符
-   增强运算符
-   逻辑运算符

-   小括号最高

#### del

1.  作用： del 语句可以删除变量
2.  语法： del 变量名1，变量名2
3.  对象引用计数：当对象绑定给变量时，计数增加1，当变量解除绑定时，计数减少
    -   待计数为0时，对象自动释放。

### 语句

1.  行

    -   物理行：程序员编写代码时的行。
    -   逻辑行：python解释器需要执行的指令。

        -   建议一个物理行对应一个逻辑行。
        -   如果在一个物理行使用多个逻辑行，使用分号隔开`；`
        -   `print('1');print('2')`

    -   如果逻辑行过长，可以使用隐式换行或显示换行
        -   隐式换行：所有括号的内容换行。`() [] {}`
        -   显示换行：通过折行符换行`\`

2.  选择

```python
if condition:
    print("...")
elif condition:
    print("...")
else:
    print("...")
```

-   真值表达式：
    -   if 条件可以为 非布尔变量，python 自动转化为 bool
-   条件表达式：
    -   语法：`variable` = `result1` if `condition` else `result2`

3.  循环

**while 语句**

```py
# while True => 死循环，后续代码不再执行
while condition:
    result
    if exit_condition:
        break # 退出循环体
else
    # while 条件结束执行，break后不执行 else
```

**for 语句**

-   用来遍历可迭代对象的数据元素
-   可迭代对象：能一次获取数据元素的对象

```py
for  变量列表 in 可迭代对象:
    语句
else
    语句
```

range() 函数

-   创建一个生成一系列整数的可迭代对象
-   range(开始，结束，间隔)
    -   返回的数字不包含结束点
    -   开始默认为 0
    -   间隔默认为 1

> for 语句 与 range() 函数 结合做预定次数的循环

4.  跳转语句

break:

-   跳出循环体，后面的代码不再执行。
-   可以让while语句的else部分不执行。

ontinue: 跳过本次循环，继续下次循环。

### 容器

#### 字符串 str

> 由一系列字符组成的**不可变序列**容器，存储的是字符编码值。

##### 编码

-   字节Byte：计算机存储的最小单位,等于8位bit（位）。
-   字符：单个的数字，文字，符号。
-   字符集(码表)：存储字符与二进制序列的对应关系。
-   编码：将字符转换为对应的二进制序列的过程。
-   解码：将二进制序列转换为对应的字符的过程。
-   编码方式：
    1.  ASCII编码：包含英文、数字等字符。每个字符1个字节。
    2.  GBK编码：兼容ASCII，包含21003个中文。每个英文1个字节，汉字2个字节。
    3.  Unicode字符集：国际统一编码，旧字符集每个字符2个字节，新字符集每个字符4字节。
    4.  UTF – 8编码：Unicode的存储和传输方式。英文1个字节，中文3个字节。

##### 相关函数

-   ord() ： 参数：字符串，返回 该字符串 的Unicode码
-   chr() ： 参数：Unicode码，返回 该字符串

##### 字面值

单引号和双引号（无区别）

-   单引号内的双引号不算结束符
-   双引号内的单引号不算结束符

三引号（即 js 中的模板字符串） =>  `"""str"""`/`'''str'''`
	可以包含单双引号
	可见即所得，常常作为文档注释

转义符

-   定义：可以改变原有字符含义的特殊字符
-   常用的：
    -   `\n` => 换行
    -   `\0` => 空字符
    -   `\t` => 水平制表格(即：tab)
-   原始字符：
    -   字符串前 加 `r` => 取消转义
    -   str = r"str"
-   字符串格式化:

    -   生成一定格式的字符串
    -   "str"%(变量列表)
        -   `"my name is %s. age is %d. score is %f" % (name, age, score)`
    -   格式：`%[- + 0 宽度.精度]类型码`

        -   `-` ： 左对齐(默认就是右对齐) => print("num is %-5d" % (num))
        -   `+` ：显示正号 => print("num is %-5d" % (num))
        -   0：左侧空白位置补零 => print("num is %05d" % (num))
        -   宽度：整个数据输出的宽度(字符大小) => print("num is %5d" % (num))
        -   精度：保留小数点后多少位 => print("num is %.2f" % (float_num))
            -   与 round() 的区别 功能相同
            -   round() 改变数值

    -   类型码: s(字符串) d(整数) f(float)

#### 通用操作

##### 数学运算符

-   `+`：拼接两个容器
-   `+=`：用原容器与右侧容器拼接，并重新绑定变量
-   `*`：重复生成容器元素
-   `*=`：用原容器生成重复元素，并重新绑定变量
-   `<  >  >=  <=  ==  !=`：依次比较两个容器中元素的编码值，一但不同则返回结果。

##### 成员运算符

-   数据  in  容器
-   数据  not in  容器
-   判断容器中是否包含指定数据，返回bool类型。

##### 索引

作用：访问容器元素
语法：容器[整数]

-   索引不能越界

正向索引从0开始，最后一个是`len(字符串) -1`
反向索引从-1开始，-1代表最后一个，第一个是 `- len(字符串)`

##### 切片

1.  作用：从容器中取出相应的元素重新组成一个容器。
2.  语法：容器[开始索引:结束索引:步长]
3.  说明：

-   结束索引不包含该位置元素
-   步长是切片每次获取完当前元素后移动的偏移量
-   省略开始索引，默认为0.
-   省略结束索引，默认最后。
-   即使越界也不会报错

4.  特殊

```py
"abcde"[::] # "abcde"
"abcde"[::-1] # "edcba"
"abcde"[-2:-5:-1] # "dcb"
"abcde"[3:1] # 空
"abcde"[3:1:-1] # "dc"
"abcde"[-2:] # "de"
"abcde"[1:1] # 空
```

##### 内建函数

-   len(容器)  返回容器长度
-   sum(容器)  返回容器所有元素的累加和（元素必须是数值）
-   max(容器)  返回容器中最大的元素
-   min(容器)  返回容器中最小的元素


#### 列表 list

> 由一系列变量组成的**可变序列**容器。

-   创建：
    -   创建空元组：list01 = [] / list()  
    -   创建有默认值的元组：list01 = [1,2,3] / list("agasdg")
        -   [元素]   
        -   list(可迭代对象)
-   添加元素
    -   追加：list01.append(元素)
    -   插入：list01.inset(index, 元素)
-   删除元素
    -   移除指定元素：list01.remove(元素)
    -   删除指定索引元素：del list01[0]
-   修改元素、获取元素 => 使用 索引、切片 定位到元素操作
-   遍历使用 for 循环结合 range
-   排序：list01.sort()
    -   指定范围排序：
    ```python
    temp = list01[:4]
    temp.sort()
    list01[:4] = temp
    ```

```python
listtext = [1, 2, 3, "a", True, "d"]
listtext[:3] = ["x", "y", "z", "z", "f"] # ['x', 'y', 'z', 'z', 'f', 'a', True, 'd']
listtext[:3] = ["x"] # ['x', 'a', True, 'd']

# 正
for i in range(len(listtext)):
    print(listtext[i])
# 跳
for i in range(0, len(listtext), 2):
    print(listtext[i])
# 倒
for i in range(len(listtext) - 1, -1, -1):
    print(listtext[i])
```

**经典案例：找最大/小值**

```python
list_num = [23, 123, 44, 1, 4, 2, 55, 234, 123, 532, 23]

max_num = list_num[0]

for i in range(1, len(list_num)):
    if list_num[i] > max_num:
        max_num = list_num[i]
print(max_num)
```

##### 与字符串联系

1.  列表和字符串都是序列，元素之间有先后顺序。
2.  字符串时不可变的序列，列表可变。
3.  字符串中每个元素存储字符，而列表可以存储任意类型对象。
4.  列表和字符串都属于可迭代对象。
5.  关联：

    -   将多个字符串拼接为一个。
        -   result = "连接符".join(列表)
    -   将一个字符串拆分为多个。
        -   列表 = "a-b-c-d".split("分隔符")
    
    ```python
    # 此方式耗内存,耗能
    result = ""
    for item in range(10):
        result += str(item)
    print(result)

    # 最优解
    list_result = []
    for item in range(10):
        list_result.append(str(item))
    str_result = "-".join(list_result)
    print(str_result)
    ```

##### 列表操作原理（内存图）

```python
list01 = [0, 1]
list02 = list01
list01[0] = 100
print(list02[0])
```

**内存图**

![Python-MemoryAllocationMap-_List01](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List01.jpg)

```python
list01 = [0, 1]
list02 = list01
list01 = [100]
print(list02[0])
```

**内存图**

![Python-MemoryAllocationMap-_List02](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List02.jpg)

```python
list01 = [0, 1]
list02 = list01[:] # list02 = list01.copy()
list01[0] = 100
print(list02[0])
```

**内存图**

![Python-MemoryAllocationMap-_List03](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List03.jpg)

##### 深拷贝和浅拷贝

>   浅拷贝：在复制过程中，只复制一层变量。不会复制深层变量绑定的对象。
>   深拷贝：复制整个依赖的变量。

**浅拷贝内存图**

![Python-MemoryAllocationMap-_List04](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List04.jpg)

**深拷贝使用**

```python
import copy

list01 = [1, [2, 3]]
list02 = copy.deepcopy(list01)
list01[1][0] = 200
print(list02[1][0])

```

##### 列表推导式

1.  语法：
    -   变量 = [表达式 for 变量 in 可迭代对象]
    -   变量 = [表达式 for 变量 in 可迭代对象 if 条件]

2.	作用：使用简易方法，将可迭代对象转生成为列表

```python
# 示例
list01 = [2, 5, 6, 7, 8, 9]
# list02 = []
# for item in list01:
#     if not item % 2:
#         list02.append(item**2)
list03 = [item**2 for item in list01 if not item % 2]
```

##### 列表扩容原理

-   开辟更大的空间
-   将原数据拷贝过来
-   替换表头地址

![Python-MemoryAllocationMap-_List05](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List05.jpg)

#### 元组 tuple

> 由一系列变量组成的**不可变序列**容器。

1.  创建空元组：t01 = () / tuple()
2.  创建有默认值的元组：t01 = (1,2,3) / tuple("agasdg")
    -   (元素)   
    -   tuple(可迭代对象)
3.  作用
    -   元组与列表都可以存储一系列变量。
    -   列表会预留内存空间，所以可以增加。
    -   元组会按需分配内存，建议变量数据固定时使用元组，因为通常占用空间小。
4.  如果元组只有一个元素必须在元素后加一个","，否则视为普通对象不是元组对象。

#### 字典 dict

![Python-MemoryAllocationMap-_List06](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List06.jpg)

1.  定义
-   由一系列键值对组成的可变映射容器。
-   映射(哈希算法)：通过键对应值，每条记录无序。
-   键必须唯一且不可变对象(字符串、数字、元组)，值没有限制。
2.  创建
-   创建空字典：d01 = {} / dict()
-   创建有默认值的字典：d01 = {"a": "A", "b": "B"} / dict([(1, 2), (3, 4)])
    -   {键1：值1，键2：值2}   
    -   dict(可迭代对象)
3.   添加/修改：
-   字典[键] = 表达式
-   说明：键不存在则创建，键存在则修改。
4.  获取值：
-   字典[键]
-   说明：如果不存在键，则错误。
    -   在字典中读取元素，先判断存在，再读取
5.  删除：
-   del 字典[键]
6.  获取字典所有记录

```python
# for item in d01.items():
#     print(item[0]) # key
#     print(item[1]) # value

# 获取字典所有记录
for k, v in d01.items():
    print(k) # key
    print(v) # value

# 获取字典所有键
for k in d01.keys():
    print(k) # key

# 获取字典所有值
for v in d01.values():
    print(k) # key
```

7.  示例：

```python
input_string = input("")
d01 = {}
for item in input_string:
    if item not in d01:
        d01[item] = 1
    else:
        d01[item] += 1
print(d01)
```

8.  字典推导式

```python
dic01 = {}
# for item in range(10):
#     if not item % 2:
#         dic01[item] = item**2

dic01 = {item: item**2 for item in range(10) if not item % 2}
# 键值反转，值不重复
dic02 = {values: keys for keys, values in dic01.items()}
# 键值反转，值重复，不希望被覆盖
dic03 = [(values, keys) for keys, values in dic01.items()]
```
