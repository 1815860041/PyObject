#布尔值的三种使用情况
#两个值在互相比较时
weather = input('请回答：你今天开心吗')
if weather == '开心':
    print('我也替你开心。')
#数值本身作为一个条件，被判断真假。
if '开心':
    print(108)
if '':
    print(108)
if 1:
    print(108)
#布尔值的运算
#国师的要求，二选一
v1 = input('对方是达官显贵吗？是/否：')
v2 = input('对方是富可敌国吗？是/否：')
if v1 == '是' or v2 == '是':
    print('国师的要求通过了')
else:
    print('国师的要求没通过')
#女王的要求，都满足
v3 = input('对方善良吗？是/否：')
v4 = input('对方好看吗？是/否：')
if v3 == '是' and v4 == '是':
    print('女王的要求通过了')
else:
    print('女王的要求没通过')
