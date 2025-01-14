class Student():
    def __init__(self,stu_id, name, phone, wx=' ', qq=' ', sex=' '):
        self.stu_id = stu_id
        self.name = name
        self.phone = phone
        self.wx = wx
        self.qq = qq
        self.sex = sex

    def show_info(self):
        return f"学号: {self.stu_id}, 姓名: {self.name}, 电话: {self.phone}, 微信号: {self.wx}, qq号: {self.qq}, 性别: {self.sex}"
    

if __name__ == "__main__":
    stu1 = Student("1", "Alice", "17846123362", "wx001")
    print(stu1.show_info())
    stu2 = Student("2", "Mecon", "17846118592", qq="qq01")
    print(stu2.show_info())
