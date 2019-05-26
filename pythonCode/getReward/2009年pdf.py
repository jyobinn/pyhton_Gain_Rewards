
#-*- conding: utf-8 -*-

import tabula

df = tabula.read_pdf("http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2009/jldh09jlgg/201001/P020100112447134382767.pdf", encoding='gbk', pages='all')
print(df)
for indexs in df.index:
    # 遍历打印企业名称
    print(df.loc[indexs].values[1].strip())