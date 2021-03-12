import os, json, shutil

def run():
    targe = "Datas/data/"
    path = "Datas/"
    i = 8800
    for direction in os.listdir(path):
        path_dir = path+"abz.vn"+"/"
        # print(direction)
        for _, _, filenames in os.walk(path_dir):
            for filename in filenames:
                
                
                if i >13000:
                    return
                try:
                    shutil.copyfile(path_dir+filename, targe+filename)
                    print(filename)
                except:
                    pass
                i +=1
run()