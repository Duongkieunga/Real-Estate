# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re , os, bs4, json, codecs

class Alonhadat:

    path = os.getcwd()+ "/Datas/alonhadat.com.vn"
    # canonical
    def __init__(self):
        pass

    def walkAllFile(self):
        # i = 0
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                # i+=1
                print(filename)
                # filename = "165.html"
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # print(os.getcwd())
                
                # return
    
    def saveFile(self, filename, info):
        # with open('./Clean_datas/alonhadat.com.vn/'+filename.split('.')[0]+'.txt','w') as f:
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)
    
    def extract(self, bs, filename):
        info = dict()
        # title
        element = bs.find("div",{"class":"title"})
        i=1
        for chil in element.find_all(text=lambda  text: not isinstance(text, bs4.element.Comment), recursive=True):
            if chil.strip() != '':
                if i ==1 :
                    info['title']= chil.strip()
                    i+=1
                else:
                    info[chil.split(':')[0]] = chil.split(":")[1].strip()
                # print(chil.strip())
                # info.append(chil.strip())
        
        # detail text-content, detail
        try:
            info['description'] = []
            element = bs.find("div",{"class":"detail text-content"})
            info['description'].append(element.text.strip())
        except:
            element = bs.find("div",{"class":"detail"})
            for chil in element.find_all(text=lambda  text: not isinstance(text, bs4.element.Comment), recursive=True):
                if chil.strip() != '':
                    # print(chil.strip())
                    info['description'].append(chil.strip())

        # moreinfor
        element = bs.find("div",{"class":"moreinfor"})
        key = None
        for chil in element.find_all(text= lambda text: not isinstance(text, bs4.element.Comment), recursive=True):
            if chil.strip() != '':
                if key is None:
                    info[chil.strip()] = None
                    key = chil.strip()
                else:
                    info[key] = chil.strip()
                    key = None
                # info.append(chil.strip())
        # address
        element = bs.find("div",{"class":"address"})
        key = None
        for chil in element.find_all(text= lambda text: not isinstance(text, bs4.element.Comment), recursive=True):
            if chil.strip() != '':
                if key is None:
                    info[chil.strip()] = None
                    key = chil.strip()
                else:
                    info[key] = chil.strip()
                    key = None
        # moreinfor1
        element = bs.find("div",{"class":"moreinfor1"})
        key = None
        for chil in element.find_all(text= lambda text: not isinstance(text, bs4.element.Comment), recursive=True):
            if chil.strip() != '':
                if 'Các thông tin khác' in chil.strip():
                    continue
                if key is None:
                    info[chil.strip()] = None
                    key = chil.strip()
                else:
                    if ('_' in chil.strip()) or ('-' in chil.strip()):
                        info[key] = None
                        key = None
                        continue
                    info[key] = chil.strip()
                    key = None
        # print(info)
        # return
        return self.saveFile(filename, info)
tvn = Alonhadat()
tvn.walkAllFile()


    