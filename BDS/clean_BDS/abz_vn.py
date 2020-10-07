# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re , os, bs4, json, codecs

class Abz:

    path = os.getcwd()+ "/Datas/abz.vn"

    def walkAllFile(self):
        # i = 0
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                # i+=1
                # print(filename)
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # print(os.getcwd())
                
                # return
    
    def saveFile(self, filename, info):
        # with open('./Clean_datas/abz.vn/'+filename.split('.')[0]+'.txt','w') as f:
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)
    
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
            key = None
            for chil in element.find_all(text=lambda text: not isinstance(text, bs4.element.Comment), recursive=True):
                if chil.strip() !='':
                    if key is None:
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
        element = bs.find("div",{"class":"row-cl"})
        key = None
        for chil in element.find_all(text=lambda text: not isinstance(text, bs4.element.Comment), recursive=True):
            if chil.strip() !='':
                # print(chil.strip())
                if key is None:
                    info[chil.strip()] = None
                    key = chil.strip()
                else:
                    info[key] = chil.strip()
                    key = None
        # print(info)
        # return
        return self.saveFile(filename, info)
tvn = Abz()
tvn.walkAllFile()


    