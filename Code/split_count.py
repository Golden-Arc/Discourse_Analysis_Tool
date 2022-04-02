import re
import os
path = r"C:\Users\Golden Arc\Desktop\大创\标注体系\标注2.0\1+4+社交+性别" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
with open("./result_dataline.txt",'a',encoding='utf8') as w:
    for file in files: #遍历文件夹
        position = path+'\\'+ file #构造绝对路径，"\\"，其中一个'\'为转义符
        w.write(position+'\n')           
        with open(position,'r',encoding='utf8') as f:
            cont = True
            li = []
            while cont:
                cont = f.readline()
                li.append(cont)
                if cont =='\n':# 读取到空行时，则对此空行到上一空行之间的文本进行提取分析
                    match_tag = re.findall(r"\<ITR\>", str(li)) # 搜索包含ITR的对话块
                    if(len(match_tag)>= 1):
                        # w.write(str(li)+'\n')
                        match_result={}
                        first_tag = re.findall(r"\<.*?\>", str(li)) # 如果对话块中ITR的个数大于1，则提取该块中所有包含在<>中的内容
                        for key in first_tag:
                            match_result[key] = match_result.get(key, 0) + 1
                        w.write(str(match_result)+'\n')
                    li = []