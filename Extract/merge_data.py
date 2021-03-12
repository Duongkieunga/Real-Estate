import os, shutil
path = os.getcwd() + '/Clean_datas/'
tar = os.getcwd() +"/clean/clean/"
count = 0
for dir in os.listdir(path):
    filenames = sorted(os.listdir(path+dir+'/'), reverse=True, key=lambda x: int(x.split('.')[0]))
    # for filename in filenames:
    #     new = str(int(filename.split('.')[0])+count)+'.txt'
    #     shutil.copyfile(path+dir+'/'+filename, tar+new)
    # # break
    # count += len(filenames)
    print(len(filenames), dir)


# import os, shutil
# path = os.getcwd() + '/Datas/'
# tar = os.getcwd() +"/clean/origin/"
# count = 0
# dirs=['muaban.net', 'rongbay.com', 'muabannhadat.vn', 'dothi.net', 'vndiaoc.com', 'abz.vn', 'batdongsan.vn', 'nhadat.net', 'batdongsan321.com', 'homedy.com', 'alonhadat.com.vn']
# for dir in dirs:
#     try:
#         filenames = sorted(os.listdir(path+dir+'/'), reverse=True, key=lambda x: int(x.split('.')[0]))
#         for filename in filenames:
#             new = str(int(filename.split('.')[0])+count)+'.html'
#             shutil.copyfile(path+dir+'/'+filename, tar+new)
#     except:
#         filenames = sorted(os.listdir(path+dir+'/bietthulienke/'), reverse=True, key=lambda x: int(x.split('.')[0]))
#         for filename in filenames:
#             new = str(int(filename.split('.')[0])+count)+'.html'
#             shutil.copyfile(path+dir+'/bietthulienke/'+filename, tar+new)
#     # break
#     count += len(filenames)
#     print(len(filenames), dir)
