import os, shutil
# print(os.getcwd())
source =os.getcwd()+ "/Datas/chotot/101168.txt"
tar = os.getcwd()+"/Clean_datas/chotot/101168.txt"
shutil.copyfile(source, tar)
# files = os.listdir(source)
# # files=[]
# i=len(os.listdir(tar))
# # print(i)
# for f in files:
#     # if int(f.split('.')[0]) >375:
#     new = str(int(f.split('.')[0])+i)+".html"
#     # print(new)
#         # os.remove(source+f)
#     # os.rename(source+f, source+str(i)+".html")
#     os.rename(source+f, source+new)
    
#     shutil.copyfile(source+new, tar+new)
#     # i+=1
