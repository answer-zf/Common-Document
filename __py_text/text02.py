"""
    
"""

list01 = [2, 34, 67, 8, 90]

list02 = (item for item in list01 if item > 10)
list03 = [item for item in list01 if item > 10]

for item in list02:
    print(item)
