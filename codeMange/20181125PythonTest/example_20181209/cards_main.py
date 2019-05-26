import example_20181209.cards_tools
while True:
    # TODO 显示功能菜单
    example_20181209.cards_tools.showMenu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # pass
        if action_str == "1":
            # 新增
            pass
        elif action_str == "1":
            # 查询
            pass
        elif action_str == "1":
            # 修改
            pass
    elif action_str == "0":
        # 退出本系統
        print("本次使用结束，请下次再来")
        # pass
        break
    else:
        print("输入错误")
