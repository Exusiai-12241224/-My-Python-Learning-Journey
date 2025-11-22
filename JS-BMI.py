#定义计算BMI的函数
def JS_bmi(H,W):
    '''计算BMI指数
       H：身高，单位：米
       W：体重，单位：千克
    '''
    bmi=W/(H*H)
    #输出BMI指数
    print( "你的BMI指数为："+str(bmi))
    #反馈BMI指数的情况
    if bmi<18.5:
        print("你的体重太轻了杂鱼~")
    if bmi>=18.5 and bmi<24.9:
        print("还不赖嘛，在正常范围内")
    if bmi>=24.9 and bmi<29.9:
        print("你的体重太重了，再不控制饮食要变成大胃袋了！")
    if bmi>=29.9:
        print("你真是大菲柱！！！已经有大胃袋了就快点控制一下吧！！！")
#收录数据
H=float(input('请输入您的身高（单位：米）：'))
W=float(input('请输入您的体重（单位：千克）：'))
#输出结果
print(JS_bmi( H, W))