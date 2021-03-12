import os, json, codecs
import pandas as pd 

# Trong folder Clean_datas chứa các thư mục dữ liệu đã được extract, sau khi chạy dữ liệu của mỗi folder sẽ có 1 filecsv tương ứng

class ConcatJson():
    path = "./Clean_datas/"

    def __init__(self):
        directions = ["alonhadat.com.vn"]
        for direction in directions:
            if direction == ".vscode" or direction == "data":
                continue
            if os.path.isdir(self.path+direction):
                pass
            else:
                continue
            set_page=set()
            try:
                with open("./Clean_datas/"+direction+".txt","r") as f:
                    for line in f.readlines():
                        set_page.add(line.split('\n')[0])
            except:
                create_file= open("./Clean_datas/"+direction+".txt","w")
            print(direction)
            # continue
            i = 1
            idx = 173
            path_dir = self.path+direction+"/"
            for _, _, filenames in os.walk(path_dir):
                for filename in filenames:
                    if filename in set_page:
                        continue
                    print(filename)
                    data = json.load(open(path_dir+filename,"r"))
                    columns = list(data.keys())
                    df = pd.DataFrame([data],columns=columns)
                    try:
                        df1 = pd.read_csv("./Clean_datas/data/"+direction+"/"+direction+str(idx)+".csv")
                        df = pd.concat([df1, df], ignore_index=True, sort = False)
                        # print('1')
                    except:
                        # print('2')
                        os.makedirs("./Clean_datas/data/"+direction, exist_ok=True)
                        pass
                    
                    df.to_csv("./Clean_datas/data/"+direction+"/"+direction+str(idx)+".csv", encoding='utf-8', index=False)
                    set_page.add(filename+"\n")
                    with open("./Clean_datas/"+direction+".txt","a") as f:
                        f.write(filename+"\n")
                    i += 1
                    # return
                    if i %1000 == 0:
                        idx += 1
# 68726
def ConcatCsv():
    path = "./Clean_datas/data/"
    directions = ["alonhadat.com.vn"]
    for direction in directions:
        print(direction)
        filenames = os.listdir(path + direction)
        frames=[]
        for filename in filenames:
           frames.append(pd.read_csv("./Clean_datas/data/"+direction+"/"+filename))
        res = pd.concat(frames, ignore_index=True, sort=False)
        res.to_csv("./Clean_datas/"+direction+".csv")


# c = ConcatJson()
ConcatCsv()
# print(os.getcwd())

