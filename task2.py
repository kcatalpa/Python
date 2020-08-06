import keyword
print(keyword.kwlist)

class My_Class_01:
    pass
var_first_second=[]
CON_FIRST_SECOND=1

def fun_my_function01():
    pass
var_01=1
var_02=2.0
var_03=True
var_04='abc'

var_05=5<<3
var_06=var_07=1
var_08,var_00=1,2
print(var_06,type(var_06))
CON_01=1
CON_02=CON_03=1
CON_04,CON_05=1,2
# 整数类型
var_01 = 20  # 十进制
var_02 = 0b10100  #  二进制
var_03 = 0o24  #  八进制
var_04 = 0x14  #  十六进制
print(var_01,var_02,var_03,var_04)
var_05 = 1000_0000_0000
print(var_05)

# 类型转换
var_06 = int(1.23)  # 切掉小数
var_07 = int(True)  # 真 1 假 0
var_08 = int('123') # 字符串内容为数字
print(var_06,var_07,var_08 )

#  底层原理
print(var_02.bit_length())
import sys
var_09 = sys.maxsize
print(var_09)
var_10 = 9223372036854775807 + 2
print(var_10)

var_11 = 0.1
var_12 = 0.01
var_13 = var_11 - var_12
if var_11 - var_12 == 0.09:
    print('条件为真！')
    pass
print(var_13)

var_14 = 'a'    # 单行时
var_14 = "a"    # 单行时

var_14 = '''a'''  # 多行时
var_14 = """a"""    # 多行时

var_15 = 'ab12啊.。'
var_16 = '\t'
print('aaa')
print('ab\tabc')
# \回车换行
var_17 \
    = \
    123
print(var_17)
# \\ \' \"
var_18 = "ab'c"
print(var_18)
var_18 = r"ab\tc"

var_list_01 = [1,2,3]
print(var_list_01)
'''
容器类型共有的方法 
'''
var_result_01 = var_list_01 + [4,5,6]
print(var_result_01)
var_result_02 = var_list_01 * 4
print(var_result_02)

'''
切片操作
'''
var_list_01[1:1] = ['a', 'b', 'c']
print(var_list_01)

'''
容器list中的方法
'''
var_list_02 = [1,2,3]
var_list_03 = [1,2,3]
var_list_04 = [4,5,6]
var_list_02.append(4)
print(var_list_02)
var_list_04.extend(var_list_03)
print(var_list_04)


# list查找功能
'''
容器类型共有方法
'''
var_list_01 = [1,2,3,4]
var_result_01 = len(var_list_01)
var_result_02 = max(var_list_01)
var_result_03 = min(var_list_01)
print(var_result_01,var_result_02,var_result_03)
var_result_04 = 1 in var_list_01

'''
切片操作 
列表变量[值1：值2：值3] 开始 结束 步长
'''
# 0个值
var_result_05 = var_list_01[:]  # 获取所有元素
var_result_06 = var_list_01[3]  # 获取索引值
var_result_07 = var_list_01[2::]  # 获取索引及之后的值
var_result_08 = var_list_01[0:3]  # 默认步长为1 左闭右开
var_result_09 = var_list_01[-1:-5:-1] # 倒叙
var_result_10 = var_list_01[::-1]
print(var_result_09,var_result_10)

'''
list自带方法
'''
var_list_01 = [1,2,3,4,1,2,1]
var_result_01 = var_list_01.count(1)
var_result_02 = var_list_01.index(2)
print(var_result_01,var_result_02)

# 修改
'''
切片
'''
var_list_01=[1,2,3,'a','b','c']
var_list_01[3] = 4
print(var_list_01)
'''
list自带方法  排序
'''
var_list_02 = [1,1,6,3,0,4]
var_list_02.sort(reverse=True)  # 同种类型才可排序
print(var_list_02)

var_list_03 = ['a','b','c',1,2,3]
var_list_03.reverse()
print(var_list_03)

# 删除
var_list_01 = [1,2,3,4,5]
'''
切片
'''
del var_list_01[0]
print(var_list_01)
'''
list 自带函数
'''
var_02 = [1,2,3,4,5,1,2]
var_02.remove(1)
print(var_02)
var_02.pop(1)
print(var_02)
var_02.pop()
print(var_02)
var_02.clear()
print(var_02)






