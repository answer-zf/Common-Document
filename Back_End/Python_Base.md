# python 基础

> python执行过程：
> 	源代码 –编译--> 字节码(特定python的表现形式.pyc) –解释--> 机器码
> 	|—————————————————— 1 次 ————————————————|

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
    -   创建空元组：list01 = \[] / list()
    -   创建有默认值的元组：list01 = [1,2,3] / list("agasdg")
        -   [元素]
        -   list(可迭代对象)
-   添加元素
    -   追加：list01.append(元素)
    -   插入：list01.inset(index, 元素)
-   删除元素
    -   移除指定元素：list01.remove(元素)
        -   删除一个建议使用
    -   删除指定索引元素：del list01[0]
        -   删除多个建议使用，从后往前删不会出错
            -   删除以后，后面的索引会前进一位，导致错误
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

![Python-MemoryAllocationMap-\_List01](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List01.jpg)

```python
list01 = [0, 1]
list02 = list01
list01 = [100]
print(list02[0])
```

**内存图**

![Python-MemoryAllocationMap-\_List02](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List02.jpg)

```python
list01 = [0, 1]
list02 = list01[:] # list02 = list01.copy()
list01[0] = 100
print(list02[0])
```

**内存图**

![Python-MemoryAllocationMap-\_List03](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List03.jpg)

##### 深拷贝和浅拷贝

>   浅拷贝：在复制过程中，只复制一层变量。不会复制深层变量绑定的对象。
>   深拷贝：复制整个依赖的变量。

**浅拷贝内存图**

![Python-MemoryAllocationMap-\_List04](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List04.jpg)

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

3.  列表推导式嵌套

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

![Python-MemoryAllocationMap-\_List05](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List05.jpg)

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

![Python-MemoryAllocationMap-\_List06](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_List06.jpg)

1.  定义

-   由一系列键值对组成的可变映射容器。
-   映射(哈希算法)：通过键对应值，每条记录无序。
-   键必须唯一且不可变对象(字符串、数字、元组)，值没有限制。

2.  创建

-   创建空字典：d01 = {} / dict()
-   创建有默认值的字典：d01 = {"a": "A", "b": "B"} / dict([(1, 2), (3, 4)])
    -   {键1：值1，键2：值2}
    -   dict(可迭代对象)

3.  添加/修改：

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
    -   子集: s02 &lt; s01
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
            -   实参用 \* 将序列拆解后与形参的位置依次对应
            -   可以在运行时，根据某些逻辑决定传入的数据（列表）
    2.  关键字传参：
        -   实参根据形参的名字进行对应 `fun01(a=1, b=2, c=3)`
        -   字典传参
            -   实参用 \*\* 将字典拆解与形参的名字进行对应。
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
                def 函数名(\*args):
                    函数体
            2.  作用：收集多余的位置形参
            3.  说明：
                -   一般命名为 \*args
                -   形参列表最多只能有一个
                -   在方法内部，就是元组
                -   对调用者而言，**可以传递数量无限的位置实参**

    -   命名关键字形参

        1.  语法：
            def 函数名(\_,参数名):
                函数体
            def 函数名(\_args,参数名):
                函数体
        2.  作用：强制实参使用关键字传递
        3.  双星号字典形参

            1.  语法：
                def 函数名(\*\*kwargs):
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

        ![Python-MemoryAllocationMap-\_Fun01](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_Fun01.jpg)

        **可变对象传参**

        ```python
        def func02(list_target):
            list_target[0] = 2
            print("list_target[0]: " + str(list_target[0]))

        list_number = [1, 2]
        func02(list_number)
        print("list_number[0]: " + str(list_number[0]))
        ```

        ![Python-MemoryAllocationMap-\_Fun02](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_Fun02.jpg)

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
            -   在函数内部修改全局变量
            -   在函数内部定义全局变量（全局声明）
        2.  语法：global 变量1，变量2
        3.  说明：
            -   在函数内部直接为全局变量赋值，视为创建新的局部变量
            -   不能先声明局部变量，再用 global 声明为全局变量

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
    -   局部变量可以访问外部嵌套变量,修改需要使用 `nonlocal` 关键字

    ```py
        def fun01():
            # 外部嵌套作用域
            a = 1

            def fun02():
                b = 2
                # 可以访问外部嵌套变量 a
                # 没有修改外部嵌套变量，而是创建了新的局部变量
                # a = 3
                # print(a)
                nonlocal a  # 生命外部嵌套变量 a
                a = 3
                print(a)

            fun02()
            print(a)

        fun01()
    ```

## 面向对象 Object Oriented

### 类和对象

#### 类和对象的浅析

1.  类：一个抽象的概念，即生活中的”类别”

    -   例如：学生、水果。

2.  对象：类的具体实例，即归属于某个类别的”个体”

    -   例如：张三同学、苹果

3.  类是创建对象的”模板”.

    -   数据成员：名词性的状态。例如：姓名
    -   方法成员：动词性的行为。例如：学习

4.  类与类的行为不同，对象与对象的数据不同。

#### 类和对象的用法

1.  定义类

    ```python
    class 类名:

    """文档说明"""

    def  __init__(self,参数列表):

    self.实例变量 = 参数
    ```

2.  方法成员

    -   类名所有单词首字母大写

    -   **init**叫做构造函数,创建对象时被调用，也可以省略。

    -   self变量绑定的是被创建的对象，名字通常叫做”self”。

#### 类和对象的语法

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
            -   通常在构造函数(**init**)中创建.
                ```python
                w01 = Car("bm")
                w01.name = "bc" # 修改
                ```
            -   每个对象存储一份，通过对象地址访问。
            -   **dict**: 对象的属性，用于存储自身是实例变量的字典
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

![Python-MemoryAllocationMap-\_OOP01](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_OOP01.jpg)

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

