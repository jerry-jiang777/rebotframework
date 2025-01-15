from student import Student


class StuDB():
    stus_dict = {}

    @classmethod
    def add_stu(cls,stu_id, name, phone, grade, wx = "", qq = "", sex = ""):
        if stu_id in  cls.stus_dict:
            print(f"{stu_id} 已存在, 不能添加")
        else:
            stu1 = Student(stu_id, name, phone, grade, wx, qq, sex)
            cls.stus_dict[stu_id] = stu1
            print(f"添加成功")
        
    @classmethod
    def select_stu(cls, stu_id):
        if stu_id in cls.stus_dict:
            STU = cls.stus_dict[stu_id]
            print(f"{STU.show_info()}")
        else:
            print(f"{stu_id} 不存在！")

    @classmethod
    def del_stu(cls, stu_id):
        if stu_id in cls.stus_dict:
            del cls.stus_dict[stu_id]
            print(f"删除学号为{stu_id}的学生信息.")
        else:
            print(f"学号为{stu_id}学生信息不存在.")

    

    @classmethod
    def change_stu(cls, stu_id, **kwargs):
        if stu_id in cls.stus_dict:
            stu = cls.stus_dict[stu_id]
            if "name" in kwargs:
                stu.name = kwargs["name"]
            if 'phone' in kwargs:
                stu.phone = kwargs['phone']
            if 'grade' in kwargs:
                stu.grade = kwargs['grade']
            if 'wx' in kwargs:
                stu.wx = kwargs['wx']
            if 'qq' in kwargs:
                stu.qq = kwargs['qq']
            if 'sex' in kwargs:
                stu.sex = kwargs['sex']
        else:
            print(f"学号 {stu_id} 不存在！")
    @classmethod
    def average_score(cls):
        scores = 0
        total = 0
        for index in cls.stus_dict.keys():
            stu_info = cls.stus_dict[index]
            stu_score = stu_info.grade
            int_stu_scores = int(stu_score)
            # print(int_stu_scores)
            scores += int_stu_scores
            total += 1
        avg_scores = scores / total
        print(f"全班总人数为 {total}, 平均分数: {avg_scores}")
    
    @classmethod
    def show_all(cls):
        for stu in cls.stus_dict.values():
            stu.show_info()

if __name__ == "__main__":
    StuDB.add_stu("1", 'Alice', "15648769645", "100")
    StuDB.add_stu("2", 'Jerry', "17749212035", "80", wx = "wx001", sex = "男")
    StuDB.add_stu("1", 'Ady', "2458961423", "100")
    print(StuDB.stus_dict)
    StuDB.select_stu("1")
    StuDB.select_stu("3")
    StuDB.del_stu("6")
    StuDB.del_stu("2")
    print(StuDB.stus_dict)
    StuDB.change_stu(stu_id= "1", name = "cici", phone = "123456789", wx = "jerry777")
    print(StuDB.select_stu("2"))
    StuDB.average_score()