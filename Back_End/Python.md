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

2.  作用：使用简易方法，将可迭代对象转生成为列表

```python
# 示例
list01 = [2, 5, 6, 7, 8, 9]
# list02 = []
# for item in list01:
#     if not item % 2:
#         list02.append(item**2)
list03 = [item**2 for item in list01 if not item % 2]
```

3. 列表推导式嵌套

```python
list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
list03 = []
# 全排列
# for i in list01:
#     for j in list02:
#         list03.append(i + j)
list03 = [i + j for i in list01 for j in list02]
print(list03)
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

#### 集合 set

> 由一系列不重复的不可变类型变量组成的可变映射容器
> 相当于只有键没有值的字典

1.  创建
-   创建空集合：s01 = set()
-   创建有默认值的集合：s01 = {"a", "b"} / set("abcde")
    -   {元素1, 元素2}   
    -   set(可迭代对象) => 其他容器 -> 集合 （去重）
2.  增：
    s01.add(元素)
3.  删：
    -   s01.remove(元素)
    -   s01.discard(元素) => `if 元素 in s01: s01.remove(元素)` (元素不存在不会报错)
4.  查：
    -   `for item in s01:`
    -   查找全部，只能使用 `for` , 不能修改 （原因是映射）
5.  运算：
    -   交集: s01 & s02
    -   并集: s01 | s02
    -   补集: s01 ^ s02
    -   对称补集: s01 - s02
    -   子集: s02 < s01
    -   超集: s01 > s02
6.  集合推导式：
    -   {表达式 for item in s01 if 条件}

#### 固定集合 frozenset

> 不可变的集合 (没有预留空间，不能增，不能删)

-   创建空集合：frozenset()
-   创建具有默认值的集合：frozenset(可迭代对象)

#### 双层 for 循环

```python
for row in range(3):
    for column in range(5):
        print("*", end="")  # 在一行输出
    print()  # 换行

# ------- 提升
num = input("")
status = False
for i in range(len(num) - 1):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            status = True
if status:
    print("no")
else:
    print("yes")

# ------- 排序
list01 = [4, 2, 5, 1, 22, 59, 21, 42, 20]
for i in range(len(list01) - 1):
    for j in range(i + 1, len(list01)):
        if list01[i] < list01[j]:
            list01[i], list01[j] = list01[j], list01[i]
print(list01)
```

### 函数 function

1.  定义：用于封装一个特定的功能，表示一个功能或行为

    -   函数是可以重复执行的语句块，可以重复调用。

2.  作用：

    -   提高代码的可重用性，可维护性（代码层次结构更清晰）

3.  定义函数：

    1.  语法：

        ```python
        def 函数名(形参列表):
		函数体
        ```
    
    2.  说明：

        -   def 关键字，全称 define ，意为”定义”。
        -   函数名：对函数体中语句的描述，命名规则与变量相同，建议使用动词。
        -   形参列表：形式参数
            -   方法定义者 要求 调用者提供 的信息
        -   函数体：完成该功能的语句。

    3.  函数的第一行语句可以选择性的使用文档字符串存储函数与参数的说明。

4.  函数调用：

    -   语法：函数名(实参列表)
    -   说明：根据形参传递内容。

5.  返回值：

    1.  定义：方法定义者告诉调用者的结果。
    2.  语法：在方法体中，通过return关键字指明结果。
        -   return 结果
    3.  说明：
        -   不写 return 关键字，相当于返回 None
        -   return 还意味着方法结束。

**实例以及规范写法**
```python
def get_prime_number(star_num, end_num):
    """
        生成指定范围内的所有素数
    :param star_num: 开始
    :param end_num: 结束
    :return: 范围内的所有素数
    """
    list_prime_number = []
    for number in range(star_num, end_num + 1):
        if is_prime(number):
            list_prime_number.append(number)
    return list_prime_number


