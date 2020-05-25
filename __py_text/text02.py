"""
    text02
"""
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
