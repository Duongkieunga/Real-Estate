# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re , os, bs4, json, codecs

class Alonhadat:

    # path = os.getcwd()+ "../Datas/alonhadat.com.vn"
    path = "/home/nga/Documents/20193/Project/request/Datas/alonhadat.com.vn"
    # canonical
    def __init__(self):
        pass

    def walkAllFile(self):
        # i = 0
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                # i+=1
                print(filename)
                # filename = "9485.html"
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # print(os.getcwd())
                
                # return
    
    def saveFile(self, filename, info):
        # with open('./Clean_datas/alonhadat.com.vn/'+filename.split('.')[0]+'.txt','w') as f:
        json.dump(info, codecs.open('/home/nga/Documents/20193/Project/request/Clean_datas/alonhadat.com.vn/'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)
    
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
                    info[chil.split(':')[0].strip()] = chil.split(":")[1].strip()
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
        elements = bs.find("div",{"class":"moreinfor"})
        for element in elements.findChildren(recursive=False):
            if element.name == 'span':
                items = element.find_all(text= lambda text:( not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
                try:
                    info[items[0].strip()] = ' '.join([item.strip() for item in items[1:]])
                except:
                    info[items[0].strip()]=None

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
        elements = bs.find("div",{"class":"moreinfor1"}).find_all("td")
        key = None
        for element in elements:
            if key is None:
                key = element.text.strip()
                info[key]= None
            else:
                if (element.text.strip() == '') or ('_' in element.text.strip()) or ('-' in element.text.strip()):
                    pass
                else:
                    info[key] = element.text.strip()
                key = None

        # print(info)
        # return
        return self.saveFile(filename, info)
tvn = Alonhadat()
tvn.walkAllFile()


    