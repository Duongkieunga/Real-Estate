import os, bs4, html, json, codecs
from bs4 import BeautifulSoup

class Vndiaoc:
    path = "/home/nga/Documents/20193/Project/request/Datas/vndiaoc.com"
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                print(filename)
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # return

    def saveFile(self, filename, info):
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        info = dict()
        info['title'] = bs.find("div", {"class":"the-title"}).text.strip()
        
        element = bs.find("div", {"class":"the-attr"}).find_all("li")
        for chil in element:
            items = chil.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            value = ""
            for item in items[1:]:
                value += item.strip()+" "
            info[items[0].strip()] = value
        
        element = bs.find("div", {"class":"the-cap"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        info['description'] = "\n".join([item.strip() for item in element])
        info['price'] = bs.find("div",{"class":"price"}).text.strip()
        
        elements = bs.find("div",{"class":"gridDesign"}).find_all("li")
        for element in elements:
            item = element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            try:
                info[item[0].strip()] = item[1].strip()
            except:
                info[item[0].strip()] = None

        element = bs.find("div",{"class":"listDesign"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        info['tien ich'] = ", ".join([item.strip() for item in element])
        
        elements = bs.find("div",{"class":"listOption"}).find_all("li")
        for element in elements:
            item = element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            info[item[0].strip()] = item[1].replace(":","").strip()
        # print(info)
        return
        return self.saveFile(filename, info)

bds = Vndiaoc()
