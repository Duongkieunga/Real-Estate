import os, bs4 , json, codecs
from bs4 import BeautifulSoup

class Batdongsan321:
    path = "/home/nga/Documents/20193/Project/request/Datas/batdongsan321.com"
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                print(filename)
                # filename='91.html'
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # return

    def saveFile(self, filename, info):
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        info = dict()
        # title 
        info['title'] = bs.find("h1",{"class":"re-title"}).text.strip()
        # re-district, type
        info['re-district'] = ""
        element = bs.find("div",{"class":"re-district"})
        for chil in element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True):
            info['re-district'] += chil.strip()+'\n'
        # price
        info['Giá:'] = bs.find("div",{"class":"re-price"}).text.split('Giá:')[1].strip().replace('\n               \n              ','')
        # contact
        element = bs.find("div",{'class':'info'})
        for chil in element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True):
            info[chil.parent.get("class")[0]] = chil.strip()
        # -------
        element = bs.find("ul",{"class":"re-property"}).find_all("li")
        for chil in element:
            try:
                items = chil.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
                value = items[0].strip().split(':')[1]
                for item in items[1:]:
                    value += item.strip()
                info[items[0].strip().split(':')[0]] = value
            except:
                pass
        # time
        info['time'] = bs.find("meta",{"property":"article:published_time"})['content']
        
        # decription, contact
        info['description'] = ""
        try:
            element = bs.find("div",{"class":"re-content"}).find_all("p")
            for chil in element[0].find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True):
                info['description'] += chil.strip()+'\n'
        except:
            element = bs.find("div",{"class":"re-content"})
            for chil in element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True):
                info['description'] += chil.strip()+'\n'
        # contact
        try:
            info['contact'] = element[1].text.strip()
        except:
            pass
        # print(info)
        # return
        return self.saveFile(filename, info)

bds = Batdongsan321()