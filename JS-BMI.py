def JS_bmi(H,W):
    '''计算BMI指数
       H：身高，单位：米
       W：体重，单位：千克
    '''
    bmi=W/(H*H)
    print( "您的BMI指数为："+str(bmi))
    if bmi<18.5:
        print("您的体重太轻了杂鱼~")
    if bmi>=18.5 and bmi<24.9:
        print("还不赖嘛，在正常范围内")
    if bmi>=24.9 and bmi<29.9:
        print("您的体重太重了，再不控制饮食要变成大胃袋了！")
    if bmi>=29.9:
        print("你真是大菲柱！！！已经有大胃袋了就快点控制一下吧！！！")
H=float(input('请输入您的身高（单位：米）：'))
W=float(input('请输入您的体重（单位：千克）：'))
print(JS_bmi( H, W))