import os

from xlwt import Workbook


def create(titleName, **dict):
    realJ = 100
    w = Workbook()  # 创建一个工作簿
    for k in dict.keys():
        ws = w.add_sheet(k)  # 创建一个工作表
        i = 0
        v = dict[k]
        for list in v:
            j = 0
            for value in list:
                # value = value.replace("\n", "").replace("\n", "").strip()
                # 判断是不是名称，是就不去掉中间空格
                if value.endswith('名称'):
                    realJ = j

                if realJ == j:
                    # 去掉两边空格
                    value = value.replace("\t", "").replace("\r", "").replace("\n", "").strip()
                else:
                    # 去掉全部空格
                    value = value.replace("\t", "").replace("\r", "").replace("\n", "").strip().replace(' ', '').replace(' ', '').replace('　', '')
                ws.write(i, j, value)
                j = j + 1
            i = i + 1
    cur_dir = os.getcwd()  # get current path
    folder_name = 'excel'
    dir_new = os.path.join(cur_dir, folder_name)
    if os.path.isdir(cur_dir):
        if not os.path.exists(dir_new):
            path = os.mkdir(dir_new)
    w.save(r"" + dir_new + "\\" + titleName + '.xls')


def getSign():
    return "、"

if __name__ == '__main__':
    list1 = ['1', '2', '3', '4']
    list2 = ['7', '8', '9', '10']
    list3 = ['1', '2', '3', '4']
    list4 = ['7', '8', '9', '10']
    list5 = []
    list5.append(list1)
    list5.append(list2)
    list5.append(list3)
    list5.append(list4)
    dict = {"diyi": list5, "sad": list5}
    create("XXsadA", **dict)
