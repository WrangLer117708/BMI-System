#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

Info = {} # 建立一个存储学生信息的字典
def print_home_page():
    # 定义HOMEPAGE
    print("="*50)
    print('~~~~主菜单~~~~')
    menu = ('1.录入','2.查询','3.修改','4.删除','5.预览','6.退出')
    for feature in menu:
        print(feature)
    print("="*50)

def key_get():
    # 获取用户输入的序号
    key = int(input("请输入功能对应的数字: "))
    return choose_func(key)

def choose_func(key):
    # 这是选择功能的函数，之所以不和key-get放一起是我想在以后增加功能方便更改
    if key == 1:
        add_stu_info(key)  # 添加学生
    elif key == 2:
        query_stu_info(key)  # 查询一个学生的信息
    elif key == 3:
        modify_stu_info(key)  # 修改学生信息
    elif key == 4:
        delete_stu_info(key)  # 删除学生信息
    elif key == 5:
        show_stu_info(key)   # 显示所有学生信息
    elif key == 6:
        exit()
    else:
        print("输入有误，请重新输入")
        return key_get()

def add_stu_info(i):
    # 录入学生信息并计算BMI值
    name = input("请输入学生姓名: ")
    height = float(input ("请输入学生身高(M): "))
    weight = float(input("请输入学生的体重(Kg): "))
    BMI = weight / (height*height)
    
    stu_info = {}
    stu_info['name'] = name
    stu_info['weight'] = weight
    stu_info['height'] = height
    stu_info['BMI'] = BMI
    if stu_info['BMI'] <=18.5:
        print('$s的BMI指数为%.1f,偏瘦。要多吃肉!' %(name,stu_info['BMI']))
        stu_info['evaluate']='偏瘦。要多吃肉!'
    elif stu_info['BMI'] <=25:
        print('%s的BMI指数为%.1f，标准。迷人身材！' % (name, stu_info['BMI']))
        stu_info['evaluate'] = '标准。迷人身材！'
    elif stu_info['BMI'] <=28:
        print('%s的BMI指数为%.1f, 过重。肉肉哒，要管住嘴！' % (name, stu_info['BMI']))
        stu_info['evaluate'] = '过重。肉肉哒，要管住嘴！'
    elif stu_info['BMI']<=32:
        print('%s的BMI指数为%.1f，肥胖。迈开腿去运动吧！' % (name, stu_info['BMI']))
        stu_info['evaluate'] = '肥胖。迈开腿去运动吧！'
    else:
        print('%s的BMI指数为%.0f，超重。最讨厌的死肥宅!' % (name, stu_info['BMI']))
        stu_info['evaluate'] = '超重。最讨厌的死肥宅!'
    Info[name] = stu_info
    return pause(i)

def query_stu_info(i):
    # 查询学生信息
    stu_name = input("请输入查询学生的姓名: ")
    print("--"*25)
    print("学生: %s的信息如下" % stu_name)
    print("姓名    身高    体重    BMI    评语") 
    print("%3s    %.2f    %.2f    %.3f    %s"
        % (Info[stu_name]['name'],Info[stu_name]['height'],Info[stu_name]['weight'],
        Info[stu_name]['BMI'],Info[stu_name]['evaluate']))
    print("--"*25)
    return pause(i)

def modify_stu_info(i):
    # 修改学生信息
    name = input("请输入要修改的学生的姓名")
    print("--"*25)
    print("学生: %s的信息如下" %name)
    print("姓名    身高    体重    BMI    评语")
    print("%3s    %.2f    %.2f    %.3f    %s"
        % (Info[name]['name'],Info[name]['height'],Info[name]['weight'],
        Info[name]['BMI'],Info[name]['evaluate']))
    print("--"*25)
    print("修改开始")
    height = float(input('请输入学生的身高(M) :'))
    weight = float(input ('请输入学生的体重(Kg) :'))
    BMI = weight / (height*height)
    stu_info = {}
    stu_info['name'] = name
    stu_info['height'] = height
    stu_info['weight'] = weight
    stu_info['BMI'] = BMI
    if stu_info['BMI'] <= 18.5:
        print('%s的BMI指数为%.1f,偏瘦。要多吃肉!' %(name,stu_info['BMI']))
        stu_info['evaluate'] = '偏瘦。要多吃肉！'
    elif stu_info['BMI'] <= 25:
        print('%s的BMI指数为%.1f，标准。迷人身材！' % (name, 
        stu_info['BMI']))
        stu_info['evaluate'] = '标准。迷人身材！'
    elif stu_info['BMI'] <= 28:
        print('%s的BMI指数为%.1f, 过重。肉肉哒，要管住嘴！' 
        % (name,  stu_info['BMI']))
        stu_info['evaluate'] = '过重。肉肉哒，要管住嘴！'
    elif stu_info['BMI'] <= 32:
        print('%s的BMI指数为%.1f，肥胖。迈开腿去运动吧！' 
        % (name, stu_info['BMI']))
        stu_info['evaluate'] = '肥胖。迈开腿去运动吧！'
    else:
        print('%s的BMI指数为%.0f，超重。最讨厌的死肥宅!' 
        % (name, stu_info['BMI']))
        stu_info['evaluate'] = '超重。最讨厌的死肥宅!'
    Info[name] = stu_info
    return pause(i)

def delete_stu_info(i):
    # 删除学生信息
    del_name = input("请输入要删除的学生姓名")
    del Info[del_name]
    return pause(i)

def show_stu_info(i):
    # 预览学生信息
    print("--"*25)
    print("学生的信息如下")
    print("姓名    身高    体重    BMI    评语")
    for stu_name in Info:
        print("%3s    %.2f    %.2f    %.3f    %s"
            % (Info[stu_name]['name'],Info[stu_name]['height'],
            Info[stu_name]['weight'],Info[stu_name]['BMI'],
            Info[stu_name]['evaluate']))
    print("--"*25)
    return pause(i)

def pause(i):
    # 这是当功能完成后的一个小判断
    temp = input("操作成功！输入1继续操作,任意键返回主菜单。")
    if temp == 1:
        if i == 1:
            add_stu_info(int(i))   # 添加学生
        elif i == 2:
            query_stu_info(int(i))  # 查询一个学生的信息
        elif i == 3:
            modify_stu_info(int(i))  # 修改学生信息
        elif i == 4:
            delete_stu_info(int(i))   # 删除学生的信息
    else:
        return main()

def main():
    # 这是主函数
    print_home_page()   # 打印菜单
    key_get()


main()
