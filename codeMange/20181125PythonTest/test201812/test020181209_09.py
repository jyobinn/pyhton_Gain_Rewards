def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_list = (1, 2, 3)
gl_dict = {"name": "小妹", "old": 18}
demo(gl_list, gl_dict)
# 拆包
demo(*gl_list, **gl_dict)