def is_prime(number):
    """
        判断是否为素数
    :param number: 需要判断的数
    :return: bool
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(get_prime_number(1, 101))
```

#### 函数传参：

1.  实参传递方式 argument

    1.  位置传参:
        -   实参与形参的位置依次对应
        -   序列传参
            -   实参用 * 将序列拆解后与形参的位置依次对应
            -   可以在运行时，根据某些逻辑决定传入的数据（列表）
    2.  关键字传参：
        -   实参根据形参的名字进行对应 `fun01(a=1, b=2, c=3)`
        -   字典传参
            -   实参用 ** 将字典拆解与形参的名字进行对应。
            -   可以在运行时，根据某些逻辑决定传入的数据（字典）

2.  形参传递方式 parameter
    
    -   默认(缺省)参数：让调用者可以有选择性的传递需要的信息
        1.  语法：
            def 函数名(参数1 = 默认值1):
                函数体
        2.  说明：
            -   缺省参数必须自右至左依次存在，如果一个参数有默认值，则右侧所有参数必须都有默认值。
            -   缺省参数可以有0个或多个

    -   位置形参
        -   星号元组形参
            1.  语法：
                def 函数名(*args):
                    函数体
            2.  作用：收集多余的位置形参
            3.  说明：
                -   一般命名为 *args
                -   形参列表最多只能有一个
                -   在方法内部，就是元组
                -   对调用者而言，**可以传递数量无限的位置实参**

    -   命名关键字形参
        1.  语法：
            def 函数名(*,参数名):
                函数体
            def 函数名(*args,参数名):
                函数体
        2.  作用：强制实参使用关键字传递
        3.  双星号字典形参
            1.  语法：
                def 函数名(**kwargs):
                    函数体
            2.  作用：收集多余的关键字传参
            3.  说明：
                -   一般命名 kwargs
                -   形参列表中最多只能有一个
                -   在方法内部，就是字典
                -   对调用者而言，**可以传递数量无限的关键字实参**
            ```python
            def keywords(**kwargs):
                print(kwargs)


            keywords(a="c", b=1, c=23)
            ```

3.  参数自左至右的顺序

    位置形参 --> 星号元组形参 --> 命名关键字形参 --> 双星号字典形参

4.  可变/不可变类型在传参时的区别：

    1.  不可变类型参数：
        -   数值型：整数、浮点数、复数 
        -   布尔值 bool
        -   空值 None
        -   字符串 str
        -   元组  tuple
        -   固定集合 frozenset
    2.  可变类型参数：
        -   列表 list
        -   字典 dict
        -   集合 set
        -   字节数组 bytearray
    3.  传参说明：
        -   不可变类型的数据传参时，函数内部不会改变原数据的值。
        -   可变类型的数据传参时，函数内部可能改变原数据的值。
    4.  内存图：

        **不可变对象传参**

        ```python
        def func01(num01):
            num01 = 2
            print("num01: " + str(num01))


        number01 = 1
        # 调用方法在内存中开辟空间（栈帧）
        # 栈帧中定义该方法内部创建的变量
        # 方法执行完毕后，栈帧立即释放
        func01(number01)
        print("number01: " + str(number01))
        ```

        ![Python-MemoryAllocationMap-_Fun01](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_Fun01.jpg)

        **可变对象传参**

        ```python
        def func02(list_target):
            list_target[0] = 2
            print("list_target[0]: " + str(list_target[0]))


        list_number = [1, 2]
        func02(list_number)
        print("list_number[0]: " + str(list_number[0]))
        ```

        ![Python-MemoryAllocationMap-_Fun02](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_Fun02.jpg)

#### 作用域 LEGB

1.  作用域：变量起作用的范围
    -   Local 局部作用域：函数内部。
    -   Encolsing 外部嵌套作用域：函数嵌套
    -   Global 全局作用域：模块(.py)文件内部
    -   Builtins 内建模块作用域：builtins.py

2.  变量名查找规则：L -> E -> G -> B

3.  全局变量：

    -   定义在函数外部，模块(.py文件)内部的变量
    -   函数体内部可以访问，但是不能直接修改（需使用global语句声明才能修改）
    -   global 语句
        1.  作用：
            -  在函数内部修改全局变量
            -  在函数内部定义全局变量（全局声明）
        2.  语法：global 变量1，变量2
        3.  说明：
            -  在函数内部直接为全局变量赋值，视为创建新的局部变量
            -  不能先声明局部变量，再用 global 声明为全局变量

        ```python
        g01 = 100


        def fun():
            # 方法内部可以读取全局变量
            # print(g01)

            # 在方法内部创建了局部变量 g01,没有修改全局变量 g01
            # g01 = 300
            # print(g01)

            # 若需要在方法内部，修改全局变量
            global g01
            g01 = 400

            # 在局部作用域中，创建全局变量 
            global g02
            g02 = 500


        fun()
        print(g01)
        print(g02)
        ```

4.  局部变量

    -   在方法体内部定义的变量
    -   调用函数时才被创建，函数结束后自动销毁
    -   在方法内部创建的变量，只能在方法内部使用

## 面向对象 Object Oriented

### 类和对象的浅析

1.  类：一个抽象的概念，即生活中的”类别” 
    -   例如：学生、水果。 

2.  对象：类的具体实例，即归属于某个类别的”个体” 

    -   例如：张三同学、苹果 

3.  类是创建对象的”模板”. 

    -   数据成员：名词性的状态。例如：姓名 
    -   方法成员：动词性的行为。例如：学习 

4.  类与类的行为不同，对象与对象的数据不同。 

### 类和对象的用法

1.  定义类

    ```python
    class 类名: 

    """文档说明"""

    def  __init__(self,参数列表): 

    self.实例变量 = 参数 
    ```

2.  方法成员

    -   类名所有单词首字母大写 

    -   __init__叫做构造函数,创建对象时被调用，也可以省略。 

    -   self变量绑定的是被创建的对象，名字通常叫做”self”。 

### 类和对象的语法

1.  创建对象(实例化对象) 
    -   变量 = 构造函数(参数列表) 
    -   构造函数的self参数会自动绑定对象地址，不用传递

2.  实例成员：
    1.  实例变量：
        -   语法： 
            -   定义：对象地址.变量名称 
            -   调用：对象地址.变量名称 
        -   说明 
            -   首次通过对象赋值为创建变量，再次赋值为修改。 
                ```python
                w01 = Car() 
                w01.name = "bm" # 创建 
                w01.name = "bc" # 修改 
                ```
            -   通常在构造函数(__init__)中创建. 
                ```python
                w01 = Car("bm") 
                w01.name = "bc" # 修改 
                ```
            -   每个对象存储一份，通过对象地址访问。 
            -   __dict__: 对象的属性，用于存储自身是实例变量的字典
                -   `w01.__dict__`
    2.  实例方法 
        -   语法： 
            -   定义：
                ```python
                def 方法名称(self,参数): 
                    方法体                
                ```
            -   调用：
                -   对象地址.实例方法名称(参数) 
                    -   通过对象地址调用实例方法，会自动传递对象地址
                -   不建议的用法： 
                     -   可以通过类名访问，并传递对象地址。 
                     -   类名.实例方法名(对象地址,参数) 
                     -   通过类名调用实例方法，需手动传递
            -   说明： 
                -   至少有一个形参，用于绑定调用该方法的对象，一般命名为"self"。 
                -   无论创建多少个对象，方法只有一份，且**实例方法被所有对象共享.** 
                -   作用：表示对象的行为。 
    3.  内存图

```python
class Car:
    # self 调用当前方法的对象
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def travel(self):
        print(self.name, "travel")

# 对象的地址
w01 = Car("bm", 12, 10000)
# 通过对象地址, 调用对象方法,会自动传递对象地址
w01.travel()
```

![Python-MemoryAllocationMap-_OOP01](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_OOP01.jpg)

3.  类成员

    1.  类变量 
        -   语法 
            -   定义：在类中，方法外定义变量 
            ```py
            class 类名:
                类变量名 = 数据
            ```
            -   调用：类名.类变量名
                -   不建议使用对象.类变量名.
            -   说明 
                -   存储在类中。
                -   只有一份，被所有对象共享。
                -   描述所有对象的共有数据。

    2.  类方法
        -   语法
            -   定义
            ```py
            @classmethod 
            def 方法名称(cls,参数): 
                方法体 
            ```
            -   调用：类名.方法名(参数)
                -   不建议使用对象.类方法名
            -   说明
                -   至少有一个形参，用于绑定调用该方法的类，一般命名为"cls"。
                -   使用@classmethod修饰的目的是调用方法时隐式传递类。
                -   类方法不能访问实例成员，实例方法可以访问类成员。
            -   作用：操作类变量

    3.  内存图

```py
class ICBC:
    moneys = 9999999

    @classmethod
    def print_total_money(cls):
        print(cls.moneys)

    def __init__(self, name, money):
        self.name = name
        self.money = money
        ICBC.moneys -= money


i01 = ICBC("zfzhihang", 100000)
# 调用类变量
# print(ICBC.moneys)
# 调用类方法，此时会自动传递类名进入方法
ICBC.print_total_money()

i02 = ICBC("cfzhihang", 100000)
ICBC.print_total_money()
```

![Python-MemoryAllocationMap-_OOP02](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_OOP02.jpg)

4.  静态方法 

    1.  语法 
        -   定义：
            ```py
            @staticmethod
            def 方法名称(参数):
                方法体
            ```
        -   调用：类名.方法名称(参数) 
            -   不建议使用对象.静态方法名. 
        -   说明：
            -   使用 @staticmethod 修饰的目的是该方法不需要隐式传递参数。 
            -   静态方法不能访问实例成员和类成员 
        -   作用：
            -   统一管理函数(定义在 .py 文件中的函数)  
            -   表达不需要使用实例成员和类成员时，使用静态方法。
            -   将函数转移到类中，即静态方法
    2.  实例
    ```python
    class Vector2:
        """
            向量
        """

        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        @staticmethod
        def right():
            return Vector2(0, 1)

        @staticmethod
        def up():
            return Vector2(-1, 0)


    class DoubleListHelper:
        """
            二维列表助手:
                在开发过程中，所有对二维列表的常用操作
        """

        @staticmethod
        def get_elements(list_target, v_pos, v_dir, count):
            get_list = []
            for i in range(count):
                v_pos.x += v_dir.x
                v_pos.y += v_dir.y
                get_list.append(list_target[v_pos.x][v_pos.y])
            return get_list


    # 测试
    # list01 = [
    #     ["00", "01", "02", "03"],
    #     ["10", "11", "12", "13"],
    #     ["20", "21", "22", "23"],
    #     ["30", "31", "32", "33"],
    # ]
    # 
    # re = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
    # print(re)
    ```

### 封装

封装数据的优势：
    -   符合人类的思考方式，
    -   将数据与对数据的操作封装起来。

#### 封装的定义

    1.  从数据角度讲：
        -   将一些基础变量复合为一个自定义类型。
        -   不但可以准确的描述事物，还可以体现该事物的行为。

    2.  从行为角度讲：
        -   向类外提供必要的功能，隐藏实现的细节。
        -   使用者可以不必操心实现过程。

    3.  从设计角度讲：

        -   分而治之
            -   将一个大的需求分解为许多类，让每个类处理一个独立的功能。
            -   优点：便于分工，便于复用，可扩展性强。
        -   封装变化
            -   需求可能会变化的功能要单独封装，避免影响其他类。
            -   模块化编程
        -   高内聚
            -   类中各个方法都在完成一项任务
        -   低耦合
            -   类与类的关联性与依赖度要低，让一个类变化，尽少影响其他的类。

#### 私有成员

1.  语法：命名使用双下划线开头
2.  作用：修改变量名，让外界”不能直接访问”
3.  本质：障眼法，也可以访问：`_类名__成员名`

```python
class Enemy:
    def __init__(self, name="", atk_speed=0):
        self.set_name(name)
        self.set_atk_speed(atk_speed)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_atk_speed(self):
        return self.__atk_speed

    def set_atk_speed(self, value):
        if 0 <= value <= 10:
            self.__atk_speed = value
        else:
            print("err")
```

#### 属性

> 公开的实例变量，缺少逻辑验证。私有的实例变量与两个公开的方法相结合，又显得调用者的操作略显复杂。而属性可以将两个方法的使用方式像操作变量一样方便

1.  定义

    ```python
    @property  # 读取数据时执行 
    def 属性名(self): 
    return  self.__ 属性名    # 私有的实例变量 

    @属性名.setter  # 写入数据时执行 
    def 属性名(self,参数): 
    self.__ 属性名 = 参数 
    ```

2.  调用：

    -   对象地址.属性名 = 数据
    -   变量 = 对象地址.属性名

3.  说明：

    -   通常两个公开属性，保护一个私有的变量。
    -   @property  负责处理读取逻辑
    -   @属性名.setter 负责处理写入逻辑

    ```python
    class Student:
        def __init__(self, name="", age=0):
            # self.set_name(name)
            self.name = name  # 调用 @name.setter 修饰的方法
            # self.set_age(age)
            self.age = age  # 调用 @age.setter 修饰的方法

        # def get_name(self):
        #     return self.__name

        # 本质：创建 property 对象， name 存储对象地址
        # 注意：创建对象时，会指定读取方法
        # 相当于：name = property(get_name， None)
        @property  # 拦截读取变量的操作
        def name(self):  # get_name()
            return self.__name

        @name.setter  # 拦截写入变量的操作 本质：name.setter(写入方法)
        def name(self, value):  # set_name()
            self.__name = value

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, value):
            if 7 <= value <= 22:
                self.__age = value
            else:
                self.__age = 0
                print("err")
    ```

4.  属性本质

    ```python
    class Student:
        def __init__(self, name=""):
            self.name = name

        def get_name(self):
            print("get")
            return self.__name

        def set_name(self, value):
            print("set")
            self.__name = value
        # 拦截对变量 name 的读写操作
        # 创建 property 对象， name 存储的是对象地址
        # 注意：创建对象时，需要传递读写方法
        name = property(get_name, set_name)
    ```

5.  只读属性

    ```python
    class Student:
        def __init__(self, name=""):
            self.__name = name

        # 只读属性
        # 本质：创建 property 对象， name 存储对象地址
        # 注意：创建对象时，会指定读取方法
        # 相当于：name = property(get_name， None)
        @property
        def name(self):
            return self.__name
    ```

6.  只写属性

    ```python
    class Student:
        def __init__(self, name=""):
            self.name = name

        def set_name(self, value):
            self.__name = value

        name = property(None, set_name)

    s01 = Student("zfzf")
    print(s01._Student__name)
    ```

7.  拓展（只读属性返回可变对象时）

    ```python
    class Person:
        def __init__(self, name):
            self.name = name
            self.__skills = []

        def teach(self, person_other, str_skill):
            person_other.__skills.append(str_skill)
            print(self.name, person_other.name, str_skill)

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, value):
            self.__name = value

        @property
        def skills(self):
            # 返回可变对象地址，意味着在类外仍可以操作可变对象
            # return self.__skills
            # 返回新的可变对象，意味着在类外操作的是新可变对象，不影响原对象
            return self.__skills[:]
            # 备注：每次通过切片返回的新对象，都会另外开辟空间创建新对象，占用过多内存
    ```

8.  `__slots__`

    -   作用：限制一个类创建的对象只能有固定的实例变量，不能再额外添加。
    -   语法：在类中定义 `__slots__ = (“变量名1”,”变量名2”)`
    -   说明
        -   含有`__slots__`属性的类所创建的对象没有`__dict__`属性。
        -   优点：防止因写错属性名称而发生的错误。
        -   缺点：丧失了动态语言可以在运行时为对象添加变量的灵活性。