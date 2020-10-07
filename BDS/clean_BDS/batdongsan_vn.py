import os, bs4 , json, codecs
from bs4 import BeautifulSoup

class Batdongsan:
    path = "/home/nga/Documents/20193/Project/request/Datas/batdongsan.vn"
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                # print(filename)
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # return

    def saveFile(self, filename, info):
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        if ('HTTP Error 400' in bs.text) or ('We found too much access from viruses or DDOS to our website' in bs.text):
            print(filename)
            return
        info = dict()

        # title
        info['title'] = bs.find("div",{"class":"P_Title1 hidden-xs"}).text.strip()
        # postDate
        info['postDate'] = bs.find("div",{"class":"detail-share"}).text.strip().split('\n')[0]
        # --------
        element = bs.find("div",{'class':"PD_Thongso col-md-5 col-md-push-7"}).findChildren(recursive=False)[0]
        # print(element)
        for chil in element.findChildren(recursive=False)[:-1]:
            items = chil.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            value = ""
            for item in items[1:]:
                value += item.strip()
            info[items[0].strip()] = value
        
        try:
            for chil in element.findChildren(recursive=False)[-1].find("ul",{"class":"attribute"}).findChildren(recursive=False):
                items = chil.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
                value = ""
                for item in items[1:]:
                    value += item.strip()
                info[items[0].strip()] = value
        except:
            pass
        
        # mo ta
        info['description'] = ""
        element = bs.find("div",{"class":"PD_Gioithieu col-md-7 col-md-pull-5"})
        for chil in element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() !=''), recursive=True):
            info['description'] += chil.strip()+"\n"
        
        
        # contact

        element = bs.find("div",{"class":"webpartbodycontrol webpartbodycontrol_50302"})
        for chil in element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() !=''), recursive=True):
            try:
                info[chil.parent.get("class")[0]] = chil.strip()
                # print(chil.strip(), chil.parent.get("class"))
            except:
                if len(chil.parent.parent.get("class"))>1:
                    info[chil.parent.parent.parent.get("class")[0]] = chil.strip()
                    continue
                info[chil.parent.parent.get("class")[0]] = chil.strip()
                # print('- ',chil.strip(), chil.parent.parent.get("class"))
        # return
        return self.saveFile(filename, info)

bds = Batdongsan()