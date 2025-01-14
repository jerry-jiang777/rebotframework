from student import Student
class StuDB():
    stus_dict = {}

    @classmethod
    def add_stu(cls,stu_id, name, phone, wx = "", qq = "", sex = ""):
        if stu_id in  cls.stus_dict:
            print(f"{stu_id} 已存在, 不能添加")
            return
        else:
            stu1 = Student(stu_id, name, phone, wx, sex)
            cls.stus_dict[stu_id] = stu1
            print(f"添加成功")
            return
        
    @classmethod
    def select_stu(cls, stu_id):
        if stu_id in cls.stus_dict:
            STU = cls.stus_dict[stu_id]
            print(f"{STU.show_info()}")
            return
        else:
            print(f"{stu_id} 不存在！")

    @classmethod
    def del_stu(cls, stu_id):
        if stu_id in cls.stus_dict:
            del cls.stus_dict[stu_id]
            print(f"删除学号为{stu_id}的学生信息.")
            return
        else:
            print(f"学号为{stu_id}学生信息不存在.")
            return
        
if __name__ == "__main__":
    StuDB.add_stu("1", 'Alice', "15648769645")
    StuDB.add_stu("2", 'Jerry', "17749212035", wx = "wx001", sex = "男")
    StuDB.add_stu("1", 'Ady', "2458961423")
    print(StuDB.stus_dict)
    StuDB.select_stu("1")
    StuDB.select_stu("3")
    StuDB.del_stu("6")
    StuDB.del_stu("2")
    print(StuDB.stus_dict)