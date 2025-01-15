from stu_db import StuDB



def run():
    print("============欢迎来到码同学学院管理系统============")
    flag = True
    while flag:
        op = int(input('请输入你的指令:(1->新增, 2->查询, 3->修改, 4->删除, 5->查询平均分, 6->显示所有学员信息, 0->退出):'))
        if op == 1:
            # print(f"新增学员")
            stu_id = input(f"请输入学员id: ")
            name = input(f"请输入学员姓名: ")
            phone = input(f"请输入学员电话: ")
            grade = input(f"请输入学员成绩: ")
            wx = input(f"请输入学院微信: ")
            qq = input(f"请输入学员qq: ")
            sex = input(f"请输入学员性别: ")
            StuDB.add_stu(stu_id, name, phone, grade, wx, qq, sex)
        elif op == 2:
            # print(f"查询学员")
            sut_id = input(f"请输入要查询的学员id: ")
            StuDB.select_stu(sut_id)
        elif op == 3:
            # print(f"修改学员")
            stu_id = input(f"请输入要修改学员的id: ")
            # 输入信息的规则：name:张三, phone:177723,wx:lha
            info = input(f"请输入要修改的学员信息: ") # info 是一个string类型
            info_list = info.split(",")
            info_dict = {}
            for data in info_list:
                key = data.split(":")[0]
                print(key)
                value = data.split(":")[1]
                print(value)
                info_dict[key] = value
                print(info_dict)
            StuDB.change_stu(stu_id, **info_dict)
        elif op == 4:
            # print(f"删除学员")
            stu_id = input(f"请输入要删除学员的id ")
            StuDB.del_stu(stu_id)
        elif op == 5:
            StuDB.average_score()
        elif op == 0:
            flag = False
            print('退出系统')
        elif op == 6:
            StuDB.show_all()
        else:
            print(f"指令错误")


if __name__ == "__main__":
    run()