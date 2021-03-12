import json, os, codecs

class Chotot:
    path = os.getcwd()+ "/Datas/"
    directions = ["chotot2", "chotot"]

    def __init__(self):
        self.set_id = set()
        with open("./clean/set_id_chotot.txt","r") as f:
            for line in f.readlines():
                self.set_id.add(line.split('\n')[0])
        i = 0
        for direction in self.directions:
            print(direction)
            for _,_, filenames in os.walk(self.path+direction):
                for filename in filenames:
                    print(filename)
                    # filename = "32122.txt"
                    self.extract(json.load(open(self.path+direction+'/'+filename, "r")), filename, direction)
                    i +=1
                    # if i >4:
                    #     return
                    # return
    
    def extract(self, data, filename, direction):
        # print(data)
        if str(data['ad']['list_id']) in self.set_id:
            return
        
        info= dict()
        for key1 in list(data.keys()):
            try:
                remove_key = ['property_status','ad_id','date','account_id','account_oid','area','region','category','type','reviewer_image','number_of_images','thumbnail_image','avatar','region_v2','area_v2','ward','street_id','house_type','streetnumber_display','unitnumber_display','contain_videos','images','reviewer_nickname']
                for key2 in data[key1].keys():
                    if key2 in remove_key:
                        continue
                    try:
                        info[key2] = data[key1][key2]['value']
                    except:
                        info[key2] = data[key1][key2]
            except:
        
                for idx in range(len(data[key1])):
                    try:
                        info[data[key1][idx]['id']]= data[key1][idx]['value']
                    except:
                        pass
                    # print(data[key1][idx]['id'], data[key1][idx]['value'])
        # print('----------------------\n\n')
        # print(info)
        with open("./clean/set_id_chotot.txt","a") as f:
            f.write(str(data['ad']['list_id'])+"\n")
            self.set_id.add(str(data['ad']['list_id']))
        self.saveFile(info, filename, direction)
    
    def saveFile(self, info, filename, direction):
        try:
            json.dump(info, codecs.open('./Clean_datas/'+direction+'/'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)
        except:
            os.makedirs(self.path+'/Clean_datas/'+ direction, exist_ok = True)
            json.dump(info, codecs.open('./Clean_datas/'+direction+'/'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

c = Chotot()