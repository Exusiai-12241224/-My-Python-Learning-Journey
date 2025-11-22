# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#介绍程序可以解决的问题
print("这是一个帮您解决鸡兔同笼问题的程序喵，接下来可以输入设定的头的数量还有脚的数量噢")
#收录数据
heads = int(input("头有多少个呢~："))
legs = int(input("脚有多少只呀~："))
#分情况讨论
##脚的数量不是双数
if legs % 2 :
    print("铸币！脚的数量要为双数哇！！！")
##脚太少或者头太多
elif legs < 2 * heads:
    print("这不对吧，脚太少了，是你肚子饿了把鸡脚啃了吗？")
##脚太多
elif legs > 4 * heads:
    print("这不对吧，全是兔子也没那么多脚啊！！！")
##正常情况
else:
    rabbits = (legs - 2 * heads) // 2
    chickens = heads - rabbits
#输出结果
    print(f"鸡有 {chickens} 只，兔有 {rabbits} 只。")
