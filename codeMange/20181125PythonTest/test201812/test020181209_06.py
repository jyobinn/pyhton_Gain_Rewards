"""
缺省参数
"""
def print_infor(name, gender=True):
    """
    输出信息
    :param name: 姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s是%s" % (name, gender_text))


print_infor("aa", True)
print_infor("aa", False)
print_infor("aa")