![Python-MemoryAllocationMap-\_OOP02](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_OOP02.jpg)

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

    ```py
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
        #
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
    \-   符合人类的思考方式，
    \-   将数据与对数据的操作封装起来。

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
3.  本质：障眼法，也可以访问：`对象._类名__成员名`

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

### 继承

1.  语法：

    ```python
    class 子类名称(父类名称):
        def __init__(self,父类参数,自身参数):
            super().__init__(父类参数)
            self.自身实例变量 =自身参数
    ```

    1.  说明：

        -   子类如果没有构造函数，将自动执行父类的，但如果有构造函数将覆盖父类的。
        -   此时必须通过super()函数调用父类的构造函数，以确保父类数据成员被正常创建。

    2.  内置函数：

        -   isisntance（对象，类型）函数:返回对象是否兼容类型。
        -   issubclass（类型，类型元组）函数:返回类型是否兼容类型元组。
            -   第二个参数只有一个，不需要使用元组，直接写类型即可
            -   类型元组只要有一个兼容该类型即返回 True

2.  定义：重用现有类的功能与概念，并在此基础上进行扩展。

    -   重用现有类的功能，并在此基础上进行扩展 => 代码的复用

3.  说明：

    -   子类拥有父类所有成员：子类直接具有父类的成员，还可以具有自己的功能。
    -   事物具有一定的层次、渊源，继承可以统一概念。

4.  优势：

    -   一种代码的复用方式。
    -   以层次化的方式管理类。

5.  劣势：

    -   子类与父类耦合度高(父类构造函数/成员的变化，直接影响所有子类)
    -   切换不灵活

6.  作用：

    -   隔离客户端代码与功能的实现方式

7.  适用性

    -   多个类在概念上是一致的，且需要进行统一的处理。

8.  相关概念

    -   父类(基类/超类)、子类(派生类).

    -   父类相对于子类更抽象，使用范围更宽泛；

    -   子类相对于父类更具体，使用范围更狭小。

    -   单继承：父类只有一个(例如：java，c#,……)

    -   多继承：父类有多个(例如：python、c++)

    -   Object类(万类之祖)：任何类都直接或者间接继承自Object类。

#### 多继承

> 定义：一个子类继承两个或两个以上的基类，父类中的成员同时被子类继承下来。

**同名方法的解析顺序（MRO）：C3算法模拟的广度优先。**

-   类自身 --> 父类继承列表(由左至右)  --> 再上层父类

```py
    class A:
        def m(self):
            print("a--m")


    class B(A):
        def m(self):
            print("b--m")


    class C(A):
        def m(self):
            print("c--m")


    class D(B, C):
        def m(self):
            super().m()
            C.m(self) # 通过类名调用实例方法，传递对象地址
            print("d--m")


    d01 = D()
    d01.m()
    print(D.mro())
```

### 多态

1.  定义：

    -   调用父类同一个方法，但在不同子类间，有不同的表现。（设计思路：调用父类，执行子类）

2.  作用

    -   继承：将相关概念的共性进行抽象，多态：在共性的基础上，体现子类的个性化。
    -   增强程序扩展性，体现开闭原则。

3.  重写

    -   子类实现了父类中相同(名称、参数)的方法，在调用该方法时，实际执行的是子类的方法。

4.  内置可重写函数

> 在python中，以双下划线开头和结尾的函数--内建函数（系统定义的成员）。可以在自定义类中对其重写，从而改变其行为。

1.  对象转换为字符串：
    -   `__str__`:重写的时候，返回给人看的友好的支持。
        ```python
            def __str__(self):
                return "id is %d, name is %s, age is %d, score is %d" % (self.id, self.name, self.age, self.score)
        ```
    -   `__repr__`:重写的时候，返回解释器可以识别(eval)的字符串。
        ```python
            def __repr__(self):
                return 'StudentModel("%s", %d, %d)' % (self.name, self.age, self.score)
        ```
2.  算数运算符重载：让自定义类生成的对象（实例）能够使用运算符进行操作，本质就是调用内建函数

    ```py
      def __add__(self, other):
          return Vector(self.x + other)

      v01 = Vector(10)
      v02 = v01 + 5
      print(v02)
    ```

**算数运算符重载：(仅支持 对象在左边)**

| 方法名                      | 运算符和表达式       | 说明  |
| :----------------------- | :------------ | :-- |
| `__add__`(self,rhs)      | self + rhs    | 加   |
| `__sub__`(self,rhs)      | self - rhs    | 减   |
| `__mul__`(self,rhs)      | self \* rhs   | 乘   |
| `__truediv__`(self,rhs)  | self / rhs    | 除   |
| `__floordiv__`(self,rhs) | self // rhs   | 地板除 |
| `__mod__`(self,rhs)      | self % rhs    | 取余  |
| `__pow__`(self,rhs)      | self \*\* rhs | 幂   |

**反向算数运算符重载：(仅支持 对象在右边)**

| 方法名                       | 运算符和表达式       | 说明  |
| :------------------------ | :------------ | :-- |
| `__radd__`(self,lhs)      | lhs + self    | 加   |
| `__rsub__`(self,lhs)      | lhs - self    | 减   |
| `__rmul__`(self,lhs)      | lhs \* self   | 乘   |
| `__rtruediv__`(self,lhs)  | lhs / self    | 除   |
| `__rfloordiv__`(self,lhs) | lhs // self   | 地板除 |
| `__rmod__`(self,lhs)      | lhs % self    | 取余  |
| `__rpow__`(self,lhs)      | lhs \*\* self | 幂   |

**复合运算符重载：**

| 方法名                       | 运算符和表达式        | 说明  |
| :------------------------ | :------------- | :-- |
| `__iadd__`(self,rhs)      | self += rhs    | 加   |
| `__isub__`(self,rhs)      | self -= rhs    | 减   |
| `__imul__`(self,rhs)      | self \*= rhs   | 乘   |
| `__itruediv__`(self,rhs)  | self /= rhs    | 除   |
| `__ifloordiv__`(self,rhs) | self //= rhs   | 地板除 |
| `__imod__`(self,rhs)      | self %= rhs    | 取余  |
| `__ipow__`(self,rhs)      | self \*\*= rhs | 幂   |

```py
def __iadd__(self, other):
    self.x += other
    return self
