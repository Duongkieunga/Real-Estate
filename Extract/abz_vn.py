# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re , os, bs4, json, codecs

class Abz:

    path = "/home/nga/Documents/20193/Project/request/Datas/abz.vn"

    def walkAllFile(self):
        # i = 0
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                # i+=1
                print(filename)
                # filename = "2023.html"
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # print(os.getcwd())
                
                # return
    
    def saveFile(self, filename, info):
        # print(info)
        # with open('./Clean_datas/abz.vn/'+filename.split('.')[0]+'.txt','w') as f:
        json.dump(info, open('/home/nga/Documents/20193/Project/request/Clean_datas/abz.vn/'+filename.split('.')[0]+'.txt','w', encoding="utf8"),ensure_ascii=False)
    
    def extract(self, bs, filename):
        info = dict()
        # title-product
        try:
            element = bs.find("h1",{"class":"title-product"})
            info['title']= element.text.strip()
        except:
            print(filename)
            os.remove(self.path+'/'+filename)
            return

        # list-attr-hot clearfix
        elements = bs.find_all("ul",{"class":"list-attr-hot clearfix"})

        for element in elements:
            for item in element.findChildren(recursive=False):
                key = None
                for chil in item.find_all(text=lambda text: not isinstance(text, bs4.element.Comment), recursive=True):
                    if chil.strip() !='':
                        if key is None:
                            # print(chil.strip())
                            info[chil.strip()]=None
                            key = chil.strip()
                        # print(chil.strip())
                        else:
                            info[key] = chil.strip()
                            key = None
                            # info.append(chil.strip())

        # thong tin mo ta
        info['description']=[]
        element = bs.find("div",{"class":"ct-pr-sum"})
        for chil in element.find_all(text=lambda text: not isinstance(text, bs4.element.Comment), recursive=True):
            if chil.strip() !='':
                if chil.strip() == 'Tìm kiếm theo từ khóa:':
                    break
                # print(chil.strip())
                info['description'].append(chil.strip())

        # lien he nguoi ban
        elements = bs.find("div",{"class":"row-cl"}).find_all("div",{"class":"col-item-info row-cl"})
        for element in elements:
            items = element.find_all(text=lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            key = None
            for item in items:
                if key is None:
                    key = item.strip()
                    info[key] = None
                else:
                    info[key] = item.strip()
                    key = None
        # print(info)
        # return
        return self.saveFile(filename, info)
tvn = Abz()
tvn.walkAllFile()


    