```

**比较运算符重载：**

| 方法名                | 运算符和表达式        | 说明   |
| :----------------- | :------------- | :--- |
| `__lt__`(self,rhs) | self &lt; rhs  | 小于   |
| `__le__`(self,rhs) | self &lt;= rhs | 小于等于 |
| `__gt__`(self,rhs) | self > rhs     | 大于   |
| `__ge__`(self,rhs) | self >= rhs    | 大于等于 |
| `__eq__`(self,rhs) | self == rhs    | 等于   |
| `__ne__`(self,rhs) | self != rhs    | 不等于  |

### 类与类的关系

1.  泛化(继承)

    -   子类与父类的关系，概念的复用，耦合度最高；

    -   B类泛化A类，意味着B类是A类的子类。

    -   做法：B类继承A类。

    -   > 父类 向 子类 的演变 => 特化

2.  关联(聚合/组合)

    -   部分与这个整体的关系，耦合度要低于泛化。

    -   A类关联B类，意味着B是A的一部分。

    -   做法：在A类中包含B类的成员。

3.  依赖

    -   合作关系，耦合度最低。

    -   A类依赖B类，意味着A类的某个功能以依靠B类实现。

    -   做法：在A类的某个方法中，将B类作为参数。

**综合实例**

```python
  class Employee:
      """
          普通员工类 即 父类
      """

      def __init__(self, name, job):  # Employee 关联 job
          self.name = name
          self.job = job

      def calcular_salary(self):
          return self.job.get_salary()


  class Job:
      def __init__(self, basic_salary):
          self.basic_salary = basic_salary

      def get_salary(self):
          return self.basic_salary


  class Programer(Job):  # Programer 泛化 Job（隔离变化）
      """
          程序员类
      """

      def __init__(self, basic_salary, extra):
          super().__init__(basic_salary)
          self.extra = extra

      def get_salary(self):
          return super().get_salary() + self.extra


  class salesmen(Job):
      """
          销售类
      """

      def __init__(self, basic_salary, extra):
          super().__init__(basic_salary)
          self.extra = extra

      def get_salary(self):
          return super().get_salary() + self.extra


  lw = Employee("lw", Programer(100, 10))
  print(lw.calcular_salary())
  lw.job = salesmen(100, 1)
  print(lw.calcular_salary())
```

### 设计原则

1.  开闭原则(目标)

    -   对扩展开放，对修改关闭。
    -   允许增加新功能，不修改客户端(使用者)代码。

2.  类的单一职责(类的定义)

    -   一个类有且只有一个改变的原因。
    -   外界一个需求的变化，内部一个改变的类。

3.  依赖倒置

    -   客户端代码尽量依赖(使用)抽象(父)的组件。
    -   抽象的是稳定的，实现是多变的。
    -   使用抽象（父类），而不使用具体（子类）
    -   隔离 调用 与 定义

4.  组合复用原则(少用继承)

    -   如果仅仅为了代码复用优先选择组合关系，而非继承关系。
    -   组合的耦合度低于继承，灵活度高于继承。

5.  里氏替换(重写注意事项)

    -   父类出现的地方可以被子类替换，在替换后依然保持原有功能。
    -   从内存角度解释：父类(成员少)   子类(成员多)
    -   子类在重写父类方法时，尽量选择扩展重写(先调父类同名方法)，不要改变原有功能。

6.  迪米特法则(低耦合)

    -   原话：不要和陌生人说话。
    -   类与类交互时，在满足功能的基础上，传递的数据量越少越好。

**总结：**

1.  主要思想：封装变化、隔离变化、执行变化
2.  三大特性：
    -   封装：分而治之、封装变化、高内聚、低耦合。
    -   继承：重用现有类功能和概念，在此基础上进行扩展。
    -   多态：继承体现的是共性，多态体现的是个性。
3.  三大关系：
    -   泛化：父子关系
    -   关联：成员关系
    -   依赖：协作关系(做成参数)
4.  六大原则：
    -   开闭原则：对扩展开放，对修改关闭。
    -   单一原则：一个类有且只有一个改变的原因。
    -   依赖倒置：使用抽象(父类),不使用具体(子类).**抽象不依赖于具体.**
    -   组合复用：使用关联关系，不使用泛化关系。（是一种，有一个）
    -   里氏替换：父类出现的地方，可以被子类替换，替换后可以保持原功能。
    -   迪米特法则：低耦合。
5.  优势：通俗的讲，灵活。
    -   高复用：没有重复的代码。
    -   高扩展：开闭原则。
    -   高维护：逻辑清晰，结构规整。

## 模块 Module

1.  定义：包含一系列代码(数据/函数/类/语句)的文件，通常以.py结尾。
2.  作用：让一些相关的代码，有逻辑的组织在一起，使结构更加清晰，有利于团队开发。
3.  导入：

    -   import

        1.  语法：`import 模块名 [as 别名]`
            -   将该模块作用域 赋值给 变量：模块名
        2.  作用：将某个模块整体导入到当前模块
        3.  本质：使用变量名(模块名)关联指定模块代码。
        4.  使用：模块名.成员

    -   from import

        1.  语法：`from 模块名 import 成员 [as 别名]`
            -   将该模块指定成员 赋值给 变量：成员（多个成员逗号隔开）
        2.  作用：将模块内的指定的成员导入到当前模块作用域中。
        3.  使用：成员

    -   from import \*

        1.  语法：`from 模块名 import *`
        2.  作用：将模块内的所有成员导入到当前模块作用域中。
        3.  注意：
            -   小心重名
            -   模块中以下划线(\_)开头的属性，不会被导入，通常称这些成员为隐藏成员。

### 模块变量

-   `__all__`变量：定义可导出成员，仅对 `from xxx import *` 语句有效
    -   `__all__ = ["fun01", "Class01"]`
-   `__doc__`变量：读取文档字符串（`"""`注释是文档字符串）
    -   使用：第一种导入语法 可以用 该模块变量 导出 文档字符串
-   `__file__`变量：模块对应的文件路径名
-   `__name__`变量：模块自身名字，可以判断是否为主模块。
    -   当此模块作为主模块（第一个运行的模块）运行时，`__name__`绑定`__main__`,不是主模块，而是被其他模块导入时，存储模块名。
    -   作用：在if代码块中定义只能从当前模块开始执行，才调用的代码。
    -   `if __name__ == "__main__":`
    -   `测试代码`

### 加载过程

> 在模块导入时，模块的所有语句都会执行。
> 如果一个模块已经导入，则再次导入时不再重复执行语句。

### 分类

1.  内置模块(builtins): 在解释器内部可以直接使用。

2.  标准库模块：安装python时自带的，经过导入后可直接使用。

    ```py
        # 标准库模块 - 时间
        import time

        # 返回时间戳（1970年后经过的浮点秒数）
        print(time.time())
        # 时间戳 -> 时间元组（ 年 月 日 时 分 秒 星期 一年的第几天 夏令时 ）
        print(time.localtime(1590313878.4446368))
        # 时间元组 -> 时间戳
        print(time.mktime(time.localtime()))
        # 时间元组 -> 字符串 （时间的格式化）
        print(time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
        # 字符串 -> 时间元组
        print(time.strptime("2020 05 26", "%Y %m %d"))
    ```

3.  第三方模块：需要自行下载，再导入使用。

4.  自定义模块：经过导入后可直接使用。

### 包 package

1.  Python 程序结构

    ```py
        包
            模块
                类
                    函数()/方法()
                        语句
    ```

2.  定义: 将模块以文件夹的形式进行分组管理。

    -   必须包含`__init__`.py

3.  作用: 让一些相关的模块有逻辑的组织在一起。

4.  使用:

    1.  导入：`import 包.模块`, 使用：`包.模块.成员`
    2.  导入：`from 包 import 模块`, 使用：`模块.成员`
    3.  导入：`from 包 import *` , 使用：`模块.成员`
        -   必须在`__init__.py`文件中，定义`__all__ = [“模块名”]`
    4.  导入：`from 包.模块 import */成员` , 使用：`成员` （推荐）

5.  搜索顺序

    -   搜索内建模块(builtins)

    -   sys.path 提供的路径

        -   第一个路径是运行模块所在路径

        -   如果希望从项目其他模块运行，那么必须在pycharm中设置项目根目录。

        -   `sys.path.append('url')`

### 异常处理

#### 异常

1.  定义：运行时检测到的错误。

2.  现象：当异常发生时，程序不再向下继续执行，而转到函数调用的语句，直到遇到异常处理语句。

3.  常见异常：

    -   名称异常（NameError）：变量未定义

    -   类型异常（TypeError）：不用类型数据进行计算

    -   索引异常（IndexError）：索引越界

    -   属性异常（AttributeError）:对象没有相应属性

    -   未实现异常（NotImplementedError）: 尚未实现的方法

    -   键异常（KeyError）：没有对应名称的键

    -   值异常（ValueError）：值错误

    -   异常基类（Exception）

#### 处理

1.  语法：

    ```py
        try:

            可能发生错误的代码

        except 异常类型1 [as 变量名]:

             处理逻辑1

        except 异常类型2 [as 变量名]:

             处理逻辑2
        else:

            未发生异常执行的代码
        finally:

            无论是否异常，一定执行的代码
    ```

2.  作用：将程序由异常状态转换为正常流程

3.  说明：

    -   as 子句：用于绑定错误对象的变量，可省略
    -   except 子句可以有一个或多个，用来捕获某种类型的错误
    -   else 子句最多只能有一个
    -   finally 子句最多只能有一个，如果没 except 子句必须存在，如有异常没有被捕获到，会向上层（调用处）继续传递，直到程序终止运行。

```py
    def get_score():
        while True:
            try:
                num = int(input("score:"))
            except:
                print("err: input int")
                continue
            if 1 <= num <= 100:
                return num

            print("err: 1-100")
```

#### raise 语句

1.  作用：抛出一个错误，让程序进入异常状态。

2.  目的：在程序调用层数较深时，向主程序传递错误信息要层层return比较麻烦，所以建议使用人为抛出异常。

#### 自定义异常类

1.  作用：封装需要传递的错误信息。

2.  定义：

    ```py
        class 类名Error(Exception):
            def __init__(self,参数):
                super().__init__(参数)
                self.数据 = 参数
    ```

3.  调用：

    ```py
        try:
            ...
            raise 自定义异常类名（参数）
            ...
        except 自定义异常类 as 变量名：
            变量名.数据
    ```

### 迭代

> 每一次对过程的重复称之为”迭代一次”，而每一次迭代得到的结果会作为下一次迭代的初始值。例如：循环获取容器中的元素。

#### 可迭代对象 iterable

> 可迭代对象：具有 `__iter__()`方法，可以返回迭代器的对象
> 能被for循环的条件：可迭代对象（具有`__iter__()`方法的对象）

1.  语法：

    -   创建：
        ```py
            class 可迭代对象类名:
                def __iter__(self):
                    return 迭代器
        ```
    -   使用：
        ```py
            for 变量名 in 可迭代对象:
                语句
        ```

2.  原理：

```py
    # for 循环原理
    # 1.  获取迭代器对象
    iterator = list01.__iter__()

    while True:
        try:  # 如果获取所有元素，则执行 except
            # 2.  获取下一个元素（迭代过程：调用迭代器的__next__方法）
            item = iterator.__next__()
            # 3.  停止迭代：捕获 StopIteration 异常
        except StopIteration:
            break  # 跳出循环
```

#### 迭代器 iterator

> 能够被`__next__()`方法的调用并返回下一个值的对象（具有`__next__()`函数的对象，可以获取下一个元素。 ）

1.  语法：

    ```py
        class 迭代器名称:
            def __init__(self,聚合对象):
                self.聚合对象 = 聚合对象
            def __next__():
                if 没有元素:
                    raise StopIteration()  # 停止迭代
                return 聚合对象元素  #聚合对象通常是容器对象
    ```

2.  作用：使用者只需要通过一种方式(`__next__`)，便可简单明了的获取聚合对象中的各个元素，无需了解其内部结构。

3.  原理：

    ```py
        class Skill:
            pass

        class SkillIterator:
            def __init__(self, target):
                self.target = target
                self.index = 0

            def __next__(self):
                # 索引越界抛出异常
                if self.index >= len(self.target):
                    raise StopIteration()

                # 返回下一个元素
                item = self.target[self.index]
                self.index += 1
                return item

        class SkillManager:
            def __init__(self, skills):
                self.skills = skills

            def __iter__(self):
                # 创建迭代器对象 传递 需要迭代的数据
                return SkillIterator(self.skills)

        manager = SkillManager([Skill(), Skill(), Skill()])

        for item in manager:  # 获取 manager 对象中集合（聚合）类型对象元素
            print(item)

        # iterator = manager.__iter__()

        # while True:
        #     try:
        #         item = iterator.__next__()
        #         print(item)
        #     except:
        #         break
    ```

4.  设计思想：

    ![Python-MemoryAllocationMap-\_OOP03](http://images.dorc.top/blog/Python/Python-MemoryAllocationMap-_OOP03.jpg)

### 生成器 generator

1.  定义：能够动态(循环一次计算一次返回一次)提供数据的可迭代对象。

2.  作用：在循环过程中，按照某种算法推算数据，不必创建容器存储完整的结果，从而节省内存空间。数据量越大，优势越明显。

3.  惰性(延迟)操作：通俗的讲在需要的时候才计算结果。

#### 生成器函数

1.  定义：含有 yield 关键字的函数，返回值是生成器对象。

2.  语法：

    -   创建

        ```py
            def 方法名():
             …
             yield 数据
             …
        ```

    -   使用

        ```py
            for 变量名 in 方法名():

                语句
        ```

3.  本质

    -   创建

        ```py
        class 生成器名称:
            def __iter__(self):
                return 迭代器对象
        ```

    -   使用

        ```py
            生成器变量名 = 生成器名称()

            迭代器变量名 =变量名.__iter__()

            while True:

                try:

                    print(迭代器变量名.__next__())

                except:

                    break
        ```

4.  语法说明：

    -   调用生成器函数返回迭代器对象，不执行函数体。
    -   执行过程：
        1.  调用生成器函数，自动创建迭代器对象。
        2.  调用迭代器对象的`__next__()`方法才执行生成器函数体。
        3.  每次执行到yield关键字时返回数据，暂时离开。
        4.  待下次调用`__next__()`方法继续执行。
        5.  再次调用 next 方法时，从上次离开的代码开始执行，到 yield 语句暂时离开
        6.  待执行完方法体，抛出 StopIteration 异常

5.  生成迭代器对象原理：

    -   将yield关键字以前的代码放到`__next__()`方法中。
    -   将yield关键字以后的数据作为`__next__()`方法返回值。

```py
    # class MyRange:
    #     def __init__(self, stop):
    #         self.stop = stop

    #     def __iter__(self):
    #         index = 0
    #         while True:
    #             if index < self.stop:
    #                 yield index
    #                 index += 1

    def my_range(stop):
    index = 0
    while True:
        if index < stop:
            yield index
            index += 1

    for item in my_range(5):
    print(item)
```

```py
    def get_even(list_target):
        for item in list_target:
            if item % 2 == 0:
                yield item

    for item in get_even(list01):
        print(item)
    # 方法/函数需要向外返回多个结果时，使用生成器函数
```

#### 内置生成器

1.  枚举函数

    -   语法：

        ```py
            for 变量 in enumerate(可迭代对象)：
                语句
            for (索引，元素) in enumerate(可迭代对象)：
                语句
        ```

    -   作用：遍历可迭代对象时，可以将索引与元素组合为一个元组。

2.  zip

    -   语法：

        ```py
            for item in zip(可迭代对象1,可迭代对象2 ...):
                语句
        ```

    -   作用：将多个可迭代对象中对应的元素组合成一个个元组，生成元组的个数由长度最短的可迭代对象决定

#### 生成器表达式

    1.  语法：(表达式 for 变量 in 可迭代对象 [if 真值表达式])

    2.  定义：用推导式语法创建的生成器对象。

    ```py
        # def fun(list01):
        #     for item in list01:
        #         yield item ** 2

        # for item in fun(list01):
        #     print(item)

        list02 = (item ** 2 for item in list01)
        for item in list02:
            print(item)
    ```

### 函数式编程

1.  定义：用一系列函数解决问题。
    -   函数可以赋值给变量，赋值后变量绑定函数。
    -   允许将函数作为参数传入另一个函数。
    -   允许函数返回一个函数。
2.  高阶函数：将函数作为参数或返回值的函数。

#### 函数作为参数

> 将核心逻辑传入方法体，使该方法的适用性更广，体现了面向对象的开闭原则。

```py
    def fun01():
        print("fun01")

    # 将方法作为方法的参数进行传递

    def fun02(func):
        # 对于 fun02 的定义者而言，不知道也不需要知道func的具体逻辑
        print("fun02")
        func()

    # 调用 fun01 ，并将返回值 赋值给 变量a
    # a = fun01()
    # 将函数赋值给 变量a（没有执行函数）
    # a = fun01
    # a()  # 调用变量a，间接执行 函数fun01

    fun02(fun01)

    def find_list(target, condition):
        for item in target:
            # 使用形参 condition 将不变与变化隔离开
            if condition(item):
                yield item

    print(list(find_list(list01, lambda item: item > 5)))
    # 生成器直接转换成列表 使用 set() 可以去重...
```

##### lambda 表达式

-   定义：是一种匿名方法。

-   作用：作为参数传递时语法简洁，优雅，代码可读性强。随时创建和销毁，减少程序耦合度。

-   语法

    -   定义：

        ```py
            变量 = lambda 形参: 方法体
        ```

    -   调用：变量(实参)

    -   说明：

        -   形参没有可以不填
        -   方法体只能有一条语句，且不支持赋值语句。

##### 内置高阶函数

-   map（函数，可迭代对象）：使用可迭代对象中的每个元素调用函数，将返回值作为新可迭代对象元素；返回值为新可迭代对象。（ListHelp.select)

-   filter(函数，可迭代对象)：根据条件筛选可迭代对象中的元素，返回值为新可迭代对象。（ListHelp.find_all）

-   sorted(可迭代对象，key = 函数,reverse = bool值)：排序，返回值为排序结果。

-   max(可迭代对象，key = 函数)：根据函数获取可迭代对象的最大值。

-   min(可迭代对象，key = 函数)：根据函数获取可迭代对象的最小值。

#### 函数作为返回值

> 逻辑连续，当内部函数被调用时，不脱离当前的逻辑。

##### 闭包

1.  三要素：

    -   必须有一个内嵌函数。

    -   内嵌函数必须引用外部函数中变量。

    -   外部函数返回值必须是内嵌函数。

2.  定义： 在一个函数内部的函数,同时内部函数又引用了外部函数的变量。

3.  本质： 闭包是将内部函数和外部函数的执行环境绑定在一起的对象。

4.  优点：

    -   内部函数可以使用外部变量。
    -   闭包使逻辑连续

5.  缺点： 外部变量一直存在于内存中，不会在调用结束后释放，占用内存。

6.  作用：实现python装饰器

```py
    def fun01():
        print("fun01")
        a = 1

        def fun02():
            print("fun02")
            print(a)

        return fun02

    result = fun01()
    # 调用内部函数（内部函数使用了外部变量 - 闭包）
    result()  # 可以使用外部函数说明外部函数在调用后，没有释放
```

##### 函数装饰器 decorators

1.  定义： 在不改变原函数的调用以及内部代码情况下，为其添加新功能的函数。

2.  语法：

    ```py
        def 函数装饰器名称(func):

            def 内嵌函数(*args, **kwargs):

                需要添加的新功能

                return func(*args, **kwargs)

        return 内嵌函数
    ```

```py
    def print_func_name(func):
        # 包装修旧功能
        def wrapper(*args, **kwargs):
            # 增加新功能
            print(func.__name__)
            # 旧功能
            return func(*args, **kwargs)

        return wrapper  # 返回包装器

    @print_func_name  # 原理 say_hello = print_func_name(say_hello)
    def say_hello():
        print("say hello")
        return 123

    print(say_hello())
```

3.  本质： 使用 `@函数装饰器名称` 修饰原函数，等同于： `原函数名称 = 函数装饰器名称（原函数名称）` 创建与原函数名称相同的变量，关联内嵌函数；故调用原函数时执行内嵌函数。

4.  装饰器链： 一个函数可以被多个装饰器修饰，执行顺序为从近到远

5.  实战

    ```py
        import time

        def print_execute_time(func):
            def wrapper(*args, **kwargs):
                old_time = time.time()
                result = func(*args, **kwargs)
                time.time() - old_time
                print(time.time() - old_time)
                return result

            return wrapper

        class Student:
            def __init__(self, name):
                self.name = name

            @print_execute_time
            def study(self):
                print("study")
                time.sleep(2)

        s01 = Student("zf")
        s01.study()
    ```

# 网络编程

## 数据结构

1.  数据：信息的载体，能输入到计算机中并且能被计算机识别/存储/处理的符号总称。
2.  数据元素：数据的基本单位，又称记录（Record）, 一般数据元素由若干基本项（段/域/属性）组成
3.  数据结构：数据元素及数据元素之间的关系，或组成数据的形式。

### 数据结构之间的关系

1.  逻辑结构

    -   数据之间的抽象关系（邻接关系/从属关系），按每个元素可能具有的直接前趋数和直接后趋数将逻辑结构分为 线性结构 和 非线性结构。
    -   与计算机无关，对现实事物进行数学描述

2.  存储结构

    -   逻辑结构在计算机中的具体实现方式，分为顺序存储方法，链接存储方法，索引存储方法，散列存储方法
    -   计算机中组成数据的数据元素按 xx 结构存储。

#### 逻辑结构

1.  特点：

    -   只是描述数据结构中数据元素之间的联系规律
    -   从具体问题抽象出来的数学模型，是独立计算机存储器的（与机器无关）。

2.  逻辑结构分类

    -   线性结构（n个数据元素的有序集合体）
        -   集合中必须存在唯一的 一个 "第一个元素"
        -   集合中必须存在唯一的 一个 "最后的元素"
        -   除最后元素之外，其他数据元素均具有唯一的 "后继"
        -   除第一个元素之外，其他数据元素均具有唯一的 "前趋"
        -   即一个挨着一个
    -   树形结构（层次结构）
        -   数据元素间存在着 一对多 树形关系的数据结构。是一类重要的非线性数据结构。
        -   在树形结构中，树根节点没有前趋节点，其余每个节点有且只有一个前趋节点，子叶节点没有后继节点，其余每个节点的后续节点数可以是一个也可以是多个
    -   图状结构（网状结构）
        -   在图状结构中任意两个数据元素间都可能存在关系。（多对多）
    -   其他结构

#### 存储结构

1.  特点

    -   数据的逻辑结构在计算机存储器中的映象（表示）
    -   存储结构是通过计算机程序实现的，故依赖具体的计算机语言

2.  分类

    -   顺序存储
        -   将数据结构中各元素按照其逻辑顺序存放于存储器一片连续的存储空间中
    -   链式存储
        -   将数据结构中的各元素分布到存储器的不同点，用记录下一个结点位置的方式建立他们之间的联系
    -   索引存储
        -   存储数据的同时，建立一个附加的索引表，即索引存储结构 = 数据文件 + 索引表
    -   散列存储（hash）
        -   根据数据元素的特殊字段（关键字 key），计算数据元素的存放地址，然后数据元素按地址存放

3.  顺序结构 和 链式结构
    -   顺序结构适合遍历，不适合插入修改
    -   链式结构适合插入操作/大量数据的分散存储，但遍历操作稍微复杂

### 线性表

> 线性表的定义：描述其逻辑结构，通常会在线性表上进行的查找/插入/删除等操作。
>
> 线性表作为一种基本的数据结构类型，在计算机存储器中的映象一般有两种形式：顺序映象/链式映象

#### 线性表的顺序存储结构

1.  定义：将线性表的 L = （a0,a1,...an-1）中的各元素依次存储与计算机一片连续的存储空间
2.  特点：
    -   逻辑上相邻的元素，存储位置也相邻
    -   存储密度高，便于对数据的遍历查找
    -   对表的 插入/删除 等的运算效率较差
3.  程序实现：list 存放一片单一连续的内存块，list 即可描述顺序存储结构

#### 线性表的链式存储结构

1.  定义：将线性表的 L = （a0,a1,...an-1）中的各元素分布在存储器的不同存储块，称为结点，每个结点（尾部节点除外）都持有一个指向下一个结点的引用。
2.  特点：
    -   逻辑上相邻的元素，存储位置不一定相邻。
    -   存储稀疏，不必开辟整块存储空间。
    -   对表的 插入/删除 等的运算效率较高
    -   逻辑结构复杂不利于遍历
3.  程序实现:

    ```py
        class Node(object):
            def __init__(self, val, next=None):
                self.val = val
                self.next = next

        class LinkList(object):

            def __init__(self):
                self.head = Node(None)

            def init_link(self, data):
                """
                    初始化链式表
                @param data:
                @return:
                """
                p = self.head  # 可移动变量
                for i in data:
                    p.next = Node(i)
                    p = p.next

            def show(self):
                """
                    控制台输出链表
                @return:
                """
                p = self.head.next
                while p:
                    print(p.val, end=" ")
                    p = p.next
                print()

            def append(self, val):
                """
                    尾部插入新结点
                @param val:
                @return:
                """
                p = self.head
                while p.next:
                    p = p.next
                p.next = Node(val)

            def get_length(self):
                """
                    获取链表长度
                @return:
                """
                n = 0
                p = self.head
                while p.next:
                    n += 1
                    p = p.next
                return n

            def is_empty(self):
                """
                    链表是否为空
                @return:
                """
                if self.get_length():
                    return False
                return True

            def clear(self):
                """
                    清空链表
                @return:
                """
                self.head.next = None

            def get_item(self, index):
                """
                    获取索引值
                @param index:
                @return:
                """
                p = self.head.next
                n = 0

                while p:
                    if index >= self.get_length() or index < 0:
                        raise IndexError("list index out of range")
                    elif index == n:
                        return p
                    p = p.next
                    n += 1
                # while n < index and p:
                #     n += 1
                #     p = p.next
                # if not p:
                #     raise IndexError("list index out of range")
                # return p

            def insert(self, index, val):
                """
                    根据索引位置插入数据(前插)
                @param index:需要插入的索引位置
                @param val:需要插入的数值
                @return:
                """
                if index < 0 or index > self.get_length():
                    raise IndexError("list index out of range")
                p = self.head
                i = 0
                while i < index:
                    p = p.next
                    i += 1
                node_val = Node(val)
                node_val.next = p.next
                p.next = node_val
                # node_val = Node(val)
                # node_val.next = self.get_item(index) if index != self.get_length() else None
                # if index == 0:
                #     self.head.next = node_val
                # else:
                #     self.get_item(index - 1).next = node_val

            def delete(self, val):
                p = self.head
                # while p.next.val != val:
                #     if not p.next:
                #         raise IndexError("list index out of range")
                #     p = p.next
                # p.next = p.next.next
                while p.next:
                    if p.next.val == val:
                        p.next = p.next.next
                        break
                    p = p.next
                else:
                    raise ValueError("x not in list")
    ```

### 栈和队列

#### 栈

1.  定义：栈是限制在一端进行插入操作和删除操作的线性表（堆栈），允许进行操作的一端栈顶，另一固定端为栈底，栈中没有元素称之为 空栈。

2.  特点：

    -   只能在一端进行数据操作
    -   栈模型具有后进先出（的规律）

        ![Python-Net_stack](http://images.dorc.top/blog/Python/Python-Net_stack.jpg)

3.  程序实现：

    -   栈的顺序存储结构

        ```py
            class StackError(Exception):
                pass

            class SequenceStack(object):
                """
                    栈的顺序存储结构
                """

                def __init__(self):
                    self._elements = []

                def top(self):
                    if not self._elements:
                        raise StackError("Stack is empty")
                    return self._elements[-1]

                def is_empty(self):
                    return self._elements == []

                def push(self, val):
                    """
                        入栈
                    @param val:
                    @return:
                    """
                    self._elements.append(val)

                def pop(self):
                    """
                        出栈
                    @return:
                    """
                    if not self._elements:
                        raise StackError("Stack is empty")
                    return self._elements.pop()
        ```

        -   应用：一段文字的括号是否匹配

            ```py
                parens = "()[]{}"
                left_paren = "([{"
                # 使用字典做判断的介质
                opposite = {")": "(", "]": "[", "}": "{"}

                def match_parent(text):
                    i, text_len = 0, len(text)
                    while True:
                        while i < text_len and text[i] not in parens:
                            i += 1
                        if i >= text_len:
                            return
                        else:
                            yield text[i], i
                            i += 1

                def verify(data):
                    stack = SequenceStack()
                    for item, index in match_parent(data):
                        if item in left_paren:
                            stack.push((item, index))
                        elif stack.is_empty() or opposite[item] != stack.pop()[0]:
                            return "Unmatching is found at %d for %s" % (index, item)
                    else:
                        if stack.is_empty():
                            return "All parentheses are matched"
                        else:
                            e = stack.pop()
                            return "Unmatching is found at %d for %s" % (e[1], e[0])

                # def is_match(left_bracket, right_bracket):
                #     if left_bracket == "(" and right_bracket == ")":
                #         return True
                #     elif left_bracket == "[" and right_bracket == "]":
                #         return True
                #     elif left_bracket == "{" and right_bracket == "}":
                #         return True
                #     else:
                #         return False
                #
                # def detection(data):
                #     stack = SequenceStack()
                #     left_brackets = ["(", "[", "{"]
                #     right_brackets = [")", "]", "}"]
                #     for item in data:
                #         if item in left_brackets:
                #             stack.push(item)
                #         if item in right_brackets:
                #             if not is_match(stack.pop(), item):
                #                 return "error"
                #     if stack.is_empty():
                #         return "ok"
                #     return "error"
            ```

    -   栈的链式存储结构

        ```py
            class LinkStack(object):
                """
                    栈的链式存储结构
                """

                def __init__(self):
                    # 标记栈顶位置
                    self._top = None

                def is_empty(self):
                    """
                        非空验证
                    @return:
                    """
                    return not self._top

                def push(self, val):
                    """
                        入栈
                    @param val:
                    @return:
                    """
                    self._top = Node(val, self._top)
                    # node_val = Node(val)
                    # node_val.next = self._top
                    # self._top = node_val

                def pop(self):
                    """
                        弹栈
                    @return:
                    """
                    if not self._top:
                        raise StackError("stack is empty")
                    p = self._top
                    self._top = p.next
                    return p.val

                def get_top(self):
                    """
                        获取栈顶元素值
                    @return:
                    """
                    if self.is_empty():
                        raise StackError("stack is empty")
                    return self._top.val
        ```

        -   应用：逆波兰表达式

            ```py
                while True:
                    str_expression = input("dc: ")
                    list_exp_element = str_expression.split(" ")
                    for item in list_exp_element:
                        if item == "p":
                            break
                        elif item not in "+-":
                            stack.push(item)
                        else:
                            first_pop = stack.pop()
                            last_pop = stack.pop()
                            stack.push(str(eval("%s%s%s" % (last_pop, item, first_pop))))

                    print(stack.get_top())
                    stack.clear()
            ```

#### 队列

1.  定义：队列是限制在两端进行插入操作和删除操作的线性表，允许进行存入操作的一端称为"队尾"， 允许进行删除操作的一端称为"队头"。

2.  特点：

    -   队列只能在队头和队尾进行数据操作。
    -   栈模型具有先进先出/后进后出的规律

        ![Python-Net_queue](http://images.dorc.top/blog/Python/Python-Net_queue.jpg)

3.  程序实现

    -   队列的顺序存储结构

        ```py
            class SequenceQueue:
                """
                    队列的顺序存储结构
                """

                def __init__(self):
                    self._element = []

                def is_empty(self):
                    return self._element == []

                def append(self, val):
                    self._element.append(val)

                def pop(self):
                    if not self._element:
                        raise QueueError("Queue is empty")
                    return self._element.pop(0)
        ```

    -   队列的链式存储结构

        ```py
            class LinkQueue:
                """
                    队列的链式存储结构
                        左侧对头，右侧队尾
                """

                def __init__(self):
                    # Node(None) 可以是任意结点（无任何作用），一整条队列
                    # front 的作用 类似一个指针，指向队尾的前一个结点
                    self._front = self._rear = Node(None)

                def is_empty(self):
                    """
                        非空验证
                    @return:
                    """
                    return self._front is self._rear

                def append(self, val):
                    """
                        入队
                    @param val:
                    @return:
                    """
                    self._rear.next = Node(val)
                    self._rear = self._rear.next

                def pop(self):
                    """
                        出队
                    @return:
                    """
                    if self._front is self._rear:
                        raise QueueError("Queue is empty")
                    self._front = self._front.next
                    return self._front.val

                def clear(self):
                    self._front = self._rear
        ```

### 树形结构

1.  定义：

    -   树（Tree）是n（n>=0）个节点的有限集合T，它满足两个条件：有且仅有一个特定的称为根（Root）的节点，其余的节点可以分为m（m>=0）个互不相交的有限集合T1.T2 ... .Tm,其中每一个集合又是一棵树，并称为其根的子树（Subtree）。

        ![Python-Net_tree01](http://images.dorc.top/blog/Python/Python-Net_tree01.jpg)

2.  基本概念：

    -   一个节点的子树的个数称为该节点的度数（多少个分叉），一棵树的度数是指该树中节点的最大度数。
    -   度数为零的节点称为树叶或终端节点，度数不为零的节点称为分支节点，除根节点外的分支节点称为内部节点。
    -   一个节点的子树之根节点称为该节点的子节点，该节点称为它们的父节点，同一节点的各个子节点之间称为兄弟节点。一棵树的根节点没有父节点，叶节点没有子节点。
    -   一个节点系列k1,k2,...ki,ki+1,...kj，并满足ki是ki+1的父节点，就称为一条从k1到kj的路径，路径的长度为j-1，即路径中的边数，路径中前面的节点是最后节点的祖先，后面的节点是前面节点的子孙。
    -   节点的层数等于父节点的层数加一，根节点的层数定义为一，树中节点层数的最大值称为该树的高度或深度。
    -   m(m>=0)棵互不相交的树的集合称为森林，树去掉根节点就成为森林，森林加上一个新的根节点就成为树。

        ![Python-Net_tree02](http://images.dorc.top/blog/Python/Python-Net_tree02.jpg)

#### 二叉树

1.  定义：

    -   二叉树（Binary Tree）是n(n>=0)个节点的有限集合，它或者是空集(n=0),或是由一个根节点以及两棵互不相交的，分别称为左子树和右子树的二叉树组成。二叉树与普通有序树不同，二叉树严格区分左孩子和右孩子，即使只有一个子节点也要区分左右。

2.  特点：

    -   特殊的树形结构
    -   度数最多为2
    -   严格区分左子树，右子树

3.  特征：

    -   二叉树第i(i>=1)层上的节点最多为 2 的 i-1 次方个。
    -   深度为k(k>=1)的二叉树最多有 2 的 k 次方 -1 个节点。
    -   在任意一棵二叉树中，树叶的数目比度数为2的节点的数目多一。
    -   满二叉树： 深度为k(k>=1)时有 2 的 k 次方 -1 个节点的二叉树。
    -   完全二叉树：只有最下面两层有度数小于2的节点，且最下面一层的叶节点集中在最左边的若干位置上。

        ![Python-Net_tree03](http://images.dorc.top/blog/Python/Python-Net_tree03.jpg)

4.  遍历：沿某条搜索路径周游二叉树，对树中的每个节点访问一次且仅访问一次。

    -   先序遍历：先访问树根，再访问左子树，最后访问右子树；
    -   中序遍历：先访问左子树，再访问树根，最后访问右子树；
    -   后序遍历：先访问左子树，再访问右子树，最后访问树根；
    -   层次遍历：从根节点开始，逐层从左向右进行遍历。

        ```bash
            # 遇到没有遍历过的节点当作根看待
            # 遍历过程中遍历到根即写出根的值

            树形结构：
                    1
                 2     3
               4     5   6
                      7

            先根 1 2 4 3 5 7 6
            中根 4 2 1 5 7 3 6
            后根 4 2 7 5 6 3 1

            树形结构：
                    1
                 2     3
               4  5      6
                    7

            先根 1 2 4 5 7 3 6
            中根 4 2 5 7 1 3 6
            后根 4 7 5 2 6 3 1
        ```
